import os
import json
from shutil import copyfile

# -*- coding: utf-8 -*-
import os
import ntpath


def path_basename(path):
    trash, tail = ntpath.split(path)
    filebasename = os.path.splitext(tail)[0]
    return filebasename

class FileOs():
    
    def get_file(self):
        pass

    def set_file(self, path, contents=''):
        full_path = self.join_path(path)
        f= open(full_path,"w+")
        f.write(contents)
        f.close()

    def set_json_file(self, path, json_content):
        file_path = self.join_path(path)
        with open(file_path, mode='w', encoding='utf-8') as feedsjson:
            json.dump(json_content, feedsjson)

    def read_file(self, path):
        with open(path, mode="r", encoding="utf-8") as feedsjson:
            return json.load(feedsjson)

    def join_path(self, path):
        if path[:1] == '/':
            return self._base_path + path
        else:
            return os.path.join(self._base_path, path)

    def copy_file(self, source_path, dest_path):
        full_source_path = self.join_path(source_path)
        full_dest_path = self.join_path(dest_path)
        copyfile(full_source_path, full_dest_path)

    def __init__(self, base_path):
        self._base_path = base_path

    def set_base_path(self, base_path):
        self._base_path = base_path
    
    def get_base_path(self):
        return self._base_path

    def get_parent_folder_name(self, key):
        head, tail = ntpath.split(key)
        trash, parent_folder = ntpath.split(head)
        return parent_folder


