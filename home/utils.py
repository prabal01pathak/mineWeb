import requests
import json
import os
import sys
import re
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from django.core.mail import EmailMultiAlternatives 


def medium_blog(url):
    """
    This function will return the title and the content of the blog
    """
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        url = data['items'][0]['link']
        items = data['items']
        blogs = []
        for i, item in enumerate(items):
            title = item['title']
            url = item['link']
            thumbnail = item['thumbnail']
            description = item['description']
            sblog = [title, url, thumbnail, description]
            blogs.append(sblog)
        return blogs


def git_projects(url):
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        projects = []
        for i, item in enumerate(data):
            if not item['fork'] and item['description'] != None:
                url = item['html_url']
                description = item['description']
                repos = [url, description]
                projects.append(repos)
        return projects


def send_simple_mail(data):
    sender_mail = os.environ['EMAIL_ADDR']
    reciver_mail = data['email']
    password = os.environ['PASS']
    msg = EmailMessage()
    msg1 = EmailMessage()
    # Send the message to the mail server.  This will send it to the recipient as well  as the sender.
    msg['Subject'] = f"Hey, Dear {data['name']}  from Prabal's website"
    msg['From'] = formataddr(("Prabal's",sender_mail))
    msg['To'] = formataddr(("Prabal's",reciver_mail))
    msg1['Subject'] = f"USER {data['name']} message."
    msg1['From'] = sender_mail
    msg1['To'] = sender_mail
    msg1.set_content(f'''Name: {data["name"]}\n
                       Message: {data["message"]}\n
                       Email: {data["email"]}\n
                       Mobile: {data["mobile"]}''')

    print(msg)
    print(msg1)
    msg.add_alternative(f"""
    <!DOCTYPE html>
    <html>
    <body>
    <div style='font-size: 1.3em;box-shadow: black 0px 0px 0px 10px,black 0px 0px 0px 20px; font-family: Georgia;background:lightblue;border:2px solid green;padding: 10px;margin: 10px;'>Hey, Dear <h1 style='display: inline;'>{data['name']}.</h1>  thank you for your interest in my website we will reply get back to you soon.</div>
    </body>
    </html>
    """, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_mail, password)
        smtp.send_message(msg)
        smtp.send_message(msg1)
        print('done')


def send_django_mail(data):
    Subject = f"Hey, Dear {data['name']}  from Prabals website"
    From = formataddr(("Prabals",sender_mail))
    To = formataddr(("Prabals",reciver_mail))
    html_content = f"""
            <!DOCTYPE html>
            <html>
            <body>
            <div style='font-size: 1.3em;box-shadow: black 0px 0px 0px 10px,black 0px 0px 0px 20px; font-family: Georgia;background:lightblue;border:2px solid green;padding: 10px;margin: 10px;'>Hey, Dear <h1 style='display: inline;'>{data['name']}.</h1>  thank you for your interest in my website we will reply get back to you soon.</div>
            </body>
            </html>
            """
    msg = EmailMultiAlternatives(Subject,"hello",From,[To])
    msg.attach_alternative(html_content,"text/html")
    msg.content_subtype="html"
    msg.send()
