import os
import time

your_file = input("Provide your file path or filename:")

start = time.perf_counter()

if os.path.exists(your_file):
    print("File exists!!")
    print("-----------------Counting word occurence----------------")
    
    try:
        count = 0
        Dict = {}
        with open(your_file, "r") as file:
            for line in file:
                count += 1
                words = line.split()
                #print(words)
                word_only = ""

                for word in words:
                    word = word.lower().strip(",?!@#$%^&*:;'/<>.""-+=_\\")
                    if word.isalpha():
                        Dict[word] = Dict.get(word,0) + 1
                    else:
                        clean = ""
                        for ch in word:
                            if ch.isalpha() or ch == "-":   
                                clean += ch
                            else:
                                clean += " "                 

                        word = clean.split()  

                        for word in word:   
                            Dict[word] = Dict.get(word, 0) + 1

            for key,value in Dict.items():
                print(key,"-", value)
            print("Number of lines:", count)
                       
                    
    except UnicodeDecodeError:
        print("Could not decode file.")

else:
    print("File not found!")

end = time.perf_counter()
print("Time taken:", end - start, "seconds")
    
