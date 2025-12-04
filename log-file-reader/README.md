# 📄 Log File Reader (Python)

This project reads a log file and prints **unique IP addresses with their occurrence count** from a **given date or date range**.  
Just enter the start and end date — the program filters the log file and shows all matching IPs.

---

## 🚀 Features

- Search by **single date** or **date range**
- Extract IP addresses from matching lines
- Count occurrences of each IP
- Display unique IPs only
- Handles:
  - Missing file
  - Wrong date format
  - No data found

---

## 📁 Project Structure

LogReader.py
sample_log_unsorted.txt
README.md

yaml
Copy code

---

## 📝 How It Works

1. User enters:
Enter start date (YYYY-MM-DD):
Enter end date (YYYY-MM-DD):

markdown
Copy code
2. The script opens the log file line-by-line  
3. For each log line:
- Extracts **date**  
- Checks if date is within range  
- Extracts the **IP address**  
4. Maintains a dictionary of IP counts  
5. Finally prints:

IP: 192.168.0.1: 3
IP: 103.22.123.11: 1

yaml
Copy code

---

## 📌 Log File Format (Expected)

Each line must begin with a date in this format:

YYYY-MM-DD HH:MM:SS METHOD IP OTHER_DATA

javascript
Copy code

Example from `sample_log_unsorted.txt`:

2024-01-02 11:45:33 GET /home 192.168.0.1
2024-01-03 10:12:20 POST /login 103.22.123.11

markdown
Copy code

Your script extracts:

- **Date** → first word  
- **IP** → 5th element in the line (`line.split(" ")[4]`)

---

## ▶️ How to Run

Run the script with:

```bash
python LogReader.py
Make sure the log file name matches:

python
Copy code
file_path = "sample_log_unsorted.txt"
📤 Example Output
sql
Copy code
Enter start date (YYYY-MM-DD): 2024-01-02
Enter end date (YYYY-MM-DD): 2024-01-03

IP: 192.168.0.1: 2
IP: 103.22.123.11: 1

Time taken: 0.00097 seconds
⚠️ Error Handling
❌ Wrong date format →
"time data 'abc' does not match format '%Y-%m-%d'"

❌ Invalid or no data found →
"Invalid format or no data found.."

❌ Wrong file path →
"Log file not found"

📦 Requirements
Python 3.x

No external libraries needed

✨ Future Improvements
Range search via command-line flags (--start, --end)

Export output to CSV

Add IP blacklist filtering

Add colored terminal output

🤝 Contributing
Pull requests are welcome.
If you want to add features or fix bugs, feel free to open an issue.

yaml
Copy code
