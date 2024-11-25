# Group 51 Dockerized Fullstack Pet WebApp Setup

## **Links**
- **Group Project Video Link**: [Group 51 Kanban Board](https://youtu.be/wL0esWZsHKM)  
- **Trello Board**: [Group 51 Kanban Board](https://trello.com/b/j8t0Ulvk/group-51-jira-kaban-board)  
- **Figma Design**: [Group 51 Figma prototype](https://www.figma.com/design/mKMWW1sIOVpuQKOlapBINQ/ishayu.ray)

---

## **Steps to Run Dockerized WebApp**

**Note**: Ensure you are in the `../cse2102-fall24-Team51/` directory while running these commands.

### **Backend Setup**:

1. **Build the Backend Docker Image**:
   ```bash
   docker build -f Backend/docker_files/Dockerfile -t team51-backend .

2. **Run Backend with terminal command (Backend runs on port 5170)**:
   ```bash
   docker run -d -p 5170:5000 team51-backend
   
3. **Build the Frontend Docker Image**:
   ```bash
   docker build -f Frontend/docker_files/Dockerfile -t team51-frontend .
   
4. **Run Frontend with terminal command (Frontend runs on port 5173)**:
   ```bash
   docker run -d -p 5173:5173 team51-frontend
   
5.  **The WebApp should now be visable at "http://localhost:5173/"**:
