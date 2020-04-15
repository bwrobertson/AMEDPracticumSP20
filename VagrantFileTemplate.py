class VagrantFileTemplate():

    def createJson(self):
        data = {
            "builders": [
                {
                    "communicator": "ssh",
                    "source_path": "",
                    "provider": "virtualbox",
                    "add_force": "true",
                    "type": "vagrant",
                    "ssh_username": "vagrant",
                    "ssh_password": "vagrant",
                }
            ],
            "provisioners": [
                {
                    "type": "shell",
                    "scripts": [
                        "ecel_install.sh"
                    ],
                    "override": {
                        "vagrant": {
                            "execute_command": "echo 'packer' | sudo -S sh -c '{{ .Vars }} {{ .Path }}'"
                        }
                    }
                }
            ]
        }
        return data