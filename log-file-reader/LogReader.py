import time
from datetime import datetime

file_path = "sample_log_unsorted.txt"

start_input = input("Enter start date (YYYY-MM-DD): ")
end_input = input("Enter end date (YYYY-MM-DD): ")

start = time.perf_counter()

start_date = datetime.strptime(start_input, "%Y-%m-%d")
end_date = datetime.strptime(end_input, "%Y-%m-%d")

IP_count = {}

try:
    with open(file_path, "r") as f:
        for line in f:
            line_date_str = line.split(" ")[0]
            line_date = datetime.strptime(line_date_str, "%Y-%m-%d")
            if start_date <= line_date <= end_date:
                IP = line.split(" ")[4]  
                if IP in IP_count:
                    IP_count[IP] += 1
                else:
                    IP_count[IP] = IP_count.get(IP, 0) + 1
        
        if not IP_count:      
            print("Invalid format or no data found..")
    
    for key,value in IP_count.items():
        print(f"IP: {key}: {value}")

except Exception as e:
    print(e)
            
end = time.perf_counter()
print("Time taken:", end - start, "seconds")
