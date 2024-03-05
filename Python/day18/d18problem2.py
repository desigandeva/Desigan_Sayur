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

# build a function for get videos based on authoe name
def getVideos(author):
    print("Videos recorded by author",author)
    for videos in video_list:
        if(videos.getAuthor()==author):
            print(videos.getVideo())
    print()
    return 0

# build a function for filter videos based on view
def filterView(views):
    print("Videos with more than ",views," views")
    for videos in video_list:
        if(videos.getViews()>views):
            print(videos.getVideo())
    print()
    return 0

# build a function for chage author name
def changeAuthor(old_author,new_author):
    for videos in video_list:
        if(videos.getAuthor()==old_author):
            videos.setAuthor(new_author)
    return 0

# build a function for add views based on video
def addViews(video,views):
    for videos in video_list:
        if(videos.getVideo()==video):
            videos.setViews(videos.getViews()+views)
    return 0

# build a function for list updates
def listall():
    print("\nAll the Videos")
    for videos in video_list:
        print("Author : ",videos.getAuthor(),", Video : ",videos.getVideo(),", Views : ",videos.getViews(),'\n')
    return 0

# build a function for sending mail to author
def sendMail(msg):
    senderMail = "user@gmail.com"
    password = input("Enter your password : ")
    server = smtplib.SMTP("smtp.gmail.com",587)
    # server.ehlo()
    server.starttls()
    server.login(senderMail,password)
    for videos in video_list:
        if(videos.getViews()==1000 or videos.getViews()==2000 or videos.getViews()==5000):
            server.sendmail(senderMail,videos.email,"Greeting "+videos.author+',\nTo improve the more views.')
    print("Mail send Successfully..\n")
    server.close()
    return 0

# build a function to search a video
def search(word):
    for videos in video_list:
        if word in videos.video:
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
# build
kannan1 = Youtube("Kannan","Intro for Python",2500)
kannan2 = Youtube("Kannan","Advance Python",200)
kannan3 = Youtube("Kannan","Java Basic",500)
kannan4 = Youtube("Kannan","Java Script",8500)
kannan5 = Youtube("Kannan","HTML and CSS",6000)
# appent to list
video_list.append(kannan1)
video_list.append(kannan2)
video_list.append(kannan3)
video_list.append(kannan4)
video_list.append(kannan5)


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
