#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyzipcode import Pyzipcode as pz
import unittest
import os

class TestModule(unittest.TestCase):
    """Checks for the sanity of all module methods"""

    def test_get_invalid_pincode(self):
        print("test", os.getcwd())
        current_result = pz.get([33044])


        print(current_result)
       #self.assertFalse(current_result)


if __name__ == "__main__":
    unittest.main()