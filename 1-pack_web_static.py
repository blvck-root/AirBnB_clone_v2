#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from folder"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generate a .tgz archive from web_static folder"""
    time = datetime.now()
    name = "web_static_{0:%Y%m%d%H%M%S}.tgz".format(time)
    local("mkdir -p versions")
    archive = local("tar -cvzf versions/{} web_static".format(name))
    if archive.failed:
        return None
    return "versions/{}".format(name)
