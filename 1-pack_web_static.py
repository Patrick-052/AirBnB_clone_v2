#!/usr/bin/python3
""""Generating a .tgz archive from the contents of
    the web_static folder of my AirBnB Cloned repo"""

import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """function containing commands and process to generate the
       .tgz archive"""
    try:
        dir = local("mkdir AirBnB_clone_v2/versions", capture=True)
        local(f"cp -r web_static/ {dir}")
        frmt = datetime.now().strftime("%Y%m%d%H%M%S")
        archive = local(f"tar -czvf web_static_{frmt}.tgz {dir}/.",
                        capture=True)
        return local(os.path.abspath(archive))
    except FileNotFoundError:
        return None
