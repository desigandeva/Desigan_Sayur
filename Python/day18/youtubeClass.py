# 2.Same the YT video class in Day 17.
# Write a function that will send an email  to the author of the video, whenever the number of likes reaches 
# 1K, 2K or 5k.
# Write a function to list all Yoga videos.
# 
# class YouTube 
# List all the videos recorded by author "Kannan"
# List all the videos with more than 1K views
# Change the author of all the videos recorded by "Kannan" to "Kannan D."
# 20 students watched Kannan's "Intro to Python" video today. Update the videos views and print
# the total views for this video.
# 
# Write a function that will send an email  to the author of the video, whenever the number of likes reaches 1K, 2K or 5k.
# Write a function to list all Yoga videos.
# 
# 

import os
import smtplib
from email.message import EmailMessage

# build a function for get videos based on authoe name
def getVideos(author):
    print("Videos recorded by author",author)
    for videos in video_list:
        # find video created by author
        if(videos.getAuthor()==author):
            # print video
            print(videos.getVideo())
    print()
    return 0

# build a function for filter videos based on view
def filterView(views):
    print("Videos with more than ",views," views")
    for videos in video_list:
        # find video views > given view
        if(videos.getViews()>views):
            # print viedo
            print(videos.getVideo())
    print()
    return 0

# build a function for chage author name
def changeAuthor(old_author,new_author):
    for videos in video_list:
        # get old author name
        if(videos.getAuthor()==old_author):
            # change old name to new name
            videos.setAuthor(new_author)
    return 0

# build a function for add views based on video
def addViews(video,views):
    for videos in video_list:
        # get given video
        if(videos.getVideo()==video):
            # updtae views
            videos.setViews(videos.getViews()+views)
    return 0

# build a function for list updates
def listall():
    print("\nAll the Videos")
    for videos in video_list:
        # print video's
        print("Author : ",videos.getAuthor(),", Video : ",videos.getVideo(),", Views : ",videos.getViews(),'\n')
    return 0

# build a function for sending mail to author
def sendMail():
    print("start mail")
    sender_mail = input("Enter your Mail Id :")
    password = input("Enter your password : ")
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(sender_mail,password)
    print("Login successfully")
    for videos in video_list:
        if(videos.getViews()==1000 or videos.getViews()==2000 or videos.getViews()==5000):
            s.sendmail(sender_mail,videos.email,"Greeting "+videos.author+',\nTo improve the more views.')
    #         server.sendmail(senderMail,videos.email,"Greeting "+videos.author+',\nTo improve the more views.')
    print("Mail send Successfully..\n")
    # server.close()
    s.quit()
    return 0

# build a function to search a video
def search(word):
    for videos in video_list:
        # search given word in video
        if word in videos.video:
            # print video
            print(videos.video)
    print()
    return 0

# youtube class
class Youtube:
    # constructor
    def __init__(self,author,video,views,mail):
        self.author = author
        self.video = video
        self.views = views
        self.email = mail
    # getters and setters 
    def getAuthor(self):
        return self.author
    def setAuthor(self,author):
        self.author = author
    def getVideo(self):
        return self.video
    def setVideo(self,video):
        self.video = video
    def getViews(self):
        return self.views
    def setViews(self,views):
        self.views = views


# empty list for store videos
video_list = []
# build object video's with view's
kannan1 = Youtube("Kannan","Intro for Python",2500,'kanna@gmail.com')
kannan2 = Youtube("Kannan","Advance Python",200,'kanna@gmail.com')
kannan3 = Youtube("Kannan","Java Basic",500,'kanna@gmail.com')
kannan4 = Youtube("Kannan","Java Script",8500,'kanna@gmail.com')
kannan5 = Youtube("Kannan","HTML and CSS",6000,'kanna@gmail.com')
# appent to list
video_list.append(kannan1)
video_list.append(kannan2)
video_list.append(kannan3)
video_list.append(kannan4)
video_list.append(kannan5)
# sendMail()

# # List all the videos recorded by author "Kannan"
# getVideos("Kannan")
# # List all the videos with more than 1K views
# filterView(1000)
# # Change the author of all the videos recorded by "Kannan" to "Kannan D."
# changeAuthor("Kannan","Kannan D")
# # 20 students watched Kannan's "Intro to Python" video today. Update the videos views and print the total views for this video.
# addViews("Intro for Python",20)
# # list all the detials
# listall()
