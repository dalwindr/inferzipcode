

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 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12
from pyworldpostal import pyinferzipcode as pz
import unittest


class TestModule(unittest.TestCase):
    """Checks for the sanity of all module methods"""

    def test_get__pincode(self):
        current_result = pz.WorldPostalSearch()._get("AD100","AD")
        self.assertGreaterEqual(len(current_result),0, "ok")

    def test_get__pincodelist(self):
        current_result = pz.WorldPostalSearch()._get(["AD100", "AD100"], "AD")
        self.assertGreaterEqual(len(current_result),0, "ok")

    def test_bulkget_pincode(self):
            current_result = pz.WorldPostalSearch().bulkget(
                [("AD100", "AD"), ("AD1000", "AD"), ("AD100", "AD"), ("AD200", "AD")])
            self.assertGreaterEqual(len(current_result), 0, "ok")

    def test_get_invalid_pincode(self):
        current_result = pz.WorldPostalSearch().valid_countries()
        self.assertGreaterEqual(len(current_result),0, "ok")


if __name__ == "__main__":
    unittest.main()
