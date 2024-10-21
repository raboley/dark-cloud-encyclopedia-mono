import unittest
from context import categorize


json_path = './tests/_testArtifacts/test_is_weapon_stat_screen/picture_text/test.json'
main_screen_path = './tests/_testArtifacts/test_is_weapon_stat_screen/picture_text/Ruby_Goddes_Ring-Main.json'
stat_screen_path = './tests/_testArtifacts/test_is_weapon_stat_screen/picture_text/Ruby_Crystal_Ring_Stats.json'
toan_screen_path = './tests/_testArtifacts/test_is_weapon_stat_screen/picture_text/Toan_Choora_Stats.json'
file_path = './tests/_testArtifacts/test_is_weapon_stat_screen/all_weapons.json'

class test_image_is_weapon_stat_screen(unittest.TestCase):
    """
    Ensure that we can correctly identify if something is weapon stat screen or not
    """

    def test_weapon_stat_screen_image_is_stat_image(self):
        self.assertTrue(categorize.image_is_weapon_stat_screen(source_text=json))

    def test_NON_weapon_stat_screen_image_is_NOT_stat_image(self):
        fail_json = categorize.get_json(main_screen_path)
        self.assertFalse(categorize.image_is_weapon_stat_screen(source_text=fail_json))

class test_set_weapon_name(unittest.TestCase):
    """
    Ensure that if it is a weapon stat screen, we can determine the weapon name from it
    """
    def test_can_set_weapon_name_if_not_exact(self):
        weapons = categorize.get_weapon_list(file_path)
        pass_json = categorize.get_json(stat_screen_path)
        weapon_name = categorize.get_weapon_name(source_text=pass_json, id=4, weapon_list=weapons)
        self.assertEqual(weapon_name,'Crystal Ring')

    def test_weapon_name_does_not_have_modifier_and_is_exact(self):
        toan_json = categorize.get_json(toan_screen_path)
        weapons = categorize.get_weapon_list(file_path)
        self.assertEqual(categorize.get_weapon_name(source_text=toan_json, id=4, weapon_list=weapons),'Choora')

class test_determine_character_name(unittest.TestCase):
    """
    Ensure that if we have a weapon name we can determine who it belongs to
    """
    def test_choora_belongs_to_toan(self):
        self.assertEqual(categorize.determine_character(weapon_name='Choora', filepath=file_path), 'Toan')



class test_get_weapon_list(unittest.TestCase):

    def test_get_weapon_list_returns_list_of_weapon_names(self):
        weapons = categorize.get_weapon_list(file_path)
        self.assertIn('Choora', weapons)

# class test_archive_weapon_map(unittest.TestCase):
#     """ Ensure we can set the thing correctly """
json = [{'DetectedText': 'ATTACHMENT', 'Type': 'LINE', 'Id': 0, 'Confidence': 99.18334197998047, 'Geometry': {'BoundingBox': {'Width': 0.08702175319194794, 'Height': 0.04405874386429787, 'Left': 0.7036759257316589, 'Top': 0.10547396540641785}, 'Polygon': [{'X': 0.7036759257316589, 'Y': 0.10547396540641785}, {'X': 0.7906976938247681, 'Y': 0.10547396540641785}, {'X': 0.7906976938247681, 'Y': 0.14953270554542542}, {'X': 0.7036759257316589, 'Y': 0.14953270554542542}]}}, {'DetectedText': 'WEAPON', 'Type': 'LINE', 'Id': 1, 'Confidence': 99.72587585449219, 'Geometry': {'BoundingBox': {'Width': 0.09527381509542465, 'Height': 0.05073431134223938, 'Left': 0.29482370615005493, 'Top': 0.11481975764036179}, 'Polygon': [{'X': 0.29482370615005493, 'Y': 0.11481975764036179}, {'X': 0.3900975286960602, 'Y': 0.11481975764036179}, {'X': 0.39084771275520325, 'Y': 0.1642189621925354}, {'X': 0.29482370615005493, 'Y': 0.16555407643318176}]}}]

if __name__ == "__main__":
    unittest.main()