# small Python script that creates a edge/chrome looking shortcut on your desktop and links you to a Youtube URL. For fun and harmless pranks.

---

To Run the script simply navigate to your folder that contains this project and run:
## py NeverGonnaGiveYouUp.py

---

If successful it will say:

Created shortcut: C:\Users\{Username}\OneDrive\Desktop\NeverLetsMeDown.lnk
Icon source: C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe,0

---

## Dependencies:

Python version 3.12+
pywin32

You can install pywin32 using Pip:
pip install pywin32

---

### I am assuming a windows desktop environment, does not run on Linux or Mac. 
This tool is for educational use only and should not be used for securing sensitive information / malicious intent. 
This is all in good faith and the name of fun, but it is easy to manipulate this tool to trick users into thinking they are clicking on edge or chrome and sending them to a malicious site for XSS, CSRF, MITM attacks, etc. 
Please dont do that by changing the URL at the URL = "" Line #7. 
Also do not change the name of the NAME ="" on Line 6 to something Like "Edge" or "Chrome" cause that could confuse a guy. 
One should not even consider changing the URL shortcut to another script that tracks user information or anything else potentially identifying or malintent.
