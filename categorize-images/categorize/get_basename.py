# -*- coding: utf-8 -*-
import os
import ntpath


def path_basename(path):
    trash, tail = ntpath.split(path)
    filebasename = os.path.splitext(tail)[0]
    return filebasename