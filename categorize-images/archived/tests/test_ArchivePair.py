# import unittest
# import os
# from testfixtures import tempdir, compare, TempDirectory
# from tests.context import categorize

# Pair = categorize.ArchivePair

# import json

# class test_archive_pair(unittest.TestCase):
#     """
#     Ensure that when something needs to be stored it can be gotten and set
#     """

#     def setUp(self):
#         self.d = TempDirectory()
#         self.filePath =  self.d.path + '/nosql.json'
#         self.pair = Pair(self.filePath)

#     def tearDown(self):
#         self.d.cleanup()

#     def test_make_new_pair_file_if_needed_does_create_file_when_doesnt_exist(self):
#         self.pair.make_new_pair_file_if_needed()
#         self.assertTrue(os.path.isfile(self.filePath))

#     def test_read_file_does_read_json_file(self):
#         data = [{"key":'12-11',"value":'choora'},{"key":'12-12',"value":'crystal_ring'}]
#         with open(self.filePath,'w') as outfile:
#             json.dump(data, outfile)
#         self.assertEqual(data,self.pair.read_pair_file())
        
#     def test_set_pairs_does_create_from_empty(self):
#         data = [{"key":'12-11',"value":'choora'}]
#         self.pair.set_pair('12-11','choora')
#         self.assertEqual(data,self.pair.read_pair_file())

#     def test_set_pairs_appends_to_an_existing_file(self):
#         data = [{"key":'12-11',"value":'choora'},{"key":'12-12',"value":'crystal_ring'}]
#         with open(self.filePath,'w') as outfile:
#             json.dump(data, outfile)
#         self.pair.set_pair('12-13','omega')
#         final_data = [{"key":'12-11',"value":'choora'},{"key":'12-12',"value":'crystal_ring'},{"key":'12-13',"value":'omega'}]
#         data_read = self.pair.read_pair_file()
#         self.assertEqual(final_data, data_read)

#     def test_set_pair_does_store_key_value_pairs(self):
#         key = 'test_key'
#         self.pair.set_pair(key,'test_value')
#         pair = self.pair.get_pair(key)
#         self.assertEqual('test_value', pair['value'])
#         self.assertEqual('test_key', pair['key'])

#     def test_when_adding_a_pair_previous_pairs_are_maintained(self):
#         key = 'test_key2'
#         self.pair.set_pair(key,'test_value2')
#         self.pair.set_pair('test_key','test_value')
#         pair = self.pair.get_pair(key)
#         self.assertEqual('test_value2', pair['value'])
#         self.assertEqual('test_key2', pair['key'])

#     def test_doesnt_add_a_pair_if_it_already_exists(self):
#         key = 'test_key'
#         self.pair.set_pair(key,'test_value')
#         self.pair.set_pair(key,'test_value')
#         pair = self.pair.read_pair_file()
#         self.assertEqual(len(pair), 1)

# if __name__ == '__main__':
#     unittest.main()