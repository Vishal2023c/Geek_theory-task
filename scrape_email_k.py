import requests
import re 
from bs4 import BeautifulSoup
import csv
class scrape:
    def __init__(self):
        self.emails=re.compile("^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$")
        return 
    def scrape_email(self):
        all_emails=self.emails
        with open("requirement.txt","r") as f:           
            line_count = 0
            for line in f:               
                url="https://www.google.com/search?q="
                requ=requests.get(url+line).text
                soup= BeautifulSoup(requ,"html.parser")
                all_email=soup.find_all(string=all_emails)               
                for email in all_email:
                    print(email)
                    with open("fetching_email.csv","a") as new_csv:
                        new_csv.write(email)
                        new_csv.write("\n")                   
                line_count += 1
obj=scrape().scrape_email()


