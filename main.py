from skpy import Skype
import os.path
slogin=Skype("mail address","password")
#use for sending image
contact=slogin.contacts["live:.cid.2405d0ce58c715aa"]
with open("image address","rb") as f:
    contact.chat.sendFile(f,"image file name",image=True)  
    
# contact=slogin.contacts
# for i in contact:
#     print(i)  # it will show all  conatct information  of your connection

# contact=slogin.contacts["live:.cid.2405d0ce58c715aa"]
# contact.chat.sendMsg("welcome to wscube Tech") #for sending message to a person

contact=slogin.contacts["live:.cid.2405d0ce58c715aa"]
group=slogin.chats.create(["userid_1_name","userid_2_name","userid_3_name"])  #it will make a group in skype