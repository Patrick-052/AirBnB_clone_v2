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
    archive_name = "web_static_{}.tgz".format(frmt)
    tgz_path = os.path.join(arch_path, archive_name)
    result = local("tar -czvf {} web_static".format(tgz_path))
    file_size = os.stat(tgz_path).st_size
    print("web_static packed: versions/web_static_{}.tgz -> {}Bytes"
          .format(frmt, file_size))

    if result.failed:
        return None
    return tgz_path