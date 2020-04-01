# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  
  # Box Settings
  config.vm.box = "ubuntu/trusty64"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = 2048
    vb.cpus = 4
  end

  config.vm.network "private_network", ip: "192.168.33.10"

      # Folder Settings
  config.vm.synced_folder ".", "/var/www/html", :nfs => { :mount_options => ["dmode=777", "fmode=666"] }

  # Provision Settings
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
  SHELL
end
    
#config.vm.define "windows" do |windows|
  #  windows.vm.box = "opentable/win-2012r2-standard-amd64-nocm"
  #end
  
    # Network Settings
  # config.vm.network "forwarded_port", guest: 80, host: 8080
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
  # config.vm.network "public_network"
    
    # Folder Settings
 #  config.vm.synced_folder ".", "/var/www/html", :nfs => { :mount_options => ["dmode=777", "fmode=666"] }

    # Provision Settings
   #config.vm.provision "shell", inline: <<-SHELL
   #  apt-get update
  #   apt-get install -y apache2
 #  SHELL
#end
