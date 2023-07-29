#!/usr/bin/python3
"""Deploying code to the servers"""
from fabric.api import sudo, put, env
import os


env.user = 'ubuntu'
env.hosts = ['34.232.67.39', '18.233.63.201']
# env.key_filename = "path to the ssh private key"


def do_deploy(archive_path):
    """Checking if archive file exists and deploying
    it to the servers"""
    if not os.path.exists(archive_path):
       return False

    filename = os.path.basename(archive_path)
    folder_name = "/data/web_static/releases/" + filename[:-4]
    put(archive_path, "/tmp/")
    sudo("mkdir -p {}".format(folder_name))
    sudo("tar -xzvf /tmp/{} -C {}".format(filename, folder_name))
    sudo("rm -f /tmp/{}".format(filename))
    sudo("rm -rf /data/web_static/current")
    sudo("ln -s {} /data/web_static/current".format(folder_name))
    
    return True

