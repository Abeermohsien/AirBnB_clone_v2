#!/usr/bin/python3
"""
removes old archeove"""

import os
from fabric.api import *

env.hosts = ['52.91.122.57', '52.201.165.108']


def do_clean(number=0):
    """
    remove outofline archeives
    """
    number = 1 if int(number) == 0 else int(number)

    arc = sorted(os.listdir("versions"))
    [arc.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in arc]

    with cd("/data/web_static/releases"):
        arc = run("ls -tr").split()
        arc = [a for a in arc if "web_static_" in a]
        [arc.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in arc]
