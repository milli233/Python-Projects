# File Watcher and Word Counter

This Python script monitors a specified text file for changes and prints a **word frequency count** along with the number of lines whenever the file is modified. It uses the `watchdog` library to detect changes in real-time.

---

## Features

* Monitors a file in the current directory for updates.
* Counts the occurrence of each word in the file (case-insensitive).
* Ignores punctuation like `, . ? ! @ # $ % ^ & * : ; ' "`.
* Prints the number of lines in the file.
* Debounces duplicate events and avoids repeated processing.

---

## Requirements

* Python 3.x
* `watchdog` library

Install `watchdog` using pip:

```bash
pip install watchdog
```

---

## Usage

1. Run the script:

```bash
python your_script_name.py
```

2. Enter the file path or filename you want to monitor.

3. The script will show the **initial word count** (`BEFORE`) and then print updates whenever the file changes (`AFTER`).

---

## Example

```
Provide your file path or filename: sample.txt
-----------------------BEFORE----------------------
hello - 3
world - 2
Number of lines: 5
Watching sample.txt for changes...
```

---

## Notes

* Only monitors files in the current directory.
* Updates are detected using file modification time and a hash check to avoid duplicate triggers.

---

## License

This project is open-source and free to use.
