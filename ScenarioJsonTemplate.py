class ScenarioJsonTemplate():

    def createJson(self):
        data = {
            "name": "",
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