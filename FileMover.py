from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

import os 
import json
import time 

class Myhandler(FileSystemEventHandler):
    def on_modified(self,event):
        for filename in os.listdir(foldertracker):
            src=foldertracker + "/" + filename
            new_folder=folderdest + "/" + filename
            os.rename(src,new_folder)

foldertracker="/Users/slavaborodin/Desktop/TestFolder"
folderdest="/Users/slavaborodin/Desktop/DestinationFolder"
event_handler = Myhandler()
observer=Observer()
observer.schedule(event_handler,foldertracker,recursive=True)

observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

