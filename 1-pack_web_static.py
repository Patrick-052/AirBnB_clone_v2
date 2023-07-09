#!/usr/bin/python3
""""Generating a .tgz archive from the contents of
    the web_static folder of my AirBnB Cloned repo"""

import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """function containing commands and process to generate the
       .tgz archive"""
    local("mkdir -p versions")
    arch_path = 'versions'
    frmt = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{frmt}.tgz"
    path = os.path.join(arch_path, archive_name)
    result = local(f"tar -czvf {path} web_static")

    if result.failed:
        return None
    return path
