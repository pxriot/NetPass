import subprocess
from pyfiglet import Figlet
from colorama import Fore, Style

f = Figlet(font='slant')
colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE]
print(Fore.MAGENTA + Fore.GREEN + f.renderText ('NetPass'))

print(Fore.LIGHTGREEN_EX + "Coded by PXRSoftware")
print("-" * 30)

profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profile_names = [line.split(':')[1].strip() for line in profiles if "All User Profile" in line]

wifi_info = {}
for name in profile_names:
    try:
        wifi_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', name, 'key=clear']).decode('utf-8').split('\n')
        password_line = [line.split(':')[1].strip() for line in wifi_data if "Key Content" in line]
        if password_line:
            wifi_info[name] = password_line[0]
        else:
            wifi_info[name] = "Password not found"
    except subprocess.CalledProcessError:
        wifi_info[name] = "ENCODING ERROR"

for name, password in wifi_info.items():
    print(Fore.MAGENTA + f"Network Name: {name}")
    print(Fore.GREEN + f"Password: {password}")
    print("-" * 30)

print(Style.RESET_ALL)