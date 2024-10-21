import unittest
from context import categorize

class test_read_file_s3(unittest.TestCase):
    """
    Ensure we can read files from s3
    """

    def test_can_recognize_image_local(self):
        response = categorize.read_file_s3('dark-cloud-bucket', 'mappings/all_weapons.json')
        self.assertEqual(response, 'asegaseg')
    
if __name__ == '__main__':
    unittest.main()