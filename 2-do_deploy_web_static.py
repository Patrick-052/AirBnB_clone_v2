#!/usr/bin/python3
"""Deploying code to the servers"""
from fabric.api import sudo, put, env
import os
from sys import argv


env.user = 'ubuntu'
env.hosts = ['107.22.143.92', '54.157.181.234']
env.key_filename = "C:\Users\12514\.ssh\id_rsa"


def do_deploy(archive_path):
    """Checking if archive file exists and deploying
    it to the servers"""
    if not os.path.exists(archive_path):
       return False
    
    fl = argv[3].split("/")[-1].split(".")[-2]
    dst = '/tmp/'
    new_dir = '/data/web_static/releases/{}'.format(fl)
    put(archive_path, dst)
    sudo("tar -xzvf {}/{}.tgz -C {}".format(dst, fl, new_dir))
    sudo("rm {}/{}.tgz".format(dst, fl))
    sudo ("rm /data/web_static/current")
    sudo("ln -s {} /data/web_static/current".format(new_dir))

    return True

