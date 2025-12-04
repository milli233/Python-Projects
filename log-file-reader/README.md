# Log File Parser

A simple Python-based utility that reads an unsorted log file, filters the entries based on a given date range, and counts occurrences of each IP address.

This project helps understand:

* File handling
* Date parsing using `datetime`
* Basic log analysis
* Dictionary-based frequency counting
* Exception handling
* Measuring execution time

---

## 🚀 Features

* Filter log entries between **start date** and **end date**.
* Count how many times each **IP address** appears.
* Handle invalid formats gracefully.
* Display execution time for performance insight.

---

## 📂 Log Format Example

Each log entry should start with a date in the format:

```
YYYY-MM-DD ... ... ... IP
```

Example:

```
2024-01-15 INFO User login success 192.168.1.10
2024-01-17 ERROR Timeout 10.0.0.5
2024-02-01 INFO Logout 192.168.1.10
```

---

## 🧪 Sample Input

```
Enter start date (YYYY-MM-DD): 2024-01-10
Enter end date (YYYY-MM-DD): 2024-01-31
```

### Output Example:

```
IP: 192.168.1.10: 1
IP: 10.0.0.5: 1
Time taken: 0.0032 seconds
```

---

## 📜 How to Run

### Prerequisites

* Python 3.8+

### Steps

```
python main.py
```

Enter required date ranges when prompted.

---

## 🗂 File Structure

```
log-file-parser/
│── main.py
│── sample_log_unsorted.txt
│── README.md
```

---

## ⚠️ Notes

* Ensure your log file contains valid date format `YYYY-MM-DD` at the start of each line.
* Replace `sample_log_unsorted.txt` with your actual log file if needed.

---

## 💡 Future Enhancements

* Export IP counts to CSV.
* Add support for different log formats.
* Add CLI arguments instead of interactive input.

---

## 📄 License

MIT License

---

## 👨‍💻 Author

Created by **Milli Srivastava** 

Feel free to contribute or suggest improvements!
