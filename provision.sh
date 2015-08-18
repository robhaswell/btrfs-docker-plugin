sudo apt-get update
sudo apt-get -y install git btrfs-tools

git clone https://github.com/robhaswell/btrfs-docker-plugin.git
sudo mkfs.btrfs /dev/sdb
sudo mkdir /mnt/btrfs
sudo mount -t btrfs /dev/sdb /mnt/btrfs
sudo mkdir /mnt/docker
