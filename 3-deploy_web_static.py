#!/usr/bin/python3
"""Creating an archive, deploying it, extracting it in the
   servers and testing if the deployed code works"""

from fabric.api import env
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

env.user = 'ubuntu'
env.hosts = ['34.232.67.39', '18.233.63.201']
# env.key_filename = "path to the ssh private key"


def deploy():
    """creating and deploying and archive file by calling
       functions involved with those tasks"""
    try:
        archive_path = do_pack()
        if not archive_path:
            return False
        deploy_success = do_deploy(archive_path)
        return deploy_success
    except Exception:
        return False
