sudo apt-get update
sudo apt-get -y install git btrfs-tools

sudo mkfs.btrfs /dev/sdb
sudo mkdir /mnt/btrfs
sudo mount -t btrfs /dev/sdb /mnt/btrfs
sudo mkdir /mnt/docker

curl -sSL https://get.docker.com/ | sudo sh

git clone https://github.com/robhaswell/btrfs-docker-plugin.git

cd btrfs-docker-plugin

sudo python setup.py install
