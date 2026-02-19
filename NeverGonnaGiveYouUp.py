import os
import winreg
from win32com.client import Dispatch

#Name the file and the video URL you want to link to
NAME = "NeverLetsMeDown"
URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

#Finds your public Desktop
def get_desktop_path() -> str:
    with winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
    ) as k:
        desktop, _ = winreg.QueryValueEx(k, "Desktop")
    return os.path.expandvars(desktop)

#Looks for your Edge app and locates Icon for copying
def find_app_exe(app: str) -> str | None:
    """
    Find an exe via Windows 'App Paths' registry (most reliable).
    app examples: 'msedge.exe', 'chrome.exe'
    """
    subkeys = [
        rf"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\{app}",
        rf"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\App Paths\{app}",
    ]
    for subkey in subkeys:
        for hive in (winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE):
            try:
                with winreg.OpenKey(hive, subkey) as k:
                    exe, _ = winreg.QueryValueEx(k, "")
                    if exe and os.path.exists(exe):
                        return exe
            except OSError:
                pass
    return None

#Creates desktop shortcut
def create_shortcut():
    desktop = get_desktop_path()
    lnk_path = os.path.join(desktop, f"{NAME}.lnk")

    edge_exe = find_app_exe("msedge.exe")
    chrome_exe = find_app_exe("chrome.exe")

    # Choose icon source: Edge > Chrome > generic shell icon as fallbacks
    if edge_exe:
        icon = f"{edge_exe},0"
    elif chrome_exe:
        icon = f"{chrome_exe},0"
    else:
        icon = r"%SystemRoot%\System32\shell32.dll,13"

    shell = Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(lnk_path)

    #set TargetPath directly to the URL (Windows will open default browser, not necessarily edge)
    shortcut.TargetPath = URL
    shortcut.IconLocation = icon
    shortcut.Save()

    print("Created shortcut:", lnk_path)
    print("Icon source:", icon)


if __name__ == "__main__":
    create_shortcut()
