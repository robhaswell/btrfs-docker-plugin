# btrfs-docker-plugin
An example Docker plugin implementing BTRFS volumes.

`sudo docker run -ti -v test:/test --volume-driver=btrfs busybox`

`sudo btrfs subvolume list /mnt/btrfs`
