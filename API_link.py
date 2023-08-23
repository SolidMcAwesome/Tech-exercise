import pip._vendor.requests as requests
import json # for testing
import random

class connection():
    def __init__(self):
        self.link = "https://jsonplaceholder.typicode.com/" # Remote API link
        
        # below are varibles used throughout the api
        self.postid = ""
        self.posts = "" # extended link for posts
        self.post = "" # extended link for a chosen post
        self.linkPostComments = "" # extended link for a chosen post's comments
        self.allPosts = "" # list of all 10 random posts
        self.postComments = "" # list of all the comments under a chosen post
        

    def connect(self):
        self.posts = self.link + "posts" # Contains all the posts
        self.post = self.posts + "/" + self.postid # Contains a single post identified using postid
        self.linkPostComments = self.link + "comments?postId=" + self.postid # Contains all the comments for a specified post

        
    def printBold(self, text): # extra utilitises added to make the interface more readable
        boldStart = '\033[1m'
        boldEnd = '\033[0m'
        print(boldStart + text + boldEnd) # makes the text bold    
        
    def print(self, New): # used to display 10 random posts
        if New: # used when a random set of posts are needed
            temp = requests.get(self.posts) # stores all the posts received from the api
            answer = temp.json() # converts
            n = 10 # number of posts wanted
            self.allPosts = random.sample(answer,n) # selects 10 random posts and stores them for later use
        allposts = self.allPosts # assigns the stored posts to a local variable
        postNBR = 1 # counter used to help the user select a post
        for var in allposts:
            print(str(postNBR) + ": " + var["title"]) # displays the title of each post with an index
            postNBR = postNBR + 1
                

    def viewPost(self, postID): # used to view a chosen post
        print("\n") # newline
        count = 1 # indexing
        for var in self.allPosts: # finds the chosen post using the given index and displays it's body
            if postID == count:
                title = var["title"]
                self.printBold(title)
                print(var["body"])
            count = count + 1
        
    
    def viewComments(self, postID): # used to view a chosen post's comments
        print("\n")
        self.printBold("Comments:")
        count = 1 # index for finding post in list
        for var in self.allPosts:
            if postID == count:
                self.postid = str(var["id"]) # saves the postid found using the index
                break
            count = count + 1
            
        self.connect() # reconnects to the remote api to update the chosen post and its comments
        t_comments = requests.get(self.linkPostComments) # retrieves the comments
        comments = t_comments.json() # converts
        self.postComments = comments # stores the comments so it can be used later
        for var in comments: # prints the name/title (in bold) and body/content of each comment on the post
            name = var["name"]
            self.printBold(name)
            print(var["body"] + "\n")
        
    def addComment(self, postID):
        newComments = self.postComments # retrieves the comments
        # the following allows the user to input the parameters required for a comment
        id = input("\nEnter userID: ")
        name = input("Enter Title: ")
        # note - could get email from userid
        email = input("Enter Email: ")
        c = input("Enter Comment: ")
        
        body = "" # body of the new comment
        while c != "": # loop used to allow user to input multiple lines in their comment, loop ends when a new line has no characters
            body += c
            body += "\n"
            c = input()
        end = len(body) - 1 
        body = body[0:end] # removes excess \n 
        
        comment = {'postId': postID, 'id': id, 'name': name, 'email': email, 'body': body} # creates the new comment
        newComments.append(comment) # adds the new comment to the list of comments
        self.postComments = newComments # stores the new comments
        self.printBold("Comments:")
        for var in self.postComments: # display the new list of comments for the chosen post
            name = var["name"]
            self.printBold(name)
            print(var["body"] + "\n")
            
        # the following is used to update the remote api
        headers = {'Content-Type': 'application/json'}
        update = requests.post(self.linkPostComments, json = self.postComments, headers = headers) # post creates a new resource in the link provided
        # print(update.status_code) # testing - error code 201 received consistantly

        
        