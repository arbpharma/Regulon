from IPython.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))
import pandas as pd
import numpy as np
import requests
import json

class WikidataClient:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.wikidata_api_url = "https://www.wikidata.org/w/api.php"
        self.session = requests.Session()
        self.login_token = self.authenticate()
        self.edit_token = self.get_edit_token()

    def transform_json(self, jsonn):
        jsonn_str = str(jsonn)
        return jsonn_str.replace("'", "\"")

    def authenticate(self):
        login_token_response = self.session.get(
            self.wikidata_api_url,
            params={
                "action": "query",
                "meta": "tokens",
                "type": "login",
                "format": "json",
            },
        )
        login_token = login_token_response.json()["query"]["tokens"]["logintoken"]
        return login_token

    def get_session_token(self):
        login_response = self.session.post(
            self.wikidata_api_url,
            data={
                "action": "login",
                "lgname": self.username,
                "lgpassword": self.password,
                "lgtoken": self.login_token,
                "format": "json",
            },
        )
        assert login_response.json()["login"]["result"] == "Success"

    def get_edit_token(self):
        edit_token_response = self.session.get(
            self.wikidata_api_url,
            params={
                "action": "query",
                "meta": "tokens",
                "format": "json",
            },
        )
        edit_token = edit_token_response.json()["query"]["tokens"]["csrftoken"]
        return edit_token

    def create_new_item(self, language, label, description):
        new_item_data = {
            "labels": {language: {"language" : language, "value" : label}},
            "descriptions": {language: {"language" : language, "value" : description}},
        }
        create_item_response = self.session.post(
            self.wikidata_api_url,
            data={
                "action": "wbeditentity",
                "format": "json",
                "new": "item",
                "token": self.edit_token,
                "data": self.transform_json(new_item_data),
                "formatversion": "2"
            },
        )
        created_item_id = create_item_response.json().get("entity", {}).get("id")
        return created_item_id
    
    def create_new_property(self, language, label, description):
        new_item_data = {
            "labels": {language: {"language" : language, "value" : label}},
            "descriptions": {language: {"language" : language, "value" : description}},
        }
        create_item_response = self.session.post(
            self.wikidata_api_url,
            data={
                "action": "wbeditentity",
                "format": "json",
                "new": "property",
                "token": self.edit_token,
                "data": self.transform_json(new_item_data),
                "formatversion": "2"
            },
        )
        created_item_id = create_item_response.json().get("entity", {}).get("id")
        if created_item_id == None:
            return create_item_response.json()
        return created_item_id

    def get_entity_by_id(self, ID, language):
        get_entity_response = self.session.get(
            self.wikidata_api_url,
            params={
                "action": "wbgetentities",
                "format": "json",
                "ids": ID,
                "languages": language,
                "formatversion": "2"
            },
        )
        return get_entity_response.json()
