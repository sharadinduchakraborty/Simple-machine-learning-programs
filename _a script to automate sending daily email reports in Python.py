#!/usr/bin/env python
# coding: utf-8

# In[8]:



get_ipython().system('pip install schedule')


# In[ ]:


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

# Email configuration
sender_email = "your_email@gmail.com"
sender_password = "your_email_password"
receiver_email = "receiver_email@example.com"
subject = "Daily Report"
message = "Here is your daily report."

def send_email():
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Login to your Gmail account
        server.login(sender_email, sender_password)

        # Send email
        server.sendmail(sender_email, receiver_email, msg.as_string())

        # Quit server
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print("An error occurred:", e)

# Schedule the email to be sent daily at a specific time
schedule.every().day.at("09:00").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(1)


# In[ ]:


python daily_report.py


# In[ ]:




