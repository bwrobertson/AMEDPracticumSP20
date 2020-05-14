import os
import subprocess
import threading
import sys
import time
import re




''' 
    Pertinent user input: {config.vm.box = os
    config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1
    vb.gui = True
    vb.memory = "1024"
    vb.cpus = 1
    config.vm.provision "shell", inline: <<-SHELL
        //commands
    SHELL
    
    json -
    vm_name
    entity_type
    os
    vm_files []
    software []
    mem
    proc
    vbox [
        boot
        vrde
        apis
        formware
        rtcuseutc
        cpuexecutioncap
        pae
        hwvirtex
        nestedpaging
    ]
'''
class Check():
    def __init__(self):
        self.amed_home = os.getcwd() # to get back to main directory 

    def edit_vagrantfile(self, user_input):
        print('inside check')
        self.amed_home = os.getcwd()
        values_to_set = user_input # should be a dictionary of values

        # collect folders
        vagrant_file_to_edit = values_to_set['os']
        vagrant_path = ""
        for f in os.listdir(self.amed_home):
            if 'vagrant' in f and vagrant_file_to_edit in f:
                vagrant_path = self.amed_home+os.sep+f
                print(vagrant_path)

        if vagrant_path == '':
            return
        # open file for editing
        vagrant_file = vagrant_path+os.sep+'Vagrantfile'
        
        fd = open(vagrant_file, 'r')
        content = fd.readline()

        # make directory for the vagrant files of the scenario vms
        make_dir = self.amed_home+os.sep+'scenario'
        if not os.path.exists(make_dir):
            os.mkdir(make_dir)

        # create specific folders to hold the scenario's
        # vm vagrant files
        vm_vagrantfile_folder = make_dir+os.sep+'vagrant_'+vagrant_file_to_edit
        if not os.path.exists(vm_vagrantfile_folder):
            os.mkdir(vm_vagrantfile_folder)
        new_file = open(vm_vagrantfile_folder+os.sep+'Vagrantfile', 'w')
        
        while content:
            for key in values_to_set:
                
                if 'vb.memory' in content and 'mem' in key:
                    l = content.split('vb.memory')
                    print(l)
                    s = l[0]+'vb.memory = '+'\"'+values_to_set[key]+'\"'
                    print(s)
                    content = s

                elif 'vb.cpus' in content and 'proc' in key:
                    l = content.split('vb.cpus')
                    s = l[0]+'vb.cpus = '+values_to_set[key]
                    content = s

                elif 'config.vm.network' in content and not '#' in content and 'config.vm.network' in key:
                    l = content.split(',')
                    s = l[0]+','+l[1]+', host: '+values_to_set[key]+','+l[3]
                    content = s

                elif '--cpuexecutioncap' in content:
                    print('inside vb.customize')
                    if '--cpuexecutioncap' in content and '--cpuexecutioncap' in key:
                        s = 'vb.customize ["modifyvm", :id, "--cpuexecutioncap", "'+values_to_set[key]+'"]'
                        print(s)
                        print(values_to_set[key])
                        content = s
                    
                    if '--vrde' in content and '--vrde' in key:
                        s = 'vb.customize ["modifyvm", :id, "--vrde", "'+values_to_set[key]+'"]'
                        content = s
                    
                    if '--apic' in content and '--apic' in key:
                        s = 'vb.customize ["modifyvm", :id, "--apic", "'+values_to_set[key]+'"]'
                        content = s

                    if '--rtcuseutc' in content and '--rtcuseutc' in key:
                        s = 'vb.customize ["modifyvm", :id, "--rtcuseutc", "'+values_to_set[key]+'"]'
                        content = s

                    if '--pae' in content and '--pae' in key:
                        s = 'vb.customize ["modifyvm", :id, "--pae", "'+values_to_set[key]+'"]'
                        content = s

                    if '--hwvirtex' in content and '--hwvirtex' in key:
                        s = 'vb.customize ["modifyvm", :id, "--hwvirtex", "'+values_to_set[key]+'"]'
                        content = s

                    if '--nestedpaging' in content and '--nestedpaging' in key:
                        s = 'vb.customize ["modifyvm", :id, "--nestedpaging", "'+values_to_set[key]+'"]'
                        content = s


                elif key == 'file':
                    print("Nothing.")
                    # depends on OS
                    # l = content.split('vb.memory')
                    # s = l[0]+'vb.memory = 'values_to_set[key]
                    
                # adding vbox settings
                # elif key == 'vbox':
                #     for i in values_to_set['vbox']:
            
            new_file.write(content)
            content = fd.readline()
        
        fd.close()
        new_file.close()
        print("File made!")

    def main(self, vm_settings):
        print("Entered main().")
        type_of_vm = ""
        while True:
            type_of_vm = str(input("Enter VM OS you'd: ")).lower()
            if type_of_vm == 'windows':
                break
            elif type_of_vm == 'ubuntu':
                break
            elif type_of_vm == 'attacker':
                break
            else:
                continue

        d = {'config.vm.box': type_of_vm, 'vb.memory': '2048', 'vb.cpus':'2',
             'config.vm.network': '8082'}

        self.edit_vagrantfile(d)
        return

if __name__ == "__main__":
    c = Check()
