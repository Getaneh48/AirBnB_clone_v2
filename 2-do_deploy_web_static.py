#!/usr/bin/python3

"""
A Fabric script that distributes an archive to a list of web servers,
using the function do_deploy
"""

from fabric.api import *
from os.path import exists
from datetime import datetime
from os.path import isdir

env.hosts = ['100.25.150.143', '18.206.233.16']


def do_deploy(archive_path):
    """deploys the given archive to the web servers"""

    if exists(archive_path):
        fileName = archive_path.split("/")[-1]
        folderName = fileName.split('.')[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        sudo('mkdir -p {}{}/'.format(path, folderName))
        sudo('sudo tar -xzf /tmp/{} -C {}/{}/'.format(fileName,
                                                      path, folderName))
        sudo('rm /tmp/{}'.format(fileName))
        sudo('mv {0}{1}/web_static/* {0}{1}/'.format(path, folderName))
        sudo('rm -rf {}{}/web_static'.format(path, folderName))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {}{}/ /data/web_static/current'.format(path,
                                                           folderName))
        print("New version deployed!")
        return True
    else:
        return False
