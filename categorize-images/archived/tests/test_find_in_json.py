import sys


import unittest

from tests.context import categorize

#find = rekognize.get_json

json_path = './tests/_testArtifacts/test_find_in_json/picture_text/test.json'
main_screen_path = './tests/_testArtifacts/test_find_in_json/picture_text/Ruby_Goddes_Ring-Main.json'
stat_screen_path = './tests/_testArtifacts/test_find_in_json/picture_text/Ruby_Crystal_Ring_Stats.json'
toan_screen_path = './tests/_testArtifacts/test_find_in_json/picture_text/Toan_Choora_Stats.json'

class test_get_json(unittest.TestCase):
    """
    Ensure we can read json from a file
    """
    def test_returns_json_from_path(self):
        self.assertEqual(categorize.find_in_json.get_json(json_path), json)

class test_has_text(unittest.TestCase):
    """
    Ensure that has text correctly can search through the json
    """
    def test_has_text_ATTACHMENT(self):
        self.assertEqual(categorize.find_in_json.has_text(source_text=json, find_text='ATTACHMENT'),1)
    
    def test_has_text_WEAPON(self):
        self.assertEqual(categorize.find_in_json.has_text(source_text=json, find_text='WEAPON'),True)

    def test_has_text_ATTACHMENT_false(self):
        fail_json = categorize.find_in_json.get_json(main_screen_path)
        self.assertEqual(categorize.find_in_json.has_text(source_text=fail_json, find_text='ATTACHMENT'),False)

    def test_has_text_WEAPON_false(self):
        fail_json = categorize.find_in_json.get_json(main_screen_path)
        self.assertEqual(categorize.find_in_json.has_text(source_text=fail_json, find_text='WEAPON'),True)
    
class test_find_value_by_id(unittest.TestCase):
    """
    Ensure that value returned when searching json for a particular Id is correct
    """
    def test_has_text_found_weapon_name(self):
        pass_json = categorize.find_in_json.get_json(stat_screen_path)
        self.assertEqual(categorize.find_in_json.find_value_by_id(source_text=pass_json, id=4),'Crystaring')

json = [{'DetectedText': 'ATTACHMENT', 'Type': 'LINE', 'Id': 0, 'Confidence': 99.18334197998047, 'Geometry': {'BoundingBox': {'Width': 0.08702175319194794, 'Height': 0.04405874386429787, 'Left': 0.7036759257316589, 'Top': 0.10547396540641785}, 'Polygon': [{'X': 0.7036759257316589, 'Y': 0.10547396540641785}, {'X': 0.7906976938247681, 'Y': 0.10547396540641785}, {'X': 0.7906976938247681, 'Y': 0.14953270554542542}, {'X': 0.7036759257316589, 'Y': 0.14953270554542542}]}}, {'DetectedText': 'WEAPON', 'Type': 'LINE', 'Id': 1, 'Confidence': 99.72587585449219, 'Geometry': {'BoundingBox': {'Width': 0.09527381509542465, 'Height': 0.05073431134223938, 'Left': 0.29482370615005493, 'Top': 0.11481975764036179}, 'Polygon': [{'X': 0.29482370615005493, 'Y': 0.11481975764036179}, {'X': 0.3900975286960602, 'Y': 0.11481975764036179}, {'X': 0.39084771275520325, 'Y': 0.1642189621925354}, {'X': 0.29482370615005493, 'Y': 0.16555407643318176}]}}]