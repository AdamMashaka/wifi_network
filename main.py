import subprocess

data =subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i , 'key=clear']).decode('utf-8'), split('\n')
result = [b.]