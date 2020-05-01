#!/usr/bin/env/ python
# encoding: utf-8

import requests


class Character:

    PROFILE_BASE_URL = "https://us.api.blizzard.com/profile/wow/character/"

    def __init__(self, name, realm):
        self.name = name
        self.realm = realm
        
        #replaces whitespace and apostrophe characters for the URL
        self.realm_slug = self.realm.lower().replace(" ", "-").replace("'", "")
        
        #retrive JSON data from Blizzard API
        self.data = "This character hasn't been updated yet. Run <name>.getData(<token>) to update."
        
        #parse useful data from JSON


    def getData(self, token):
        url = "https://us.api.blizzard.com/profile/wow/character/" + self.realm_slug + "/" + self.name.lower() + "?namespace=profile-us&locale=en_US&access_token=" + token
        data = requests.get(url)
        if data.ok:
            self.data = data.json()
            self.race = self.data['race']['name']
            self.level = self.data['level']
            self.item_level = self.data['average_item_level']
            self.char_class = self.data['character_class']['name']
            self.spec = self.data['active_spec']['name']
        else:
            print("Encountered a problem. Reason: " + data.reason)
        
    def pretty_summary(self):
        """Prints a summary of the relevant character info"""
        return "{}, level {} {} {} ({}, ilvl = {}), on {}".format(self.name, self.level, self.race, self.char_class, self.spec, self.item_level, self.realm)