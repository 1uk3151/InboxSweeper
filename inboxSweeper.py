# You must specify 2 arguments:
#   1. Credentials file in yaml format.
#   2. Location of log output. Logfile needs to be a txt file. 

# To run script - Example: python.exe ./inboxSweeper.py ./creds.yaml ./log.txt

import imaplib
import yaml
import datetime
import sys

# yaml file containing username and password. Use the following format:
# user: "email address"
# password: "password"
credfile = str(sys.argv[1])
        
# Log file
logfile = str(sys.argv[2])
with open(logfile, mode="a") as log:
    
    try:
        
        # Read credentials from yaml file
        with open(credfile) as f:
            content = f.read()
            
        my_creds = yaml.load(content, Loader=yaml.FullLoader)
        
        user, password = my_creds["user"], my_creds["password"]
        
        
        # Connect to Gmail account
        imap_url = "imap.gmail.com"    
        
        my_mail = imaplib.IMAP4_SSL(imap_url)
        
        my_mail.login(user, password)
        
        
        # Delete emails in Inbox that are over 2 days old.
        my_mail.select("Inbox")
        
        yesterday = (datetime.date.today() - datetime.timedelta(1)).strftime("%d-%b-%Y")
        
        _, data = my_mail.search(None, f'before {yesterday}')
        
        mail_id_list = data[0].split()
        
        
        for mail in mail_id_list:
            my_mail.store(mail, "+X-GM-LABELS", "\\Trash")
            
        my_mail.expunge()
        
        # Close connection to Gmail account
        my_mail.close()
        my_mail.logout()
        
        # Write to log - SUCCESS
        log.write(f"{str(datetime.date.today())}  SUCCESS\n")
        log.write(f"Deleted {len(mail_id_list)} emails")
        log.write("\n\n")
        
    # Write error to log
    except BaseException as e:
        log.write(f"{datetime.date.today()}  {str(e)}")
        log.write("\n\n")



