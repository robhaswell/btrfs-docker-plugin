curl -sSL https://get.docker.com/ | sudo sh
sudo service docker restart
sudo mkdir -p /run/docker/plugins

sudo apt-get -y install git btrfs-tools python-setuptools build-essential python-dev socat

sudo mkfs.btrfs /dev/sdb
sudo mkdir /mnt/btrfs
sudo mount -t btrfs /dev/sdb /mnt/btrfs
sudo mkdir /mnt/docker

git clone https://github.com/robhaswell/btrfs-docker-plugin.git

cd btrfs-docker-plugin

sudo python setup.py install

sudo socat UNIX-LISTEN:/run/docker/plugins/btrfs.sock,fork TCP:127.0.0.1:5000
