#!/usr/bin/python3
"""deleting out-of-date archives"""

from fabric.api import env


env.user = 'ubuntu'
env.hosts = ['34.232.67.39', '18.233.63.201']
# env.key_filename = "path to the ssh private key"


def do_clean(number=0):
    """Cleaning up"""
    if number == 0 || number == 1 || number == 2:
       pass
    else:
       with lcd("versions/"):
           local("ls -lt | awk 'NR >= 3' | xargs rm -f")
       run("rm -f /data/web_static/releases/{}*".format(endswith(".tgz")))
       print("Am done cleaning up!!")
