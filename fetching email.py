import requests
import re 
from bs4 import BeautifulSoup
import csv

# particular url 
#email_id=re.compile('\w+@\w+.\w+')

#html=requests.get("https://sparkmailapp.com/formal-email-template").text
#soup=BeautifulSoup(html,"html.parser")
#emails=soup.find_all(string=email_id)
#for email in emails:
    #print(email)
    
 #--------------------------------------------------------------------
    
# regular expretions
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
#email_condition="\w+@\w+.\w+"
emails=re.compile(email_condition)

#file read
with open('E:\program/task_algo_email.txt','r') as f:
    
    line_count = 0
    for line in f:
        #print(line.strip())
        
        requ=requests.get(line.strip()).text
        #print(requ)
        soup= BeautifulSoup(requ,"html.parser")
        all_email=soup.find_all(string=emails)
        
        for email in all_email:
            
            #with open("E:\program/fetching_email.csv","w") as new_csv:
             #   new_csv.write(email)    
            print(email)   
        line_count += 1
    
        
        

