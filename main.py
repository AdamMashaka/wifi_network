#window user
import subprocess


data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

print("\n{:<30}| {:<}".format("Wi-Fi Name", "Password"))
print("----------------------------------------------")

for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print("{:<30}| {:<}".format(i, results[0]))
    except IndexError:
        print("{:<30}| {:<}".format(i, ""))
        
        
        
# Linux user        

import subprocess

# Get the list of profiles
data = subprocess.check_output(['nmcli', '-t', '-f', 'NAME', 'connection', 'show']).decode('utf-8').split('\n')
profiles = [i for i in data if i]

print("\n{:<30}| {:<}".format("Wi-Fi Name", "Password"))
print("----------------------------------------------")

for i in profiles:
    try:
        results = subprocess.check_output(['nmcli', '-s', '-g', '802-11-wireless-security.psk', 'connection', 'show', i]).decode('utf-8').strip()
        print("{:<30}| {:<}".format(i, results))
    except subprocess.CalledProcessError:
        print("{:<30}| {:<}".format(i, ""))