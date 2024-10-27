# from .context import categorize
# import os
# import unittest

# class controller(unittest.TestCase):
#     """
#     ensure that this will recognize images
#     Post the json in a folder
#     determine the image type (stat, main, side 1 and 2)
#     extract the weapon name from the stat page
#     post the weapon name and image group folder date stamp to an archive file
#     move and rename the image to staging location for image cropping
#     """

#     def setUp(self):
#         self.source_json_path = './tests/_testArtifacts/test_controller/Ruby_Crystal_Ring_Stats.json'
#         self.json = categorize.find_in_json.get_json(self.source_json_path)
#         self.weapon_name = categorize.get_weapon_name(self.json)
#         self.character_map = './tests/_testArtifacts/test_controller/weapon_character_pairs.json'
#         self.weapon_map = './tests/_testArtifacts/test_controller/__temp/folder_weapon_pairs.json'
#         self.pair = categorize.ArchivePair(self.weapon_map)
#         self.image_path = './tests/_testArtifacts/test_controller/abcdefg_ruby_crystalring_bdc.jpg'
#         self.final_path_folder = './tests/_testArtifacts/test_controller/__temp/'
#         self.base_path = './tests/_testArtifacts/test_controller/'

#     # Json can be gotten
#     def test_can_get_json(self):
#         self.json = categorize.find_in_json.get_json(self.source_json_path)
#         self.assertIsNotNone(self.json)
#     # Determine image type based on json
#     def test_can_tell_it_is_stats_image(self):
#         picture_type = categorize.determine_picture_type(self.json)
#         self.assertEqual(picture_type, 'Stat')
#     # If it is a stat screen

#         # get the weapon name
#     def test_can_get_weapon_name(self):
#         weapon_name = categorize.get_weapon_name(self.json)
#         self.assertEqual(weapon_name, 'Crystaring')

#         # figure out the character name based on the weapon name
#     def test_get_character_name_from_weapon_name(self):
#         character_name = categorize.determine_character(self.weapon_name, self.character_map)
#         self.assertEqual(character_name, 'Ruby')
        
#         # write the weapon name to the pair file
#     def test_can_write_image_weapon_pair_to_file(self):
#         categorize.write_weapon_map_to_file('test_controller', self.weapon_name, self.pair)

#         data = [{"key":'test_controller',"value":self.weapon_name}]
#         self.assertEqual(data, self.pair.read_pair_file())
#         # copy the file to the staging folder with the correct name

#     def test_reads_weapon_name_from_file(self):
#         couple = self.pair.get_pair('test_controller')
#         self.assertEqual(couple['value'], 'Crystaring')

#     def test_gets_final_file_name_from_files(self):
#         file_object = categorize.FileOs(base_path=self.base_path)
#         file_name = categorize.get_image_file_name(file_object=file_object)
#         self.assertEquals(file_name, 'Ruby_Crystaring_Stats.jpg')

#     def test_moves_the_file_to_staging_with_correct_name(self):
#         pass

#     def test_z_final_cleanup(self):
#         os.remove(self.weapon_map)

# if __name__ == '__main__':
#     unittest.main()