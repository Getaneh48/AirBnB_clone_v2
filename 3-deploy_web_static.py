#!/usr/bin/python3
"""
a Fabric script that creates and distributes an archive to
a web servers, using the function deploy
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


def do_pack():
    """
    generates a tar archive from the web_static folder
    """

    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return (file_name)
    except error as err:
        return None


def deploy():
    """
    A function to archive and deploy the web_static folder to a remot
    servers.
    """
    path = do_pack()
    if path is not None:
        return do_deploy(path)
    return False
