# /import os
# import json

# class ArchivePair:
#     _filepath: str = ''

#     def __init__(self, filepath):
#         self._filepath = filepath
        
#     def set_pair(self, key, value):
#         self.make_new_pair_file_if_needed()
#         feeds = self.read_pair_file()
#         self.add_new_pair(key, value, feeds)


#     def make_new_pair_file_if_needed(self):
#         if not os.path.exists(self._filepath):
#             with open(self._filepath, mode='w', encoding='utf-8') as f:
#                 json.dump([], f)

#     def read_pair_file(self):
#         with open(self._filepath, mode='r', encoding='utf-8') as feedsjson:
#             return json.load(feedsjson)

#     def add_new_pair(self, key, value, feeds):
#         with open(self._filepath, mode='w', encoding='utf-8') as feedsjson:
#             entry = {
#                 'key': key, 
#                 'value': value
#                 }
#             feeds.append(entry)
#             json.dump(feeds, feedsjson)

#     def get_pair(self, key):
#         data = self.read_pair_file()
#         return next(item for item in data if item["key"] == key)
        