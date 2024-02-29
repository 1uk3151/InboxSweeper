# InboxSweeper
Moves emails 2 or more days old to Trash. Only works with Gmail.  

THIS SCRIPT WILL MOVE ANY EMAILS IN THE GMAIL INBOX OVER 2 DAYS OLD TO TRASH!!!!!!!!
Create a folder for emails you prefer to keep. 
____________________________________________________________________

You must configure your Gmail account before using this script. 
  1. In Gmail Settings > See all settings > Forwarding and POP/IMAP > Enable IMAP
  2. In your Google account settings, create an app password (Search in settings for "app password"). The password can be named whatever
     you prefer. Google will randomly generate the password in the format:
           xxxx xxxx xxxx xxxx
     This is the password you will use in your credentials file.
____________________________________________________________________

To run the script, you must specify 2 arguments:
   1. Credentials file in yaml format. (See SampleCredFile.yaml for example of format.)
   2. Location of log output. Log file needs to be a txt file.

Here is an example of how to run the script: python.exe ./inboxSweeper.py ./SampleCredFile.yaml ./log.txt
____________________________________________________________________

To be effective, the script should be executed daily using Windows Task Scheduler or Linux Crontab.
Create a folder for emails that you prefer to keep. This script will remove any email in the Inbox over 2 days old!!!!!





