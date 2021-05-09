import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'name'
email['to'] = 'his@email.com'
email['subject'] = 'All good!'

email.set_content(html.substitute({'name': 'Mihai'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('your@email.com', 'password')
	smtp.send_message(email)
	print('all good!')
