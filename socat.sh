#!/bin/sh
exec socat UNIX-LISTEN:/run/docker/plugins/btrfs.sock,fork TCP:127.0.0.1:5000
