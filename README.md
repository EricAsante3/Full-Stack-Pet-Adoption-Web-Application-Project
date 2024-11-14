# CSE2102-fall24-Team51

Eric Asante eoa21004<br>
Kyle Kirejczyk kek20009<br>
Ishayu Ray isr21011<br>
Kunal Bagga kub21001<br>

Link to Trello: [https://trello.com/b/j8t0Ulvk/group-51-jira-kaban-board](https://trello.com/b/j8t0Ulvk/group-51-jira-kaban-board)<br>
Link to Figma Prototype: [https://www.figma.com/design/mKMWW1sIOVpuQKOlapBINQ/ishayu.ray](https://www.figma.com/design/mKMWW1sIOVpuQKOlapBINQ/ishayu.ray)<br>

# Terminal commands to run DOCKERIZED API:<br>
Make sure you cd into Backend folder.<br>
1. docker build -f docker_files/Dockerfile -t team51-backend .<br>
2. docker run -d -p 5000:5000 team51-backend<br>
3. pytest


# How to run frontend application: <br>
Separate terminals will be needed. <br>
1. python3 app.py <br>
2. python3 initdatabase.py <br>
3. python3 databasefunctions.py <br>
4. cd Frontend, cd recat-app-team51, nvm run dev <br>
5. interact with the screens! <br>

The sign up screen redirects to the login screen, and the login screen redirects to a placeholder homepage. <br>
There are buttons on both the sign up screen and login screen that take you back to the other page. <br>