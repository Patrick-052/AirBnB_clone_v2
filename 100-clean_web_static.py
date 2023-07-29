#!/usr/bin/python3
"""deleting out-of-date archives"""

from fabric.api import env, run, local, lcd


env.user = 'ubuntu'
env.hosts = ['34.232.67.39', '18.233.63.201']
# env.key_filename = "path to the ssh private key"


def do_clean(number=0):
    """Cleaning up"""
    if number < 1:
        print("Number must be greater than or equal to 1")
        return
    with lcd("versions/"):
        local("ls -lt | tail -n +{} | xargs rm -f".format(number + 1))
    run("ls -t /data/web_static/releases/ | tail -n +{} | xargs -I {{}}\
        rm -rf /data/web_static/releases/{{}}".format(number + 1))
    print("Done cleaning up!!")
