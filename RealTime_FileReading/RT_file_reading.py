from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import hashlib

last_modified_time = 0
last_hash = ""

def word_count(file_path):
    count=0
    Dict = {}
    with open(file_path, "r") as file:
        for line in file:
            count += 1
            words = line.split()
            #print(words)

            for word in words:
                word = word.lower().strip(",?!@#$%^&*:;'/<>'-+=_\\").strip('."')
                Dict[word] = Dict.get(word,0) + 1
                #print(Dict)

        for key,value in Dict.items():
            print(key,"-", value)
        print("Number of lines:", count)
        print("-------------------------------------------------------------------\n")
    
class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        
        global last_modified_time, last_hash

        if not event.src_path.endswith(your_file):
            return

        #Debounce: avoid duplicate events
        current_time = time.time()
        if current_time - last_modified_time < 1:  # 1 second gap
            return
        last_modified_time = current_time

        try:
            with open(event.src_path, "r") as f:
                data = f.read()
        except:
            return  

        new_hash = hashlib.md5(data.encode()).hexdigest()   #hash works as fingerprint for file

        if new_hash == last_hash:
            return  

        last_hash = new_hash

        print("\n File updated:")
        print("\n-----------------------------------------------AFTER---------------------------------")
        word_count(event.src_path)


if __name__ == "__main__":
    your_file = input("Provide your file path or filename:")
    print("-----------------------BEFORE----------------------")
    word_count(your_file)
    path = "."  # watch current directory
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    print(f" Watching {your_file} for changes...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
