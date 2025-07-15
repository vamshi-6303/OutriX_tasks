import tkinter as tk
from tkinter import messagebox
import webbrowser
import csv

# === Rule-based phishing detection logic ===
def is_phishing(url):
    suspicious_keywords = ["login", "update", "free", "verify", "click", "bank", "secure", "paypal", "account"]
    score = 0
    reasons = []

    if url.startswith("http://"):
        score += 1
        reasons.append("Uses insecure HTTP")

    if "-" in url:
        score += 1
        reasons.append("Contains '-' in domain")

    if url.count(".") > 3:
        score += 1
        reasons.append("Too many subdomains")

    if any(keyword in url.lower() for keyword in suspicious_keywords):
        score += 1
        reasons.append("Suspicious keyword in URL")

    if len(url) > 75:
        score += 1
        reasons.append("Very long URL")

    return score >= 2, reasons


# === URL Checking Function ===
def check_url():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL to check.")
        return

    is_phish, reasons = is_phishing(url)

    result_label.config(fg="red" if is_phish else "green")
    result_label.config(text=f"{'⚠ Phishing Detected!' if is_phish else '✅ URL is likely safe.'}")

    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)

    output_text.insert(tk.END, f"🔍 Scanned URL: {url}\n")
    output_text.insert(tk.END, f"🔎 Verdict: {'Phishing' if is_phish else 'Safe'}\n\n")
    if reasons:
        output_text.insert(tk.END, "📌 Reasons:\n" + "\n".join(f"• {r}" for r in reasons))
    else:
        output_text.insert(tk.END, "✅ No suspicious patterns detected.")
    output_text.config(state="disabled")


# === Other Functionalities ===
def clear_log():
    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.config(state="disabled")
    result_label.config(text="")

def open_url():
    url = url_entry.get().strip()
    if url.startswith("http://") or url.startswith("https://"):
        webbrowser.open(url)
    else:
        messagebox.showerror("Invalid URL", "Please enter a valid URL (http or https).")

def export_csv():
    data = output_text.get("1.0", tk.END).strip()
    if not data:
        messagebox.showinfo("No Data", "There is no data to export.")
        return
    with open("scan_result.csv", "w", newline="") as f:
        writer = csv.writer(f)
        for line in data.split("\n"):
            writer.writerow([line])
    messagebox.showinfo("Exported", "Scan results saved to scan_result.csv")

def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        root.config(bg="#222")
        top_frame.config(bg="#222")
        main_frame.config(bg="#333")
        bottom_frame.config(bg="#222")
        result_label.config(bg="#333", fg="white")
        output_text.config(bg="#111", fg="white", insertbackground="white")
        title_label.config(bg="#222", fg="cyan")
    else:
        root.config(bg="#cce6ff")
        top_frame.config(bg="#cce6ff")
        main_frame.config(bg="#e6f0ff")
        bottom_frame.config(bg="#cce6ff")
        result_label.config(bg="#e6f0ff", fg="black")
        output_text.config(bg="white", fg="black", insertbackground="black")
        title_label.config(bg="#005ab4", fg="white")

# === UI Setup ===
root = tk.Tk()
root.title("Phishing URL Detector (AI + VirusTotal + History)")
root.geometry("800x500")
root.resizable(True, True)
root.config(bg="#cce6ff")

dark_mode = False

# === Title ===
title_label = tk.Label(root, text="Phishing URL Detector", font=("Arial", 20, "bold"), bg="#005ab4", fg="white", pady=10)
title_label.pack(fill=tk.X)

# === Top Frame ===
top_frame = tk.Frame(root, bg="#cce6ff")
top_frame.pack(pady=10)

url_label = tk.Label(top_frame, text="Enter URL:", font=("Arial", 12), bg="#cce6ff")
url_label.pack(side=tk.LEFT, padx=5)

url_entry = tk.Entry(top_frame, font=("Arial", 12), width=50)
url_entry.pack(side=tk.LEFT, padx=5)

check_button = tk.Button(top_frame, text="Check URL", font=("Arial", 12, "bold"), bg="#3399ff", fg="white", command=check_url)
check_button.pack(side=tk.LEFT, padx=5)

# === Main Frame ===
main_frame = tk.Frame(root, bg="#e6f0ff", bd=2, relief=tk.GROOVE)
main_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

result_label = tk.Label(main_frame, text="", font=("Arial", 12, "italic"), bg="#e6f0ff")
result_label.pack(pady=10)

output_text = tk.Text(main_frame, height=5, font=("Arial", 12), wrap=tk.WORD, state="disabled")
output_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=False)

# === Bottom Button Frame ===
bottom_frame = tk.Frame(root, bg="#cce6ff")
bottom_frame.pack(pady=10)

btn_width = 15
btn_height = 2
btn_font = ("Arial", 10, "bold")

clear_btn = tk.Button(bottom_frame, text="Clear Chat/Log", width=btn_width, height=btn_height, font=btn_font, bg="#dddddd", command=clear_log)
clear_btn.grid(row=0, column=0, padx=10, pady=10)

open_btn = tk.Button(bottom_frame, text="Open URL", width=btn_width, height=btn_height, font=btn_font, bg="#87cefa", command=open_url)
open_btn.grid(row=0, column=1, padx=10, pady=10)

export_btn = tk.Button(bottom_frame, text="Export CSV", width=btn_width, height=btn_height, font=btn_font, bg="#b6fcb6", command=export_csv)
export_btn.grid(row=0, column=2, padx=10, pady=10)

dark_btn = tk.Button(bottom_frame, text="Dark Mode", width=btn_width, height=btn_height, font=btn_font, bg="#333333", fg="white", command=toggle_dark_mode)
dark_btn.grid(row=0, column=3, padx=10, pady=10)

# === Bind Enter Key to Trigger Scan ===
root.bind("<Return>", lambda event: check_url())

root.mainloop()