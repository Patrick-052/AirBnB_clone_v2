#!/usr/bin/python3
""""Generating a .tgz archive from the contents of
    the web_static folder of my AirBnB Cloned repo"""

from fabric.api import local
from datetime import datetime
from fabric.decorators import runs_once


@runs_once
def do_pack():
    """function containing commands and process to generate the
       .tgz archive"""
    local("mkdir -p versions")
    frmt = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(frmt)
    tgz_path = "versions/{}".format(archive_name)
    result = local("tar -czvf {} web_static".format(tgz_path))

    if result.failed:
        return None
    return tgz_path

