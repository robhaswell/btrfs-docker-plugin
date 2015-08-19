import os
from flask import Flask, request
app = Flask(__name__)

@app.route('/Plugin.Activate', methods=['POST'])
def plugin_activate():
    return '{"Implements": ["VolumeDriver"]}'

@app.route('/VolumeDriver.Create', methods=['POST'])
def volume_create():
    data = request.get_json()
    os.system("btrfs subvolume create /mnt/btrfs/%s" % (data['Name'],))
    return '{"Err": null}'

@app.route('/VolumeDriver.Mount', methods=['POST'])
def volume_mount():
    data = request.get_json()
    os.system("mount -t btrfs -o subvol=%s /dev/sdb /mnt/docker/%s" % (data['Name'], data['Name']))
    return '{"Mountpoint": "/mnt/docker/%s", "Err": null}' % (data['Name'],)

@app.route('/VolumeDriver.Path', methods=['POST'])
def volume_path():
    data = request.get_json()
    os.system("mount -t btrfs -o subvol=%s /dev/sdb /mnt/docker/%s" % (data['Name'], data['Name']))
    return '{"Mountpoint": "/mnt/docker/%s", "Err": null}' % (data['Name'],)

@app.route('/VolumeDriver.Unmount', methods=['POST'])
def volume_unmount():
    data = request.get_json()
    os.system("unmount /mnt/docker/%s" % (data['Name'],))
    return '{"Err": null}'

def main():
    app.run()
