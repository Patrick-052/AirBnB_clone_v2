#!/usr/bin/python3
""""Generating a .tgz archive from the contents of
    the web_static folder of my AirBnB Cloned repo"""

import os
from fabric.api import local
from datetime import datetime
from fabric.decorators import runs_once


@runs_once
def do_pack():
    """function containing commands and process to generate the
       .tgz archive"""
    local("mkdir -p versions")
    path = ("versions/web_static_{}.tgz"
            .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    result = local("tar -cvzf {} web_static"
                   .format(path))

    if result.failed:
        return None
    return path

