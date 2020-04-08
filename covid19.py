# -*- coding: utf-8 -*-

# Copyright (C) 2020 Botir Ziyatov <botirziyatov@gmail.com>
# This program is free software: you can redistribute it and/or modify

from typing import Dict, List
import requests

class Covid19(object):
    url = ""

    def __init__(self, url="https://covid.delalify.com/api"):
        self.url = url

    def _request(self, endpoint, params=None):
        if params is None:
            params = {}
        response = requests.get(self.url + endpoint, {**params})
        response.raise_for_status()
        if response:
            return response.json()['response']
        else:
            return False

    def getLatest(self) -> List[Dict[str, int]]:
        """
        :return: The latest amount of total confirmed cases, deaths, and recoveries.
        """
        data = self._request("/latest")
        return data


    def getByCountryCode(self, country_code) -> List[Dict]:
        """
        :param country_code: String denoting the ISO 3166-1 alpha-2 code (https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the country
        :return: A list of areas that correspond to the country_code. If the country_code is invalid, it returns an empty list.
        """
        data = self._request("/countries", {"country_code": country_code})
        return data
