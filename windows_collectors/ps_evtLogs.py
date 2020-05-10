import subprocess
import sys
import os

path1 = os.getcwd()

def get_eventlogs(logType='System', duration=24):
    subprocess.Popen(["powershell.exe", "Get-EventLog {} -After (Get-Date).AddHours(-{})".format(logType, duration), "|", "ConvertTo-HTML", "|", "Out-File", f"{path1}\\data\\{logType}_Event_Logs.htm"])
    print("Done")
