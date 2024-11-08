# Link to Trello: 
https://trello.com/b/j8t0Ulvk/group-51-jira-kaban-board

###

# Link to Figma:
https://www.figma.com/design/mKMWW1sIOVpuQKOlapBINQ/ishayu.ray



###
###
###

# Starting the Database.
1.  The Dockerfile in the Backend folder populates the database. 
    **MAKE SURE YOU ARE IN THE BACKEND FOLDER IN YOUR TERMINAL!** 

2.  Use this command below to build the image 
    
    **docker build -f Dockerfile -t team51_backend .**

3. Then run the docker together with this command
   
   **docker run -p 5000:5000 team51_backend**


     