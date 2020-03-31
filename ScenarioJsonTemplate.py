class ScenarioJsonTemplate():

    def createJson(self):
        data = {
            "name": "",
            "id": 1,
            "date_created": "",
            "date_modified": "",
            "exploit": {
                "file": ""
            },
            "pov": {
                "file": ""
            },
            "machines": {}
        }
        
        return data