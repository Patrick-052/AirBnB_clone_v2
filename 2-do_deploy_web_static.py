#!/usr/bin/python3
"""Deploying code to the servers"""
from fabric.api import put, env, run
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
    folder_name = "/data/web_static/releases/{}/".format(filename[:-4])
   
    try:
        put(archive_path, "/tmp/{}".format(filename))
        run("mkdir -p {}".format(folder_name))
        run("tar -xzvf /tmp/{} -C {}".format(filename, folder_name))
        run("rm -f /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(folder_name, folder_name))
        run("rm -rf {}web_static".format(folder_name))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_name))
        print('New version deployed!')
        success = True
    except Exception:
        success = False
    return success
