# Define a class for YouTube video. 
# decide the properties and functions based on the questions below.
# 
# List all the videos recorded by author "Kannan"
# List all the videos with more than 1K views
# Change the author of all the videos recorded by "Kannan" to "Kannan D."
# 20 students watched Kannan's "Intro to Python" video today. Update the videos views and print the total views for this video.
# 
# 


# build a function for get videos based on authoe name
def getVideos(author):
    print("Videos recorded by author",author)
    for videos in video_list:
        if(videos.getAuthor()==author):
            print(videos.getVideo())
    print()
# build a function for filter videos based on view
def filterView(views):
    print("Videos with more than ",views," views")
    for videos in video_list:
        if(videos.getViews()>views):
            print(videos.getVideo())
    print()
# build a function for chage author name
def changeAuthor(old_author,new_author):
    for videos in video_list:
        if(videos.getAuthor()==old_author):
            videos.setAuthor(new_author)
# build a function for add views based on video
def addViews(video,views):
    for videos in video_list:
        if(videos.getVideo()==video):
            videos.setViews(videos.getViews()+views)
# build a function for list updates
def listall():
    print("\nAll the Videos")
    for videos in video_list:
        print("Author : ",videos.getAuthor(),", Video : ",videos.getVideo(),", Views : ",videos.getViews())

# youtube class
class Youtube:
    # constructor
    def __init__(self,author,video,views):
        self.author = author
        self.video = video
        self.views = views

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


# List all the videos recorded by author "Kannan"
getVideos("Kannan")
# List all the videos with more than 1K views
filterView(1000)
# Change the author of all the videos recorded by "Kannan" to "Kannan D."
changeAuthor("Kannan","Kannan D")
# 20 students watched Kannan's "Intro to Python" video today. Update the videos views and print the total views for this video.
addViews("Intro for Python",20)
# list all the detials
listall()