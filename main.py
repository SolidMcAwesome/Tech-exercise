'''
Created by Tise Olayinka
Date Modified: 23 Aug 2023
Time Spent: 3-4 hours
Content:
A tech exercise for the final stage of an interview
Purpose:
Listed below in the following comments
'''
'''
    To Do
List a random 10 ‘posts’ from those on the remote API - done
Allow the user to choose one of the posts to view - done
Allow the user to view the comments on that post, and post their own comment (the API fakes the actual post) - done
Bonus: a cool feature we haven’t thought of - refresh - done
    Deliverables
Working code and tests (send us a git bundle or link to your GitHub with commit history)
Include a Readme.md with instructions to run your application and tests
We expect you to only spend a few hours on this - less is more!
    Notes
Clean, simple, maintainable code
Security conscious work
Carefully chosen libraries
Good unit test coverage and mocks
Good documentation
Well structured commit history with messages

'''

from API_link import connection # Connects to remote API

def authenticateInput(inpuType, input): # for validating inputs, can be expanded for different input types
    if inpuType == "int":
        try:
            integer = int(input)
            if (integer < 11 and integer > 0): # used to make sure user only selects numbers 1 to 10
                return True
        except:
            pass
    else:
        pass
    return False

def main():
    api = connection() 
    api.connect() # makes the connection
    newPosts = True # used to decide if posts will be refreshed
    
    menuLoop = True # loops interface
    while(menuLoop):
        print("\nSelect a post(1 to 10):\n(r) to refresh (e) to exit\n")
        api.print(newPosts) # shows 10 random posts
        query = input("\n>: ")
        if query == "r": # if user enters r, new posts are generated
            newPosts = True
        elif query == "e":
            menuLoop = False
        else:
            viewingPost = authenticateInput("int", query) # makes sure the input is in the specified range
            if viewingPost == False:
                newPosts = False
            postID = query # used to identify which post was chosen
            while(viewingPost): # looping the post being viewed
                api.viewPost(int(postID)) # opens up the selected post
                postMenu = input("\nOpen Comments (c)\nGo Back to Posts (b)\n>: ")
                if postMenu == "b": # goes back to the list of 10 posts
                    newPosts = False
                    viewingPost = False
                elif postMenu == "c": # opens up the comments for the chosen post
                    viewingComments = True
                    api.viewComments(int(postID))
                    while viewingComments:
                        commentMenu = input("Add Comment (a)\nGo Back to Post (b)\n>:")
                        if commentMenu == "a": # adds a comment to the post
                            api.addComment(postID)
                        elif commentMenu == "b": # goes back to the chosen post
                            viewingComments = False

if __name__ == "__main__":
    main() # launches main()