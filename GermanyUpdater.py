import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL = "https://footystats.org/clubs/germany-national-team-7980"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}


def checkGermany():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, "html.parser")

    totalGoalsFor = soup.find_all("div", class_ = "g")[3].get_text()
    totalGoalsForInt = int(totalGoalsFor)

    totalGoalsAgainst = soup.find_all("div", class_ = "a")[3].get_text()
    totalGoalsAgainstInt = int(totalGoalsAgainst)


    if totalGoalsForInt == 23 or totalGoalsForInt == 24:
        send_mail_scored()
    if totalGoalsAgainstInt == 16 or totalGoalsAgainstInt == 17:
        send_mail_conceded()

def send_mail_scored():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("PythonPractice7@gmail.com", "Coconut6")

    subject = "Germany Scored!"
    body = "Check Score https://footystats.org/clubs/germany-national-team-7980"
    
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        "PythonPractice7@gmail.com",
        "PythonPractice7@gmail.com",
        msg
    )

    print("EMAIL HAS BEEN SENT!")
    server.quit()

def send_mail_conceded():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("PythonPractice7@gmail.com", "Coconut6")

    subject = "Germany Conceded!"
    body = "Check Score https://footystats.org/clubs/germany-national-team-7980"
    
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        "PythonPractice7@gmail.com",
        "PythonPractice7@gmail.com",
        msg
    )

    print("EMAIL HAS BEEN SENT!")
    server.quit()

while True:
    checkGermany()
    time.sleep(60*30)