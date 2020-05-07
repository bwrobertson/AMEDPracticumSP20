    def pushScenario(self):


        try:
            folder = str(self.comboBox.currentText())
            if folder == '':
                msg = "Select a File type to store file."
                QMessageBox.about(self, "Select Folder", msg)
                return
        except:
            QMessage.about(self, "Select Folder", "Select a File type to store file.")
            pass
        
        data = Ui_DBConfiguration.db[folder]
        today = date.today()
        today = today.strftime("%d%b%Y")

        absolutePath = self.scenarioPath

        # try:    
        fd = open(absolutePath, 'r')
        content = fd.read()
        encoded_content = ""

        if not 'bytes' in str(type(content)): 
            encoded_content = base64.b64encode(content.encode())

        m = hashlib.sha256(encoded_content) # Hashed encoded data
        d = {}
        file_name = self.lineEdit.text()
        d['filename'] = file_name
        d['encoded_content'] = encoded_content.decode() # to recover base64.b64decode(encoded_content.encode()).decode()
        d['hash'] = m.hexdigest()

        data.insert_one(d)
        QMessage.about(self, "Select Folder", "File uploaded.")
        # except:
        #     print("ImportData.py -- pushScenario.")

        return
