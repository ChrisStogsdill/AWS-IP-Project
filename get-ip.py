from requests import get
from send_aws_email import sendEmail

ip = get('https://api.ipify.org').content.decode('utf8')
print(f'My public IP address is {ip}')

sendEmail(ip)