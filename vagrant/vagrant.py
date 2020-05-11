import os
import subprocess
import threading
import sys
import time
import re
import platform
import json



''' 
    Pertinent user input: {config.vm.box = os
    config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1
    vb.gui = True
    vb.memory = "1024"
    vb.cpus = 1
    config.vm.provision "shell", inline: <<-SHELL
        //commands
    SHELL
'''
class Check():
    def __init__(self):
        self.amed_home = os.getcwd() # to get back to main directory 

        self.vbox_manage_path = ''
        path_var = os.environ['PATH']
        folders = path_var.split(';')
        for f in folders:
            if 'VirtualBox' in f:
                if platform.system().lower() == 'windows':
                    self.vbox_manage_path = f+os.sep+'VBoxManage.exe'
                elif platform.system().lower() == 'linux':
                    self.vbox_manage_path = f+os.sep+'VBoxManage'
                elif platform.system().lower() == 'darwin':
                    self.vbox_manage_path = f+os.sep+'VBoxManage'
                else:
                    print("Edit line in enable_rdp() in vagrant.py!")

        return

    def edit_vagrantfile(self, user_input):
        values_to_set = user_input # should be a dictionary of values

        # collect folders
        os_file = values_to_set['config.vm.box']
        vagrant_path = ""
        for f in os.listdir(self.amed_home):
            if 'vagrant' in f and os_file in f:
                vagrant_path = self.amed_home+os.sep+f

        if vagrant_path == '':
            print("Vagrant path empty!")
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
        vm_vagrantfile_folder = make_dir+os.sep+'vagrant_'+os_file
        if not os.path.exists(vm_vagrantfile_folder):
            os.mkdir(vm_vagrantfile_folder)
        new_file = open(vm_vagrantfile_folder+os.sep+'Vagrantfile', 'w')
        
        while content:
            for key in values_to_set:
                
                if 'vb.memory' in content and 'vb.memory' in key:
                    l = content.split('vb.memory')
                    s = l[0]+'vb.memory = '+'\"'+values_to_set[key]+'\"'
                    content = s

                elif 'vb.cpus' in content and 'vb.cpus' in key:
                    l = content.split('vb.cpus')
                    s = l[0]+'vb.cpus = '+values_to_set[key]
                    content = s

                elif 'config.vm.network' in content and not '#' in content and 'config.vm.network' in key:
                            l = content.split(',')
                            s = l[0]+','+l[1]+', host: '+values_to_set[key]+','+l[3]
                            content = s

                
            new_file.write(content)
            content = fd.readline()
        
        fd.close()
        new_file.close()
        print("File made!")
        values_to_set['folder'] = vm_vagrantfile_folder

        if os_file == 'windows':
            files = ['install.bat', 'install2.bat', 'run_collectors.bat']
            for f in files:
                fd = open(vagrant_path+os.sep+f,'r')
                f_new = open(vm_vagrantfile_folder+os.sep+f,'w')
                content = fd.read()
                f_new.write(content)
                fd.close()
                f_new.close()

        f = open(vm_vagrantfile_folder+'_dictionary','w')
        f.write(json.dumps(values_to_set))
        f.close()
        return values_to_set

    # start vm to create vagrant log files, 
    # get activation id, power down to enable rdp,
    # then start to upload
    def start_vm(self, d):

        vagrant_folder = d['folder']
        os.chdir(vagrant_folder)

        print("Running vagrant up...\n")
        proc = subprocess.Popen(['vagrant', 'up'], stdout=subprocess.PIPE)

        for line in iter(proc.stdout.readline,''):
            if line == b'':
                break
            print(line.rstrip())

        poll = proc.poll()
        while True:
            if poll == None:
                print("Alive!")
                poll = proc.poll()
            else:
                break
        


        print("Running vagrant halt...\n")
        proc_0 = subprocess.Popen(['vagrant', 'halt'], stdout=subprocess.PIPE)

        for line in iter(proc_0.stdout.readline,''):
            if line == b'':
                break
            print(line.rstrip())

        if d['config.vm.box'] == 'kali':
            kali_base_key = self.amed_home+os.sep+'vagrant_kali'+os.sep+'private_key'
            ch_to = self.amed_home+os.sep+vagrant_folder+os.sep+'.vagrant'+os.sep+'machines'+os.sep+'default'+os.sep+'virtualbox'
            os.chdir(ch_to)
            fd = open(kali_base_key,'rb')
            ft = open(ch_to+'private_key','wb')
            content = fd.read()
            ft.write(content)
            fd.close()
            ft.close()


        os.chdir(self.amed_home)

        return

    # use VBoxManage
    # use Headless when starting the vm for the scenario
    def enable_rdp(self, d):
        vagrant_folder = d['folder']
        
        ch_to = vagrant_folder+os.sep+'.vagrant'+os.sep+'machines'+os.sep+'default'+os.sep+'virtualbox'
        os.chdir(ch_to)
        self.action_provision_id=-1

        try:

            f=open('action_provision','r') # Get the p_id from the vagrant file
            line=f.read()
            line=line.split(':')
            self.action_provision_id=line[1]

        except:
            print("No provision file found.")

        
        print("\nEnabling RDP...")
        proc = subprocess.Popen([self.vbox_manage_path, 'modifyvm', self.action_provision_id,
         '--vrde', 'on'], stdout=subprocess.PIPE)

        for line in iter(proc.stdout.readline,''):
            if line == b'':
                break
            print(line.rstrip())

        os.chdir(self.amed_home)
        return

    # use ssh
    def upload_files_vm(self, d):
        vagrant_folder = d['folder']
        ubuntu_home = '/home/vagrant/'
        kali_home = '/'
        windows_home = 'C:'+os.sep+'vagrant'+os.sep+'Desktop'+os.sep
        os.chdir(vagrant_folder)

        print("\nRunning vagrant up for uploading file...")
        proc = subprocess.Popen(['vagrant', 'up'], stdout=subprocess.PIPE)

        for line in iter(proc.stdout.readline,''):
            if line == b'':
                break
            print(line.rstrip())

        print("\nUploading file...")
        file_upload = d['file']
        for fu in file_upload:
            file = fu.split(os.sep)[-1]
            if d['config.vm.box'] == 'ubuntu':
                proc_1 = subprocess.Popen(['vagrant', 'upload', fu, ubuntu_home+file], 
                    stdout=subprocess.PIPE)
                
                for line in iter(proc_1.stdout.readline,''):
                    if line == b'':
                        break
                    print(line.rstrip())
            elif d['config.vm.box'] == 'windows':
                proc_1 = subprocess.Popen(['vagrant', 'upload', fu, windows_home+file], 
                    stdout=subprocess.PIPE)
                
                for line in iter(proc_1.stdout.readline,''):
                    if line == b'':
                        break
                    print(line.rstrip())

            elif d['config.vm.box'] == 'kali':
                proc_1 = subprocess.Popen(['vagrant', 'upload', fu, kali_home+file], 
                    stdout=subprocess.PIPE)
                
                for line in iter(proc_1.stdout.readline,''):
                    if line == b'':
                        break
                    print(line.rstrip())                    
  
        else:
            # Neet to find out how to upload 
            # file to windows box
            print("Constructing Windows VM.")

        os.chdir(self.amed_home)
        return


    def main(self):
        print("Entered main().")
        type_of_vm = ""
        while True:
            try:
                type_of_vm = str(input("Enter VM OS you'd: ")).lower()
                if type_of_vm == 'windows':
                    break
                elif type_of_vm == 'ubuntu':
                    break
                elif type_of_vm == 'kali':
                    break
                else:
                    print("Entered: ",type_of_vm)
                    print("Must enter: 'ubuntu', 'kali', or 'windows' .")
                    continue
            except:
                continue

        while True:
            try:
                memory = int(input("Amount of RAM: "))
                if (memory >= 4097 or memory < 511):
                    print("Enter a RAM size between 512 and 4096.")
                    continue
                else:
                    break
            except:
                continue


        d = {'config.vm.box': type_of_vm, 'vb.memory' : str(memory), 'vb.cpus': '1',
             'config.vm.network': '8082', 
             'file': ['C:\\Users\\kmhon\\Desktop\\vagrant_work\\exploit.py']} # files should be placed using ssh

        d = self.edit_vagrantfile(d)
        self.start_vm(d)
        self.enable_rdp(d)
        self.upload_files_vm(d)

        return

if __name__ == "__main__":
    c = Check()
    c.main()
