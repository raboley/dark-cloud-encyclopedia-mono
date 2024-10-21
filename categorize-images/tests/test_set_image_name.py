import unittest
from testfixtures import tempdir, compare, TempDirectory

from context import categorize

class test_set_image_name(unittest.TestCase):
    """
    Ensure that we can set the image name correctly with weapon, character name and type
    """
    def setUp(self):
        self.d = TempDirectory()
        self.args = {
            "bucket_name": "dark-cloud-bucket",
            "image_key": "archive/2019-01-27_18-20-31/DwJ6vY_VAAIexyj.jpg",
            "bucket_image_folder_path": "new_images/",
            "bucket_text_folder_path": "new_text/",
            "local_text_folder": self.d.path,
            "weapon_mapping_file": "mappings/all_weapons.json",
            "datefolder_character_weapon_mapping_file": "__test/mappings/datefolder_character_weapon_mapping_file.json",
            "output_folder_name": "__test/weapons",
            "output_bucket_name": "dark-cloud-bucket"
        }
        self.file_object =  categorize.FileS3(self.args['bucket_name'])
        self.output_file_object = categorize.FileS3(self.args["output_bucket_name"])
        
    def tearDown(self):
        self.d.cleanup

    def test_get_image_name_when_is_stat_screen(self):
        image_name = categorize.get_image_name(self.args, self.file_object, self.output_file_object)
        self.assertEqual(image_name, 'Toan_Choora_Stat.jpg')

    def test_get_image_name_when_is_side_screen(self):
        self.args["image_key"] = 'archive/2019-01-27_18-20-31/DwJ6v8fUcAAa-Ov.jpg'

        image_name = categorize.get_image_name(self.args, self.file_object, self.output_file_object)
        self.assertEqual(image_name, 'Toan_Choora_Side1.jpg')

    def test_get_image_name_when_is_main_screen(self):
        self.args["image_key"] = 'archive/2019-01-27_18-20-31/DwJ6vmKVAAAcjG3.jpg'

        image_name = categorize.get_image_name(self.args, self.file_object, self.output_file_object)
        self.assertEqual(image_name, 'Toan_Choora_Main.jpg')

    # def test_get_image_name_when_is_side_screen(self):
    #     self.args["image_key"] = 'archive/2019-01-27_18-20-31/DwJ6v8fUcAAa-Ov.jpg'

    #     image_name = categorize.get_image_name(self.args, self.file_object, self.output_file_object)
    #     self.assertEqual(image_name, 'Toan_Choora_Side1.jpg')
    def test_copies_image_from_folder_to_output_with_categorized_name(self):
        categorize.copy_image_to_folder_with_categorized_name(self.args, self.file_object, self.output_file_object)
        test_full_path = self.args["output_folder_name"] + '/Toan_Choora_Stat.jpg'
        self.assertTrue(self.output_file_object.check_existence(test_full_path))

if __name__ == '__main__':
    unittest.main()

#keys = ["archive/2019-01-27_18-20-31/DwJ6v8fUcAAa-Ov.jpg",'archive/2019-01-27_18-20-31/DwJ6vY_VAAIexyj.jpg','archive/2019-01-27_18-20-31/DwJ6vmKVAAAcjG3.jpg','archive/2019-01-27_18-20-31/DwJ6vxHUUAARYrH.jpg']