import unittest
import get_tweet_name


client = get_tweet_name
username = 'cloud_images'

class test_image_text_decider(unittest.TestCase):
    """
    Ensure if something is a stat screen, it takes the appropriate actions
    """
    def test_is_weapon_stat_screen(self):
        self.assertEqual(client.get_tweets(username),'stat_screen')