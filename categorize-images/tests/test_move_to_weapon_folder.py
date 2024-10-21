import unittest

def get_weapon_name_from_archive(key, dictionary):
    return dictionary[key]

class test_move_to_weapon_folder(unittest.TestCase):
    """
    Ensure that images get moved to the correct folder
    """

    def test_get_weapon_name_from_archive(self):
        key = '2019-01-18_13-53-02'
        dictionary = {
            '2019-01-18_13-53-00': 'Chopper',
            '2019-01-18_13-53-01': 'Crystal Ring',
            '2019-01-18_13-53-02': 'Choora'
        }
        real_weapon_name ='Choora'
        weapon_name = get_weapon_name_from_archive(key=key, dictionary=dictionary)
        self.assertEqual(real_weapon_name, weapon_name)


