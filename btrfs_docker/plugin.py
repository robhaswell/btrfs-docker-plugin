import os, json
from flask import Flask, request
app = Flask(__name__)
app.debug = True

@app.route('/Plugin.Activate', methods=['POST'])
def plugin_activate():
    return '{"Implements": ["VolumeDriver"]}'

@app.route('/VolumeDriver.Create', methods=['POST'])
def volume_create():
    data = json.loads(request.get_data())
    os.system("mkdir -p /mnt/docker/%s" % (data['Name'],))
    os.system("btrfs subvolume create /mnt/btrfs/%s" % (data['Name'],))
    return '{"Err": null}'

@app.route('/VolumeDriver.Mount', methods=['POST'])
def volume_mount():
    data = json.loads(request.get_data())
    os.system("mount -t btrfs -o subvol=%s /dev/sdb /mnt/docker/%s" % (data['Name'], data['Name']))
    return '{"Mountpoint": "/mnt/docker/%s", "Err": null}' % (data['Name'],)

@app.route('/VolumeDriver.Path', methods=['POST'])
def volume_path():
    data = json.loads(request.get_data())
    return '{"Mountpoint": "/mnt/docker/%s", "Err": null}' % (data['Name'],)

@app.route('/VolumeDriver.Unmount', methods=['POST'])
def volume_unmount():
    data = json.loads(request.get_data())
    os.system("umount /mnt/docker/%s" % (data['Name'],))
    return '{"Err": null}'

def main():
    app.run()
