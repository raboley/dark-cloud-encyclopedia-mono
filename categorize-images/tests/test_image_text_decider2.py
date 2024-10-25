import unittest
from categorize.image_text_decider import determine_picture_type

class TestImageTextDecider(unittest.TestCase):
    def test_determine_picture_type_stats(self):
        source_text = """
        WEAPON (michem StarBreaker+1 Cou? RI WHp 5,0,78,3 Abss  0Y108} 1200 IOT e IoZ Garnet" Sp mot Gem Can be attached to Mp FNe Meapon:
        """
        expected_type = 'Stats'
        result = determine_picture_type(source_text)
        self.assertEqual(result, expected_type)

if __name__ == '__main__':
    unittest.main()