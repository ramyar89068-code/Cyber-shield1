import random
import traceback
import json
import os
import sys
import smtplib
import requests
import base64
import time
import socket
import whois
from tkinter import *
from datetime import datetime
from email.message import EmailMessage
from urllib.parse import quote
from tkinterweb import HtmlFrame
import sqlite3
import customtkinter as ctk
from PIL import Image
from tkinter import messagebox
import tkinter as tk
from email.mime.text import MIMEText
from reportlab.pdfgen import canvas
from tkinter import filedialog
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet




ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("")

    return os.path.join(base_path, relative_path)

def save_blocked_sites():

    global current_user_email

    filename = f"{current_user_email}_blocked.json"

    with open(filename, "w") as file:

        json.dump(
            auto_blocked_sites,
            file,
            indent=4
        )

def load_data():

    global total_scans
    global threats_found

    total_scans = len(scan_history)

    threats_found = sum(
        1
        for scan in scan_history
        if scan.get("status") in ["Malicious", "Suspicious"]
    )




def load_blocked_sites():

    global auto_blocked_sites
    global current_user_email

    filename = f"{current_user_email}_blocked.json"

    auto_blocked_sites = []

    if os.path.exists(filename):

        with open(filename, "r") as file:

            auto_blocked_sites = json.load(file)
    print("Blocked loaded:", len(auto_blocked_sites))
    print(auto_blocked_sites)

app = ctk.CTk()
conn = sqlite3.connect("cybershield.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE,
    password TEXT
)
""")

conn.commit()
SENDER_EMAIL = "pranathiraojupalli@gmail.com"
APP_PASSWORD = "igds ewcy ilki ttna"

generated_otp = ""
otp_verified = False
auto_blocked_sites = []
scan_history = []
total_scans = 0
threats_found = 0
manual_blocked_sites = []
last_scan = None
DATA_FILE = "cybershield_data.json"
VT_API_KEY = "2596ec5def9572621758d09d88bebc63c03bbbfbda9cc610612fa5902470f298"
current_user_email = ""
load_data()


logo_image = ctk.CTkImage(
    light_image=Image.open(resource_path("logo3.jpeg")),
    dark_image=Image.open(resource_path("logo3.jpeg")),
    size=(300,150)
)


app.title("Cyber Shield")
app.geometry("1100x900")



        
         
def show_team():

    project_window = ctk.CTkToplevel(app)
    project_window.title("Project Information")
    project_window.geometry("800x600")
    project_window.lift()
    project_window.focus_force()
    project_window.attributes("-topmost", True)

    # Optional: remove topmost after opening
    project_window.after(
        500,
        lambda: project_window.attributes(
            "-topmost",
            False
        )
    )

    html_content = """
    <html>
    <head>
        <title>Project Information</title>

        <style>

            body{
                font-family: Arial;
                margin: 20px;
            }

            h1{
                color: #0066cc;
            }

            h2{
                color: #333333;
            }

            table{
                border-collapse: collapse;
                width: 100%;
                margin-bottom: 20px;
            }

            th, td{
                border: 1px solid #cccccc;
                padding: 8px;
                text-align: left;
            }

            th{
                background-color: #e6e6e6;
            }

        </style>
    </head>

    <body>

    <h1>Cyber Shield - Project Information</h1>

    <p>
    This project was developed by <b>ProTech Defenders</b>
    as part of a Cyber Security Internship.
    The project helps identify malicious websites,
    phishing attacks, suspicious URLs and cyber threats.
    </p>

    <h2>Project Details</h2>

    <table>

        <tr>
            <th>Project Details</th>
            <th>Value</th>
        </tr>

        <tr>
            <td>Project Name</td>
            <td>Cyber Shield(Malicious website Blocker)</td>
        </tr>

        <tr>
            <td>Project Description</td>
            <td>Website Security Scanner and Threat Detection System</td>
        </tr>
        <tr>
            <td>Project start date</td>
            <td>4-06-2026</td>
        </tr>
        <tr>
            <td>Project end date</td>
            <td>21-06-2026</td>
        </tr>



        <tr>
            <td>Project Status</td>
            <td>Completed</td>
        </tr>

        <tr>
            <td>Version</td>
            <td>1.0</td>
        </tr>

    </table>

    <h2>Developer Details</h2>

    <table>

        <tr>
            <th>Name</th>
            <th>Employee ID</th>
            <th>Email</th>
        </tr>

        <tr>
            <td>Pranathi Jupalli</td>
            <td>ST#IS#9254</td>
            <td>pranathiraojupalli@gmail.com</td>

        </tr>
        
        <tr>
            <td>Ramya Chikkanti</td>
            <td>ST#IS#9261</td>
            <td>ramyar89068@gmail.com</td>

        </tr>
        <tr>
            <td>vennala chatla</td>
            <td>ST#IS#9248</td>
            <td>chatla.vennala123@gmail.com</td>

        </tr>
        <tr>
            <td>Manasa Thallapalli</td>
            <td>ST#IS#9241</td>
            <td>tallapallimanasa26@gmail.com</td>

        </tr>
        <tr>
            <td>I sowmya</td>
            <td>ST#IS#9244</td>
            <td>isowmya1823@gmail.com</td>

        </tr>

    </table>

    
   
    <h2>Project Features</h2>

    <table>

        <tr>
            <th>Features</th>
        </tr>

        <tr><td>Quick Scan</td></tr>
        <tr><td>Deep Scan</td></tr>
        <tr><td>VirusTotal Integration</td></tr>
        <tr><td>WHOIS Lookup</td></tr>
        <tr><td>Scan History</td></tr>
        <tr><td>PDF Report Export</td></tr>
        <tr><td>Website Blocking</td></tr>
        <tr><td>Dashboard Statistics</td></tr>

    </table>

    <h2>Company Details</h2>

    <table>

        <tr>
            <th>Field</th>
            <th>Value</th>
        </tr>

        <tr>
            <td>Company Name</td>
            <td>Supraja Technologies</td>
        </tr>

        <tr>
            <td>Email</td>
            <td>contact@suprajatechnologies.com</td>
        </tr>
         <tr>
            <td>Team Name</td>
            <td>Pro Tech Defenders</td>
        </tr>


        <tr>
            <td>Version</td>
            <td>1.0</td>
        </tr>

    </table>

    </body>
    </html>
    """

    html_frame = HtmlFrame(
        project_window,
        horizontal_scrollbar="auto"
    )

    html_frame.pack(
        fill="both",
        expand=True
    )

    html_frame.load_html(
        html_content
    )
   
def show_frame(frame):
    
    login_frame.pack_forget()
    dashboard_frame.pack_forget()
    history_frame.pack_forget()
    scanner_frame.pack_forget()
    blocked_frame.pack_forget()
    settings_frame.pack_forget()

    frame.pack(fill="both", expand=True)
    
def open_register():

    home_frame.pack_forget()
    register_frame.pack(fill="both", expand=True)


def back_home():

    register_frame.pack_forget()
    home_frame.pack(fill="both", expand=True)

# ---------------- SEND OTP FUNCTION ----------------
def send_otp():

    global generated_otp

    receiver_email = email_entry.get().strip()

    if receiver_email == "":

        messagebox.showerror(
            "Error",
            "Enter Email First"
        )
        return

    generated_otp = str(
        random.randint(
            100000,
            999999
        )
    )

    print("Generated OTP =", generated_otp)

    try:

        msg = EmailMessage()

        msg["Subject"] = "Cyber Shield OTP"

        msg["From"] = SENDER_EMAIL

        msg["To"] = receiver_email

        msg.set_content(
            f"Your OTP is: {generated_otp}"
        )

        with smtplib.SMTP(
            "smtp.gmail.com",
            587
        ) as server:

            server.starttls()

            server.login(
                SENDER_EMAIL,
                APP_PASSWORD
            )

            server.send_message(msg)

        messagebox.showinfo(
            "Success",
            "OTP Sent Successfully"
        )

    except Exception as e:

        messagebox.showerror(
            "Email Error",
            str(e)
        )


def verify_otp():

    print("Verify OTP Clicked")

    global otp_verified
    global generated_otp

    entered_otp = otp_entry.get().strip()

    print("Entered OTP =", entered_otp)
    print("Generated OTP =", generated_otp)

    if entered_otp == generated_otp:

        otp_verified = True

        messagebox.showinfo(
            "Success",
            "OTP Verified Successfully"
        )

    else:

        otp_verified = False

        messagebox.showerror(
            "Error",
            "Invalid OTP"
        )

def toggle_password():

    if password_entry.cget("show") == "*":

        password_entry.configure(show="")

        eye_btn.configure(text="🙈")

    else:

        password_entry.configure(show="*")

        eye_btn.configure(text="👁")
     
def register_user():

    global otp_verified

    if not otp_verified:

        messagebox.showerror(
            "Error",
            "Verify OTP First"
        )
        return

    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if email == "" or password == "":

        messagebox.showerror(
            "Error",
            "Fill All Fields"
        )
        return

    try:

        cursor.execute(
            "INSERT INTO users(email, password) VALUES(?, ?)",
            (email, password)
        )

        conn.commit()

        messagebox.showinfo(
            "Success",
            "Registration Successful"
        )

        otp_verified = False

        email_entry.delete(0, "end")
        otp_entry.delete(0, "end")
        password_entry.delete(0, "end")

    except sqlite3.IntegrityError:

        messagebox.showerror(
            "Error",
            "Email Already Registered"
        )


def export_selected_scan(scan):
    print("Export function started")

    if scan is None:

        messagebox.showerror(
            "Error",
            "No scan selected."
        )
        return

    from tkinter import filedialog

    file_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[
            ("PDF Files", "*.pdf")
        ]
    )

    if not file_path:
        return

    from reportlab.platypus import (
        SimpleDocTemplate,
        Paragraph,
        Spacer
    )

    from reportlab.lib.styles import getSampleStyleSheet

    pdf = SimpleDocTemplate(file_path)

    styles = getSampleStyleSheet()

    content = []

    text = f"""
    <b>Website:</b> {scan.get('website','N/A')}<br/>
    <b>IP Address:</b> {scan.get('ip','N/A')}<br/>
    <b>Registrar:</b> {scan.get('registrar','N/A')}<br/>
    <b>Status:</b> {scan.get('status','N/A')}<br/>
    <b>Malicious:</b> {scan.get('malicious',0)}<br/>
    <b>Suspicious:</b> {scan.get('suspicious',0)}<br/>
    <b>Harmless:</b> {scan.get('harmless',0)}<br/>
    <b>Undetected:</b> {scan.get('undetected',0)}<br/>
    <b>Creation Date:</b> {scan.get('creation_date','N/A')}<br/>
    <b>Expiration Date:</b> {scan.get('expiration_date','N/A')}<br/>
    <b>Scan Time:</b> {scan.get('scan_time','N/A')}
    """

    content.append(
        Paragraph(text, styles["BodyText"])
    )

    content.append(
        Spacer(1, 20)
    )

    pdf.build(content)

    messagebox.showinfo(
        "Success",
        f"Report Saved:\n{file_path}"
    )
def open_login():

    home_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)


def back_home_login():

    login_frame.pack_forget()
    home_frame.pack(fill="both", expand=True)


def login_user():
    global current_user_email
    email = login_email.get().strip()
    password = login_password.get().strip()

    cursor.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (
            email,
            password
        )
    )

    user = cursor.fetchone()

    if user:

        current_user_email = email

        load_scan_history()

        load_data()

        load_blocked_sites()
        
        update_dashboard_stats()

        open_dashboard()
    else:

        messagebox.showerror(
            "Error",
            "Invalid Email or Password"
        )



def update_dashboard_stats():

    stats_label.configure(
        text=f"📊 Scans: {total_scans} | 🚫 Blocked: {len(auto_blocked_sites)} | ☠ Threats: {threats_found}"
    )
def open_dashboard():
    update_dashboard_stats()

    login_frame.pack_forget()

    user_label.configure(
        text=f"👤 User: {current_user_email}"
    )

    dashboard_frame.pack(
        fill="both",
        expand=True
    )
def logout():

    dashboard_frame.pack_forget()

    home_frame.pack(
        fill="both",
        expand=True
    )
def open_blocked_sites():

    dashboard_frame.pack_forget()

    sites_listbox.delete(
        0,
        "end"
    )
    print("Showing blocked sites:", auto_blocked_sites)

    for site in auto_blocked_sites:

        sites_listbox.insert(
            "end",
            site
        )

    blocked_frame.pack(
        fill="both",
        expand=True
    )




def quick_scan():
    global total_scans
    global threats_found


    website = quick_scan_entry.get().strip().lower()

    if website == "":
        messagebox.showerror(
            "Error",
            "Enter Website URL"
        )
        return

    suspicious_keywords = [
        "free-money",
        "hack",
        "crack",
        "phishing",
        "malware",
        "virus",
        "fake-login"
    ]

    if website in auto_blocked_sites:

        status = "Blocked"

        quick_result_label.configure(
            text="🚫 BLOCKED WEBSITE"
        )

    elif any(
        keyword in website
        for keyword in suspicious_keywords
    ):

        status = "Suspicious"

        quick_result_label.configure(
            text="⚠️ SUSPICIOUS WEBSITE"
        )

    else:

        status = "Safe"

        quick_result_label.configure(
            text="✅ APPEARS SAFE"
        )

    history_entry = {

        "website": website,

        "status": status,

        "scan_time":
        datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )
    }

    scan_history.append(
        history_entry
    )
    load_data()
    update_dashboard_stats()
    history_box.insert(
        "end",
        f"{website} | {status}\n"
    )
    total_scans += 1
    update_security_score()

    update_dashboard_stats()

    save_scan_history()

    save_data()
  

def save_scan_history():

    global current_user_email
    global scan_history

    if not current_user_email:
        print("No user logged in")
        return

    filename = f"{current_user_email}_history.json"

    print("Saving file:", filename)
    print("Current folder:", os.getcwd())

    with open(filename, "w") as file:

        json.dump(
            scan_history,
            file,
            indent=4
        )



def open_quick_scan():

    dashboard_frame.pack_forget()

    quick_scan_frame.pack(
        fill="both",
        expand=True
    )

def open_scanner():

    dashboard_frame.pack_forget()

    scanner_frame.pack(
        fill="both",
        expand=True
    )

def update_security_score():

    global security_score

    security_score = 100

    security_score -= (
        threats_found * 5
    )

    security_score -= (
        len(auto_blocked_sites) * 2
    )

    if security_score < 0:

        security_score = 0

    security_score_label.configure(
        text=f"🛡 Security Score: {security_score}"
    )
def back_to_dashboard_from_scanner():

    scanner_frame.pack_forget()

    dashboard_frame.pack(
        fill="both",
        expand=True
    )

def back_to_dashboard():

    blocked_frame.pack_forget()

    dashboard_frame.pack(
        fill="both",
        expand=True
    )


def add_website():

    website = website_entry.get().strip().lower()

    if website == "":

        messagebox.showerror(
            "Error",
            "Enter Website Name"
        )
        return

    for i in range(sites_listbox.size()):

        if sites_listbox.get(i).lower() == website:

            messagebox.showerror(
                "Duplicate",
                "Website Already Exists"
            )
            return

    sites_listbox.insert(
        "end",
        website
    )

    website_entry.delete(
        0,
        "end"
    )

    update_stats()




def remove_website():
    selected = sites_listbox.curselection()

    if not selected:

        messagebox.showwarning(
            "Warning",
            "Please Select A Website"
        )
        return

    website = sites_listbox.get(
        selected[0]
    ).lower()

    if website in auto_blocked_sites and website not in manual_blocked_sites:
        confirm = messagebox.askyesno(
            "Security Warning",
            f"{website} was automatically blocked by Cyber Shield.\n\nRemoving it may expose your system to threats.\n\nDo you want to continue?"
        )

        if not confirm:
            return

        auto_blocked_sites.remove(
            website
        )

    elif website in manual_blocked_sites:

        manual_blocked_sites.remove(
            website
        )

    sites_listbox.delete(
        selected[0]
    )

    remove_realtime_block(
        website
    )

    save_blocked_sites()

    update_stats()
    print("Manual:", manual_blocked_sites)
    print("Auto:", auto_blocked_sites)

def remove_realtime_block(site):

    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

    with open(hosts_path, "r") as file:
        lines = file.readlines()

    with open(hosts_path, "w") as file:

        for line in lines:

            if site not in line and f"www.{site}" not in line:
                file.write(line)




def search_website():

    website = website_entry.get().strip().lower()

    if website == "":
        return

    found = False

    for i in range(sites_listbox.size()):

        site = sites_listbox.get(i).lower()

        if website == site:

            sites_listbox.selection_clear(0, "end")

            sites_listbox.selection_set(i)

            sites_listbox.see(i)

            found = True

            break

    if not found:

        messagebox.showinfo(
            "Search",
            "Website Not Found"
        )
def update_stats():

    count = sites_listbox.size()

    stats_label.configure(
        text=f"🛡Total Blocked Websites: {count}"
    )
def apply_realtime_blocking(site):

    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

    with open(hosts_path, "a") as file:

        file.write(f"\n127.0.0.1 {site}")
        file.write(f"\n127.0.0.1 www.{site}")
def save_data():

    global total_scans
    global threats_found
    global current_user_email

    total_scans = len(scan_history)

    threats_found = sum(
        1
        for scan in scan_history
        if scan.get("status") in ["Malicious", "Suspicious"]
    )

    filename = f"{current_user_email}_data.json"

    data = {
        "total_scans": total_scans,
        "threats_found": threats_found
    }

    with open(filename, "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )





def load_scan_history():

    global scan_history
    global current_user_email

    if not current_user_email:

        scan_history = []

        return

    filename = f"{current_user_email}_history.json"

    print("Loading file:", filename)

    if os.path.exists(filename):

        with open(filename, "r") as file:

            scan_history = json.load(file)

    else:

        scan_history = []

    print("Loading history from:", filename)
    print("Scans loaded:", len(scan_history))

    if 'history_box' in globals():

        history_box.delete(
            "1.0",
            "end"
        )

        for scan in scan_history:

            history_box.insert(
                "end",
                f"{scan.get('website','N/A')} | "
                f"{scan.get('status','N/A')}\n"
            )
 


def save_data():

    data = {

        "total_scans": total_scans,

        "threats_found": threats_found,

        "blocked_sites": auto_blocked_sites,

        "scan_history": scan_history

    }

    with open(
        DATA_FILE,
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )
      
def scan_website():

    global total_scans
    global threats_found

    website = scanner_entry.get().strip()

    if not website:

        messagebox.showwarning(
            "Warning",
            "Please enter a website URL."
        )
        return

    scan_progress.set(0.1)

    result_label.configure(
        text="🔄 Scanning Website..."
    )

    app.update()

    try:

        # -----------------------------
        # DOMAIN INFO
        # -----------------------------

        domain = (
            website
            .replace("https://", "")
            .replace("http://", "")
            .split("/")[0]
        )

        try:

            ip_address = socket.gethostbyname(
                domain
            )

        except:

            ip_address = "Unknown"

        try:

            domain_info = whois.whois(
                domain
            )

            registrar = str(
                domain_info.registrar
            )

            creation_date = domain_info.creation_date
            expiration_date = domain_info.expiration_date

            if isinstance(
                creation_date,
                list
            ):
                creation_date = creation_date[0]

            if isinstance(
                expiration_date,
                list
            ):
                expiration_date = expiration_date[0]

            creation_date = str(
                creation_date
            )

            expiration_date = str(
                expiration_date
            )

        except:

            registrar = "Unknown"

            creation_date = "Unknown"

            expiration_date = "Unknown"

        # -----------------------------
        # VIRUSTOTAL
        # -----------------------------

        headers = {
            "x-apikey": VT_API_KEY
        }

        scan_progress.set(0.3)

        app.update()

        submit_response = requests.post(
            "https://www.virustotal.com/api/v3/urls",
            headers=headers,
            data={
                "url": website
            },
            timeout=20
        )

        submit_response.raise_for_status()

        analysis_id = (
            submit_response.json()
            ["data"]["id"]
        )

        analysis_url = (
            f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"
        )

        completed = False

        for _ in range(30):

            analysis_response = requests.get(
                analysis_url,
                headers=headers,
                timeout=20
            )

            analysis_response.raise_for_status()

            result = analysis_response.json()
            status = (
                result["data"]
                ["attributes"]
                ["status"]
            )



            if status == "completed":

                stats = (
                    result["data"]
                    ["attributes"]
                    ["stats"]
                )

                malicious = stats.get(
                    "malicious",
                    0
                )

                suspicious = stats.get(
                    "suspicious",
                    0
                )

                harmless = stats.get(
                    "harmless",
                    0
                )

                undetected = stats.get(
                    "undetected",
                    0
                )

                completed = True

                break

            time.sleep(2)

        if not completed:

            result_label.configure(
                text="⚠️ VirusTotal Still Processing"
            )

            malicious = 0
            suspicious = 0
            harmless = 0
            undetected = 0

            status = "Pending"
        # -----------------------------

        total_scans += 1

        if malicious > 0 or suspicious > 0:

            threats_found += 1

        save_data()

        update_dashboard_stats()
        update_security_score()

        scan_progress.set(1.0)

        # -----------------------------
        # STATUS
        # -----------------------------

        
        if malicious > 0:

            status_text = (
                f"🚨 MALICIOUS ({malicious})"
            )

            status = "Malicious"

            if website not in auto_blocked_sites:

                auto_blocked_sites.append(
                    website
                )

                save_blocked_sites()

        elif suspicious > 0:

            status_text = (
                f"⚠️ SUSPICIOUS ({suspicious})"
            )

            status = "Suspicious"

            if website not in auto_blocked_sites:

                auto_blocked_sites.append(
                    website
                )

                save_blocked_sites()

        else:

            status_text = (
                "✅ SAFE WEBSITE"
            )

            status = "Safe"

        result_label.configure(
            text=status_text
        )
        update_dashboard_stats()

        # -----------------------------
        # HISTORY ENTRY
        # -----------------------------

        history_entry = {

            "website": website,

            "ip": ip_address,

            "registrar": registrar,

            "creation_date": creation_date,

            "expiration_date": expiration_date,

            "malicious": malicious,

            "suspicious": suspicious,

            "harmless": harmless,

            "undetected": undetected,

            "status": status,

            "scan_time":
            datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            )
        }

        scan_history.append(
        history_entry
        )
        print("History Added")

        save_scan_history()

        print("History Saved")
            

        



# Save history permanently
        with open(
            f"{current_user_email}_history.json",
            "w"
        ) as f:

            json.dump(
                scan_history,
                f,
                indent=4
                )
                # -----------------------------
        # HISTORY PAGE
        # -----------------------------

        history_box.insert(
            "end",
            f"{website} | "
            f"M:{malicious} | "
            f"S:{suspicious} | "
            f"{status}\n"
        )

        # -----------------------------
        # REPORT PAGE
        # -----------------------------

        scan_report.delete(
            "1.0",
            "end"
        )

        scan_report.insert(
            "end",
            f"""
Website:
{website}

IP Address:
{ip_address}

Registrar:
{registrar}

Creation Date:
{creation_date}

Expiration Date:
{expiration_date}

Status:
{status}

Malicious:
{malicious}

Suspicious:
{suspicious}

Harmless:
{harmless}

Undetected:
{undetected}

Scan Time:
{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}
"""
        )

        save_data()

    except requests.exceptions.Timeout:

        messagebox.showerror(
            "Connection Error",
            "VirusTotal request timed out."
        )

    except requests.exceptions.RequestException as e:

        messagebox.showerror(
            "Network Error",
            str(e)
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )











def back_to_dashboard_from_history():

    history_frame.pack_forget()

    dashboard_frame.pack(
        fill="both",
        expand=True
    )


def open_reports():

    dashboard_frame.pack_forget()

    reports_frame.pack(
        fill="both",
        expand=True
    )

    reports_box.delete(
        "1.0",
        "end"
    )

    for scan in scan_history:

        if isinstance(scan, dict):

            reports_box.insert(
                "end",
                f"""
Website: {scan.get('website','N/A')}
IP: {scan.get('ip','N/A')}
Status: {scan.get('status','N/A')}
Malicious: {scan.get('malicious',0)}
Suspicious: {scan.get('suspicious',0)}
Scan Time: {scan.get('scan_time','N/A')}

----------------------------------

"""
            )

def export_last_scan():

    if not scan_history:

        messagebox.showwarning(
            "Warning",
            "No scan available."
        )
        return

    export_selected_scan(
        scan_history[-1]
    )

def export_report():
    if not scan_history:
        messagebox.showwarning(
            "No Data",
            "No scan history available."
        )
        return

    pdf = SimpleDocTemplate(
        f"CyberShield_Report_{datetime.now().strftime('%d%m%Y_%H%M%S')}.pdf"
    )
    styles = getSampleStyleSheet()

    content = []

    title = Paragraph(
        "Cyber Shield Scan Report",
        styles['Title']
    )

    content.append(title)
    content.append(Spacer(1, 20))

    for scan in scan_history:

        if not isinstance(scan, dict):
            continue

        text = f"""
        <b>Website:</b> {scan.get('website','N/A')}<br/>
        <b>IP Address:</b> {scan.get('ip','N/A')}<br/>
        <b>Registrar:</b> {scan.get('registrar','N/A')}<br/>
        <b>Status:</b> {scan.get('status','N/A')}<br/>
        <b>Malicious:</b> {scan.get('malicious',0)}<br/>
        <b>Suspicious:</b> {scan.get('suspicious',0)}<br/>
        <b>Harmless:</b> {scan.get('harmless',0)}<br/>
        <b>Undetected:</b> {scan.get('undetected',0)}<br/>
        <b>Creation Date:</b> {scan.get('creation_date','N/A')}<br/>
        <b>Expiration Date:</b> {scan.get('expiration_date','N/A')}<br/>
        <b>Scan Time:</b> {scan.get('scan_time','N/A')}<br/><br/>
        """

        content.append(
            Paragraph(text, styles['BodyText'])
        )
    pdf.build(content)

    messagebox.showinfo(
        "Success",
        "Report Exported Successfully"
    )

def is_blocked(url):

    for site in auto_blocked_sites:

        if site.lower() in url.lower():
            return True

    for site in manual_blocked_sites:

        if site.lower() in url.lower():
            return True

    return False
def open_settings():

    settings_window = ctk.CTkToplevel(app)

    settings_window.title("Settings")
    settings_window.geometry("400x300")

    ctk.CTkLabel(
        settings_window,
        text="Cyber Shield Settings"
    ).pack(pady=20)

    ctk.CTkButton(
    settings_window,
    text="Light Theme",
    command=lambda: ctk.set_appearance_mode("Light")
    ).pack(pady=10)
    ctk.CTkButton(
    settings_window,
    text="Dark Theme",
    command=lambda: ctk.set_appearance_mode("Dark")
    ).pack(pady=10)
    ctk.CTkLabel(
    settings_window,
    text=f"User: {current_user_email}"
    ).pack(pady=5)
def back_from_settings():

    settings_frame.pack_forget()

    dashboard_frame.pack(
        fill="both",
        expand=True
    )


def manual_block_website():

    website = website_entry.get().strip().lower()

    if website == "":
        messagebox.showerror(
            "Error",
            "Enter Website"
        )
        return

    if website not in auto_blocked_sites:

        auto_blocked_sites.append(
            website
        )

        manual_blocked_sites.append(
            website
        )

        apply_realtime_blocking(
            website
        )

        sites_listbox.insert(
            "end",
            website
        )

        save_blocked_sites()

        update_dashboard_stats()

        messagebox.showinfo(
            "Success",
            f"{website} blocked"
        )
    




def open_scan_history():

    dashboard_frame.pack_forget()

    history_frame.pack(
        fill="both",
        expand=True
    )

    history_box.delete(
        "1.0",
        "end"
    )

    for scan in scan_history:

        history_box.insert(
            "end",
            f"{scan.get('website','N/A')} | "
            f"{scan.get('status','N/A')}\n"
        )

home_frame = ctk.CTkFrame(app)
home_frame.pack(fill="both", expand=True)

title = ctk.CTkLabel(
    home_frame,
    image=logo_image,
    text=""
)
title.pack(pady=10)


subtitle = ctk.CTkLabel(
    home_frame,
    text="Advanced Malicious Website Blocker",
    font=("Arial", 18)
)
subtitle.pack(pady=10)

team_btn = ctk.CTkButton(
    home_frame,
    text="ProTech Defenders",
    command=show_team,
    width=250,
    height=40
)
team_btn.pack(pady=20)

login_btn = ctk.CTkButton(
    home_frame,
    text="Login",
    width=250,
    height=40,
    command=open_login
)
login_btn.pack(pady=10)

register_btn = ctk.CTkButton(
    home_frame,
    text="Register",
    width=250,
    height=40,
    command=open_register
)
register_btn.pack(pady=10)
# REGISTER PAGE

register_frame = ctk.CTkFrame(app)

register_title = ctk.CTkLabel(
    register_frame,
    text="User Registration",
    font=("Arial", 28, "bold")
)
register_title.pack(pady=20)

email_entry = ctk.CTkEntry(
    register_frame,
    width=350,
    placeholder_text="Email Address"
)
email_entry.pack(pady=10)

otp_entry = ctk.CTkEntry(
    register_frame,
    width=350,
    placeholder_text="Enter OTP"
)
otp_entry.pack(pady=10)

password_frame = ctk.CTkFrame(
    register_frame,
    fg_color="transparent"
)
password_frame.pack(pady=10)

password_entry = ctk.CTkEntry(
    password_frame,
    width=300,
    placeholder_text="Password",
    show="*"
)
password_entry.pack(side="left", padx=5)

eye_btn = ctk.CTkButton(
    password_frame,
    text="👁",
    width=40,
    command=toggle_password
)
eye_btn.pack(side="left")
send_btn = ctk.CTkButton(
    register_frame,
    text="Send OTP",
    command=send_otp
)
send_btn.pack(pady=10)


verify_btn = ctk.CTkButton(
    register_frame,
    text="Verify OTP",
    command=verify_otp
)
verify_btn.pack(pady=10)

register_user_btn = ctk.CTkButton(
    register_frame,
    text="Register",
    command=register_user
)
register_user_btn.pack(pady=10)

back_btn = ctk.CTkButton(
    register_frame,
    text="Back",
    command=back_home
)
back_btn.pack(pady=10)
# LOGIN PAGE

login_frame = ctk.CTkFrame(app)

login_title = ctk.CTkLabel(
    login_frame,
    text="User Login",
    font=("Arial", 28, "bold")
)
login_title.pack(pady=20)

login_email = ctk.CTkEntry(
    login_frame,
    width=350,
    placeholder_text="Email Address"
)
login_email.pack(pady=10)

login_password = ctk.CTkEntry(
    login_frame,
    width=350,
    placeholder_text="Password",
    show="*"
)
login_password.pack(pady=10)

login_page_btn = ctk.CTkButton(
    login_frame,
    text="Login",
    command=login_user
)
login_page_btn.pack(pady=10)

back_login_btn = ctk.CTkButton(
    login_frame,
    text="Back",
    command=back_home_login
)
back_login_btn.pack(pady=10)
# ================= DASHBOARD =================
# ================= DASHBOARD =================

dashboard_scroll = ctk.CTkScrollableFrame(
    app
)

dashboard_frame = dashboard_scroll

dashboard_title = ctk.CTkLabel(
    dashboard_frame,
    text="🛡CYBER SHIELD",
    font=("Arial", 32, "bold")
)
dashboard_title.pack(pady=20)

'''stats_card = ctk.CTkLabel(
    dashboard_frame,
    text="📊 Scans: 0 | 🚫 Blocked: 0 | 🚨 Threats: 0",
    font=("Arial", 14)
)
stats_card.pack(pady=2)'''
security_score_label = ctk.CTkLabel(
    dashboard_frame,
    text="🛡 Security Score: 100",
    font=("Arial",18,"bold")
)
security_score_label.pack(pady=2)

user_label = ctk.CTkLabel(
    dashboard_frame,
    text="👤 User",
    font=("Arial", 12)
)

user_label.place(
    relx=0.97,
    y=20,
    anchor="ne"
)

dashboard_subtitle = ctk.CTkLabel(
    dashboard_frame,
    text="Advanced Malicious Website Blocker",
    font=("Arial", 16)
)
dashboard_subtitle.pack(pady=5)

welcome_frame = ctk.CTkFrame(
    dashboard_frame,
    width=700,
    height=120
)
welcome_frame.pack(pady=20)

welcome_label = ctk.CTkLabel(
    welcome_frame,
    text="Threat Monitoring & Protection Center",
    font=("Arial", 18, "bold")
)
welcome_label.pack(pady=20)
stats_label = ctk.CTkLabel(
    dashboard_frame,
    text="🛡Total Blocked Websites: 0",
    font=("Arial", 16, "bold")
)
stats_label.pack(pady=10)
# Button Cards Container

cards_frame = ctk.CTkFrame(
    dashboard_frame,
    fg_color="transparent"
)
cards_frame.pack(pady=20)

# Row 1

quick_scan_btn = ctk.CTkButton(
    cards_frame,
    text="🛡Quick Scan",
    width=160,
    height=50,
    font=("Arial", 18, "bold"),
    command=open_quick_scan
)
quick_scan_btn.grid(row=0, column=0, padx=10, pady=10)
history_btn = ctk.CTkButton(
    cards_frame,
    text="📜 Scan History",
    command=open_scan_history,
    font=("Arial", 16, "bold"),
    width=180,
    height=50
)
history_btn.grid(
    row=2,
    column=0,
    padx=10,
    pady=10
)
deep_scan_btn = ctk.CTkButton(
    cards_frame,
    text="🔍 Deep Scan",
    width=160,
    height=50,
    font=("Arial", 18, "bold"),
    command=open_scanner
)
deep_scan_btn.grid(row=0, column=1, padx=10, pady=10)
# Row 2
blocked_sites_btn = ctk.CTkButton(
    cards_frame,
    text="🚫 Blocked Websites",
    width=160,
    height=50,
    font=("Arial", 14, "bold"),
    command=open_blocked_sites
)
blocked_sites_btn.grid(
    row=1,
    column=0,
    padx=10,
    pady=10
)
blocked_sites_btn.grid(row=1, column=0, padx=10, pady=10)

reports_btn = ctk.CTkButton(
    cards_frame,
    text="📊 Reports",
    command=open_reports,
    width=170,
    height=50,
    font=("Arial", 18, "bold")
)

reports_btn.grid(
    row=1,
    column=1,
    padx=10,
    pady=10
)


# Row 3
settings_frame = ctk.CTkFrame(app)
settings_title = ctk.CTkLabel(
    settings_frame,
    text="⚙ Settings",
    font=("Arial", 24, "bold")
)
settings_title.pack(pady=20)
theme_label = ctk.CTkLabel(
    settings_frame,
    text="🎨 Theme"
)

theme_label.pack(pady=10)


def change_theme(choice):

    ctk.set_appearance_mode(choice)


theme_menu = ctk.CTkOptionMenu(
    settings_frame,
    values=[
        "Dark",
        "Light",
        "System"
    ],
    command=change_theme
)
theme_menu.pack(pady=10)
realtime_switch = ctk.CTkSwitch(
    settings_frame,
    text="🛡 Enable Real-Time Protection"
)

realtime_switch.pack(pady=10)
notification_switch = ctk.CTkSwitch(
    settings_frame,
    text="🔔 Enable Notifications"
)
notification_switch.pack(pady=10)

update_switch = ctk.CTkSwitch(
    settings_frame,
    text="🔄 Auto Update Threat Database"
)

update_switch.pack(pady=10)


back_btn = ctk.CTkButton(
    settings_frame,
    text="⬅ Back",
    command=back_from_settings
)

back_btn.pack(pady=20)

settings_btn = ctk.CTkButton(
    cards_frame,
    text="⚙️ Settings",
    width=160,
    height=50,
    font=("Arial", 18, "bold"),
    command=open_settings
)
settings_btn.grid(
    row=2,
    column=1,
    padx=10,
    pady=10
)


logout_btn = ctk.CTkButton(
    cards_frame,
    text="🚪 Logout",
    width=170,
    height=50,
    font=("Arial", 18, "bold"),
    command=logout
)

logout_btn.grid(
    row=3,
    column=0,
    columnspan=2,
    pady=10
)
# ================= BLOCKED WEBSITES =================

blocked_frame = ctk.CTkFrame(app)

blocked_title = ctk.CTkLabel(
    blocked_frame,
    text="🚫 Blocked Websites",
    font=("Arial", 24, "bold")
)
blocked_title.pack(pady=20)
ctk.CTkLabel(
    blocked_frame,
    text="🛡️Manual Website Blocking",
    font=("Arial", 16, "bold")
).pack(pady=5)

website_entry = ctk.CTkEntry(
    blocked_frame,
    width=300,
    placeholder_text="Enter Website to block"
)
website_entry.pack(pady=10)
block_btn = ctk.CTkButton(
    blocked_frame,
    text="🚫 Block Website",
    command=manual_block_website
)

block_btn.pack(pady=10)
sites_listbox = tk.Listbox(
    blocked_frame,
    width=35,
    height=6,
    bg="#2b2b2b",
    fg="white",
    font=("Arial", 12),
    selectbackground="#1f6aa5"
)
sites_listbox.pack(pady=10)
load_blocked_sites()

remove_btn = ctk.CTkButton(
    blocked_frame,
    text="❌ Remove Website",
    command=remove_website
)
remove_btn.pack(pady=5)

search_btn = ctk.CTkButton(
    blocked_frame,
    text="🔍 Search Website",
    command=search_website
)
search_btn.pack(pady=5)

back_btn = ctk.CTkButton(
    blocked_frame,
    text="⬅ Back",
    command=back_to_dashboard
)
back_btn.pack(pady=20)
# ================= SCANNER PAGE ================
scanner_frame = ctk.CTkFrame(app)


scanner_title = ctk.CTkLabel(
    scanner_frame,
    text="🔍 Website Scanner",
    font=("Arial", 24, "bold")
)
scanner_title.pack(pady=20)
scanner_entry = ctk.CTkEntry(
    scanner_frame,
    width=350,
    placeholder_text="Enter Website URL"
)
scanner_entry.pack(pady=10)
scan_progress = ctk.CTkProgressBar(
    scanner_frame,
    width=300
)

scan_progress.pack(pady=10)

scan_progress.set(0)

result_label = ctk.CTkLabel(
    scanner_frame,
    text="Threat Level: Not Scanned",
    font=("Arial", 16)
)
result_label.pack(pady=20)
scan_report = ctk.CTkTextbox(
    scanner_frame,
    width=500,
    height=150
)

scan_report.pack(pady=10)
scan_btn = ctk.CTkButton(
    scanner_frame,
    text="🔍 Scan Website",
    command=scan_website
)
scan_btn.pack(pady=10)
back_btn = ctk.CTkButton(
    scanner_frame,
    text="⬅ Back",
    command=back_to_dashboard_from_scanner,
    width=150
)

back_btn.pack(pady=10)
# ================= HISTORY PAGE =================

history_frame=ctk.CTkFrame(app)
history_frame.pack_forget()

history_title = ctk.CTkLabel(
    history_frame,
    text="📋 Scan History",
    font=("Arial", 22, "bold")
)
history_title.pack(pady=20)

history_box = ctk.CTkTextbox(
    history_frame,
    width=700,
    height=400
)
history_box.pack(pady=10)
for scan in scan_history:

    if not isinstance(scan, dict):
        continue

    history_box.insert(
        "end",
        f"{scan.get('website','N/A')} | "
        f"M:{scan.get('malicious',0)} | "
        f"S:{scan.get('suspicious',0)} | "
        f"{scan.get('status','Unknown')}\n"
    )
history_back_btn = ctk.CTkButton(
    history_frame,
    text="⬅ Back",
    command=lambda: show_frame(dashboard_frame)
)
history_back_btn.pack(pady=10)
def clear_history():

    scan_history.clear()

    history_box.delete(
        "1.0",
        "end"
    )
    

    for scan in scan_history:

        if isinstance(scan, dict):

            history_box.insert(
                "end",
                f"{scan.get('website','N/A')} | {scan.get('status','N/A')}\n"
            )

clear_history_btn = ctk.CTkButton(
    history_frame,
    text="🗑 Clear History",
    command=clear_history
)

clear_history_btn.pack(pady=5)
history_btn = ctk.CTkButton(
    cards_frame,
    text="📋 Scan History",
    command=open_scan_history
)
quick_scan_frame = ctk.CTkFrame(app)

quick_title = ctk.CTkLabel(
    quick_scan_frame,
    text="⚡ Quick Scan",
    font=("Arial", 24, "bold")
)

quick_title.pack(pady=20)

quick_scan_entry = ctk.CTkEntry(
    quick_scan_frame,
    width=350,
    placeholder_text="Enter Website URL"
)

quick_scan_entry.pack(pady=10)

quick_scan_btn2 = ctk.CTkButton(
    quick_scan_frame,
    text="⚡ Scan",
    command=quick_scan
)

quick_scan_btn2.pack(pady=10)

quick_result_label = ctk.CTkLabel(
    quick_scan_frame,
    text=""
    
)

quick_result_label.pack(pady=10)

quick_back_btn = ctk.CTkButton(
    quick_scan_frame,
    text="⬅ Back",
    command=lambda: [
        quick_scan_frame.pack_forget(),
        dashboard_frame.pack(
            fill="both",
            expand=True
        )
    ]
)

quick_back_btn.pack(pady=10)
reports_frame = ctk.CTkFrame(app)

reports_title = ctk.CTkLabel(
    reports_frame,
    text="📊 Security Reports",
    font=("Arial", 24, "bold")
)

reports_title.pack(pady=20)

reports_box = ctk.CTkTextbox(
    reports_frame,
    width=600,
    height=300
)

reports_box.pack(pady=20)
report_combo = ctk.CTkComboBox(
    reports_frame,
    values=[
        "Select Report",
        "Latest Scan",
        "All Scans"
    ]
)
report_combo.pack(
    pady=10
)
report_combo.set(
    "Select Report"
)
export_btn = ctk.CTkButton(
    cards_frame,
    text="📄 Export Report",
    command=open_reports
) 
export_selected_btn = ctk.CTkButton(
    reports_frame,
    text="📄 Export Selected Scan",
    command=export_last_scan
)

export_selected_btn.pack(pady=10)


reports_back_btn = ctk.CTkButton(
    reports_frame,
    text="⬅ Back",
    command=lambda:[
        reports_frame.pack_forget(),
        dashboard_frame.pack(fill="both", expand=True)
    ]
)

reports_back_btn.pack(pady=10)

load_blocked_sites()
settings_title = ctk.CTkLabel(
    settings_frame,
    text="⚙ Settings",
    font=("Arial", 24, "bold")
)

settings_title.pack(pady=20)

back_btn = ctk.CTkButton(
    settings_frame,
    text="⬅ Back",
    command=back_from_settings
)

back_btn.pack(pady=10)
load_data()
update_dashboard_stats()
update_security_score()
load_scan_history()
app.mainloop()
