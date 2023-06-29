import os
npm_switch = 0
npm_v_check = 0
git_switch = 0
print("ZeroneLABS WMS Dependencies Installer...")
print("Do not disconnect from internet")
os.system("pause")
print("Installing QT Window Framework...")
os.system("pip install pyqt5")
def is_npm_installed():
    print("checking NodeJavaScript status...")
    return os.system('npm -v') == 0

if is_npm_installed():
    print("npm is installed.")
    npm_switch = 0
else:
    print("npm is not installed.")
    npm_witch = 1
import os

def is_git_installed():
    return os.system('git --version') == 0

if is_git_installed():
    print("Git is installed.")
    git_switch = 0
else:
    print("Git is not installed.")
    print("Close this commandprompt window, check the GIT installation and retry...")
    os.system("pause")
    git_switch = 1

if git_switch == 0:
    print("Git is ready !")

if npm_switch == 0:
    print("Installing Mudslide Library...")
    os.system("npm install -g mudslide")
print("End of script")
os.system("pause")