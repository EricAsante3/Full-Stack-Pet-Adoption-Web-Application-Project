# CSE2102-fall24-Team51

Eric Asante eoa21004<br>
Kyle Kirejczyk kek20009<br>
Ishayu Ray isr21011<br>
Kunal Bagga kub21001<br>

Link to Trello: [https://trello.com/b/j8t0Ulvk/group-51-jira-kaban-board](https://trello.com/b/j8t0Ulvk/group-51-jira-kaban-board)<br>
Link to Figma Prototype: [https://www.figma.com/design/mKMWW1sIOVpuQKOlapBINQ/ishayu.ray](https://www.figma.com/design/mKMWW1sIOVpuQKOlapBINQ/ishayu.ray)<br>

Terminal commands to run DOCKERIZED API:<br>
# Make sure you cd into Backend folder.<br>
1. docker build -f docker_files/Dockerfile -t team51-backend .<br>
2. docker run -d -p 5000:5000 team51-backend<br>
3. pytest
