#!/usr/bin/python3
"""Fabric script that generates an archive and distribute it to servers"""
from fabric.api import *
from datetime import datetime
from os.path import exists

env.user = "ubuntu"
env.hosts = ["54.158.205.177", "18.207.141.0"]


def do_pack():
    """Generate a .tgz archive from web_static folder"""
    time = datetime.now()
    filename = "web_static_{0:%Y%m%d%H%M%S}.tgz".format(time)
    local("mkdir -p versions")
    archive = local("tar -cvzf versions/{} web_static".format(filename))
    if archive.failed:
        return None
    return "versions/{}".format(filename)


def do_deploy(archive_path):
    """Distribute an archive to web servers"""
    if not exists(archive_path):
        print(f"{archive_path} is not a file")
        return False
    put(archive_path, "/tmp/")
    archive = archive_path.replace(".tgz", "")
    archive = archive.replace("versions/", "")
    run("mkdir -p /data/web_static/releases/{}/".format(archive))
    run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
        .format(archive, archive))
    run("rm /tmp/{}.tgz".format(archive))
    run("mv /data/web_static/releases/{}/web_static/* ".format(archive) +
        "/data/web_static/releases/{}/".format(archive))
    run("rm -rf /data/web_static/releases/{}/web_static".format(archive))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
        .format(archive))
    print("New version deployed!")
    return True
