import unittest
from context import categorize

class test_move_to_weapon_folder(unittest.TestCase):
    """
    Ensure that images get moved to the correct folder
    """

    def test_can_recognize_image_local(self):
        response = categorize.rekognize_image_json_local('/Users/russellboley/Downloads/Git/categorize-images/tests/_testArtifacts/test_controller/abcdefg_ruby_crystalring_bdc.jpg')
        self.assertEqual(response, 'asegaseg')

    

    
if __name__ == '__main__':
    unittest.main()