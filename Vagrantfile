# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

btrfsvol = "btrfs.disk"

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  # create and attach a second disk.
  # warning! this is destructive!!
  config.vm.provider :virtualbox do |vb|
      vb.customize ['createhd', '--filename', btrfsvol, '--size', 1 * 1024]
      vb.customize ['storageattach', :id, '--storagectl', 'SATAController', '--port', 1, '--device', 0, '--type', 'hdd', '--medium', btrfsvol]
  end

  config.vm.network "private_network", ip: "192.168.33.10"

  config.vm.provision "shell", path: "provision.sh"
end
