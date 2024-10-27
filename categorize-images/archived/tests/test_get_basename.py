# -*- coding: utf-8 -*-

from .context import categorize

import unittest

class Get_Basename(unittest.TestCase):
    """Test that the basename is returned from a full path"""

    def test_path_basename_returns_just_basename_of_file(self):
        path = '/Users/russellboley/Downloads/Git/categorizemod/tests/context.py'
        basename = 'context'
        self.assertEqual(categorize.path_basename(path),basename)


if __name__ == '__main__':
    unittest.main()