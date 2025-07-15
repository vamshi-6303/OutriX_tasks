# OutriX_tasks

# 🔐 Phishing URL Detector (Tkinter GUI)

A simple yet effective *Phishing URL Detector* using Python's Tkinter for the GUI and rule-based logic for phishing detection.

## 🚀 Features

- ✅ Rule-based phishing detection
- 🌐 Open URLs in the browser
- 📋 Export scan results to CSV
- 🌗 Toggle between Light and Dark Mode
- 🧹 Clear scan logs
- 🖥 User-friendly GUI interface with keyboard shortcut support

## 📷 Screenshot


<img width="1919" height="1079" alt="1" src="https://github.com/user-attachments/assets/f6725802-5eab-48f4-85a7-cf996f8c1c72" />



after run the program its pop up the GUI like this shows in the bellow


<img width="1919" height="1079" alt="2" src="https://github.com/user-attachments/assets/dca7813b-b8bd-4fbe-9e9f-47b6c4fef765" />

## 📺 Demo Video

🎥 [Click here to watch the demo](https://drive.google.com/file/d/1egZ3Vaty1I-o5A3BolbTJYDpJ3OeOPQk/view?usp=drivesdk)

> Demonstrates the phishing detection, result export, dark mode toggle, and URL scanning features.


## 🧠 How It Works

The detector analyzes URLs using rule-based heuristics:

- Detects usage of http:// instead of https://
- Flags long URLs or those with excessive subdomains
- Checks for common phishing keywords (login, free, verify, etc.)
- Identifies suspicious patterns like hyphens in the domain

If 2 or more rules match, the URL is marked as *⚠ Phishing Detected*.

## 🛠 Technologies Used

- Python 3.x
- Tkinter (Standard Python GUI Library)
- csv and webbrowser modules

## 📂 File Structure

phishing_url_detector/ ├── phishing_detector.py     # Main application code ├── scan_result.csv          # Exported results (auto-generated) ├── README.md                # This file └── OutriX_task_1.txt        # Internship task submission


<h3 style="color:black; font-weight:bold;">🔗 LinkedIn Profile</h3>
<p><a href="https://www.linkedin.com/in/vamshi-gundoji?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" target="_blank">
https://www.linkedin.com/in/vamshi-gundoji
</a></p>


<h2 style="color:black; font-weight:bold;">💡 LEARNING OUTCOME</h2>
<hr>

<h3 style="color:black; font-weight:bold;">🧠 UNDERSTANDING PHISHING ATTACKS</h3>
<p>Learned how phishing websites trick users by disguising malicious URLs as legitimate ones.</p>

<h3 style="color:black; font-weight:bold;">🛡 RULE-BASED DETECTION ENGINE</h3>
<p>Implemented logic-based heuristics to classify URLs using pattern matching, keyword detection, and structural checks.</p>

<h3 style="color:black; font-weight:bold;">🔍 REAL-WORLD CONCEPTS APPLIED</h3>
<ul>
  <li>SSL usage</li>
  <li>WHOIS domain lookup (conceptual)</li>
  <li>URL parsing and validation</li>
</ul>

<h3 style="color:black; font-weight:bold;">🖥 GUI DEVELOPMENT WITH TKINTER</h3>
<ul>
  <li>Real-time threat detection</li>
  <li>Dark Mode toggle</li>
  <li>CSV export</li>
  <li>URL launching and result logging</li>
</ul>

<h3 style="color:black; font-weight:bold;">🚀 HANDS-ON CYBERSECURITY PRACTICE</h3>
<p>Strengthened my understanding of threat analysis, phishing indicators, and secure web behavior.</p>

<hr>

<p><strong>📁 This project was developed and submitted as Task 1 for the OutriX Virtual Internship</strong>, demonstrating:</p>
<ul>
  <li>✅ Python programming</li>
  <li>✅ GUI design and UX</li>
  <li>✅ Cybersecurity awareness</li>
  <li>✅ Real-world project building</li>
</ul>
## 🎯 How to Run

1. Make sure Python is installed.
2. Run the Python file:
```bash
python phishing_detector.py

3. Enter a URL and click "Check URL".



✅ Example URLs to Try

http://paypal.verify-account.com

https://google.com

http://free-money-login.gq


📤 Export Feature

You can export your results to a CSV file with the "Export CSV" button. It will be saved as scan_result.csv.

🌙 Dark Mode

Toggle the theme between light and dark for a better viewing experience.

🧾 Task Info

Submitted as part of the OutriX Internship (Task 1).


---

🙌 Acknowledgments

Thanks to OutriX for the opportunity to showcase this project.

📧 Contact

Vamshi Gundoji
📧 gundojivamshi13@gmail.com
📍 Telangana, India

