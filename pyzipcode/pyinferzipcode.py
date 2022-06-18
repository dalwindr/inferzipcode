#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import pandas as pd



__version__ = '0.1.3'
__author__ = "Tasdik Rahman"


class Pyzipcode(object):

    BASE_URL_ZIPTASTIC_API = 'http://zip.getziptastic.com/v2/{code}/{pin}'
    BASE_URL_GOOGLE_API = 'http://maps.googleapis.com/maps/api/geocode/json?address={pin}'

    @staticmethod
    def query_ziptastic_api(pincode, country_code="IN", return_json=False):
        """
        appends the pincode to the base API url and queries the API.
        country_code defaults to 'IN'

        :param pincode: The pincode 
        :param country_code: The country for the pincode. Defaults to "IN"
        :returns: returns the JSON data returned by the API
        """
        
        url = Pyzipcode.BASE_URL_ZIPTASTIC_API.format(code=country_code, pin=pincode)
        response = requests.get(url)
        if response.status_code == 200:
            json_obj = response.json()
            if return_json == True:
                return json.dumps(json_obj)
            else:
                return json_obj
        else:
            return False


    @staticmethod
    def query_google_api(pincode, return_json=False):
        """
        queries the Google maps API for getting the longitude and latitude 
        for a given pincode

        :param pincode: The pincode
        :returns: returns the latitude and longitude
        """

        url = Pyzipcode.BASE_URL_GOOGLE_API.format(pin=pincode)
        response = requests.get(url)
        if response.status_code == 200:
            json_obj = response.json()
            if json_obj["status"] == "OK":
                results = json_obj["results"][0]["geometry"]
                
                '''Storing the JSON data'''
                data = {
                    "location": results["location"],   
                    "location_type": results["location_type"],
                    "bounds": results["bounds"]
                }
                if return_json == True:
                    return json.dumps(data)
                else:
                    return data
            else:
                return False
        else:
            return False


    @staticmethod
    def get(pincode, country_code="IN",return_json=False):
        """
        Unifies the JSON data from different API's into a single one

        :param pincode: pincode for the place
        :param country_code: country code for the pincode. You can find the list of country codes in 
                             "https://github.com/tasdikrahman/pyzipcode-cli/blob/master/pyzipcode_cli/countries.json"
        :returns: A unified result of both ziptastic and google maps API
        """

        data_API_1 = Pyzipcode.query_ziptastic_api(pincode, country_code)
        data_API_2 = Pyzipcode.query_google_api(pincode)

        if data_API_2 is not False and data_API_1 is not False:
            # final_dictionary = { 
            #     "ziptastic": data_API_1,
            #     "google_maps": data_API_2
            # }
            data_API_1.update(data_API_2)   ## merges the two dictionaries
            if return_json == True:
                return json.dumps(data_API_1)
            else:
                return data_API_1
        else:
            return False

cols = ["postal_code", "country_code", "admin_name1", "admin_code1", "admin_name2", "admin_code2", "admin_name3", "admin_code3"]
colnames = {
    "country_code"      : "iso country code, 2 characters",
    "postal_code"       : "varchar(20)",
    "place_name"        : "varchar(180)",
    "admin_name1"       : "1. order subdivision (state) varchar(100)",
    "admin_code1"       : "1. order subdivision (state) varchar(20)",
    "admin_name2"       : "2. order subdivision (county/province) varchar(100)",
    "admin_code2"       : "2. order subdivision (county/province) varchar(20)",
    "admin_name3"       : "3. order subdivision (community) varchar(100)",
    "admin_code3"       : "3. order subdivision (community) varchar(20)",
    "latitude"          : "estimated latitude (wgs84)",
    "longitude"         : "estimated longitude (wgs84)",
    "accuracy"          : "accuracy of lat/lng from 1=estimated, 4=geonameid, 6=centroid of addresses or shape"
}
file1 = "/Users/dalwinder.singh/Downloads/Dalwinder_sf.csv"
file2 ="allCountries.txt"
NL_full ="NL_full.txt"
GB_full ="GB_full.txt"
CA_full ="CA_full.txt"

df1 = pd.read_csv(file2, sep="\t", names=list(colnames.keys()), header=None)[cols]
print(df1.shape, df1["country_code"].unique().shape)
df2 = pd.read_csv(NL_full, sep="\t", names=list(colnames.keys()), header=None)[cols]
df3 = pd.read_csv(GB_full, sep="\t", names=list(colnames.keys()), header=None)[cols]
df4 = pd.read_csv(CA_full, sep="\t", names=list(colnames.keys()), header=None)[cols]
df1 = df1.append(df2, ignore_index=True)
del df2
df1 = df1.append(df3, ignore_index=True)
del df3
df1 = df1.append(df4, ignore_index=True)
del df4

pd.set_option('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None)
pd.set_option('display.width', 6000)

# print(df1.columns)
print(df1.dtypes)
df1["postal_code"]=df1["postal_code"].astype("str")
df1["admin_code1"]=df1["admin_code1"].astype("str")
df1["admin_code2"]=df1["admin_code2"].astype("str")
df1["admin_code3"]=df1["admin_code3"].astype("str")

#df1.to_orc("/Users/dalwinder.singh/Downloads/world_postal.orc")
df1.to_parquet("world_postal.bsparquet", engine="pyarrow", compression="brotli")
