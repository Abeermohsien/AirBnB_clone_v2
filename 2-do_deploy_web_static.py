#!/usr/bin/python3
"""
fabric file"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['52.91.122.57', '52.201.165.108']


def do_deploy(archive_path):
    """archeive distriput"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        fp = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(fp, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, fp, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(fp, no_ext))
        run('rm -rf {}{}/web_static'.format(fp, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(fp, no_ext))
        return True
    except:
        return False
