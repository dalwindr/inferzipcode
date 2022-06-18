#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import os
import requests
__version__ = '0.1.0'
__author__ = "Dalwinder singh"


class Pyzipcode(object):
    @staticmethod
    def get(pincode: list, country_code=None, return_json=False):
        r = requests.get('https://raw.github.com/kennethreitz/requests/master/README.rst')

        # print("code", os.getcwd())
        # df = pd.read_csv("../pyzipecode/world_postal.zcsv", compression="zip")
        return df[pincode].to_dict("record")
