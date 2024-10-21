from context import categorize
import unittest
from testfixtures import tempdir, compare, TempDirectory
import os
import json

FileOs = categorize.FileOs

class test_FileOs(unittest.TestCase):
    """
    Ensure file object can get set and output paths to files
    """
    def setUp(self):
        self.d = TempDirectory()
        self.base_path =  self.d.path + "/test"
        self.d.makedir(self.base_path)
        self.file_obj = FileOs(self.base_path)
        
        cats = [{"name": "Zophie", "desc": "chubby"}, {"name": "Pooka", "desc": "fluffy"}]
        file_path = os.path.join(self.base_path, 'read_cats.json')
        with open(file_path, mode='w', encoding='utf-8') as feedsjson:
            json.dump(cats, feedsjson)
        

    
    def tearDown(self):
        self.d.cleanup()

    def test_creates_new_file_object(self):
        self.assertIsNotNone(self.file_obj)

    def test_init_sets_base_path(self):
        self.assertEqual(self.file_obj._base_path, self.base_path)

    def test_can_get_base_path(self):
        self.assertEqual(self.file_obj.get_base_path(), self.base_path)

    def test_can_set_base_path(self):
        new_base_path = self.d.path + "/new_path"
        self.file_obj.set_base_path(new_base_path)
        self.assertEqual(self.file_obj._base_path, new_base_path)

    def test_can_create_file_from_absolute_path(self):
        file_path = "/new_file.txt"
        full_path = self.base_path + file_path
        self.file_obj.set_file(file_path)
        self.assertTrue(os.path.isfile(full_path))

    def test_can_create_file_from_filename(self):
        file_path = "new_file.txt"
        full_path = os.path.join(self.base_path, file_path)
        self.file_obj.set_file(file_path)
        self.assertTrue(os.path.isfile(full_path))

    def test_will_create_file_in_folder_not_make_file_name_plus_folder(self):
        file_path = "new_file.txt"
        false_full_path = self.base_path + file_path
        full_path = os.path.join(self.base_path, file_path)
        self.file_obj.set_file(file_path)
        self.assertFalse(os.path.isfile(false_full_path))
        self.assertTrue(os.path.isfile(full_path))

    def test_will_set_content_in_file(self):
        cats = [{"name": "Zophie", "desc": "chubby"}, {"name": "Pooka", "desc": "fluffy"}]
        file_path = "new_file.txt"
        full_path = os.path.join(self.base_path, file_path)
        self.file_obj.set_json_file(file_path, cats)
        with open(full_path, mode="r", encoding="utf-8") as feedsjson:
            test_contents = json.load(feedsjson)

        self.assertEqual(test_contents, cats)

    def test_can_read_contents_of_file(self):
        cats = [{"name": "Zophie", "desc": "chubby"}, {"name": "Pooka", "desc": "fluffy"}]
        file_path = os.path.join(self.base_path, 'read_cats.json')
        
        test_cats = self.file_obj.read_file(file_path)
        self.assertEqual(test_cats, cats)

    def test_can_copy_file_from_one_place_to_another(self):
        source_path = 'read_cats.json'
        dest_path = 'pasted_cats.json'
        full_dest_path = os.path.join(self.base_path, dest_path)

        self.file_obj.copy_file(source_path, dest_path)
        self.assertTrue(os.path.isfile(full_dest_path))

    def test_can_return_parent_folder_name(self):
        full_path = 'archive/2019-01-18_13-53-00/Dvndh6DUYAAF1rM.jpg'
        parent_name = self.file_obj.get_parent_folder_name(full_path)
        self.assertEqual(parent_name, '2019-01-18_13-53-00')

if __name__ == "__main__":
    unittest.main()