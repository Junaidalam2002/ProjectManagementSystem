# Project Management System

PMS is a lightweight project management system built using Django, SQLite, and HTML with Tailwind CSS. It's designed to help you stay organized, collaborate with your team, and boost productivity. Whether you're managing personal tasks or coordinating a team project, TaskFlow has you covered.

## Features

### 1. Task Lists (To-Do Lists)
- Create task lists for different projects or categories.
- Add tasks with due dates, priorities, and descriptions.
- Mark tasks as complete or pending.

### 2. Notes and Documentation
- Maintain project-specific notes, meeting minutes, and brainstorming sessions.
- Use rich-text formatting (bold, italic, bullet points) for clarity.
- Organize notes into folders or tags.

### 3. Attachments and Files
- Attach files directly to tasks or notes.
- Supported file types: documents (Word, PDF), images, spreadsheets, etc.
- Version control for attachments.

### 4. Project Dashboard
- Visualize project progress with charts and graphs.
- Overview of pending tasks, completed tasks, and milestones.
- Project health indicators (e.g., overdue tasks, resource allocation).

## Getting Started

1. **Clone the Repository:**
   ```
   git clone https://github.com/Junaidalam2002/ProjectManagementSystem
   cd ProjectManagementSystem
   ```

2. **Create a Virtual Environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run Migrations:**
   ```
   python manage.py migrate
   ```

5. **Login as (Admin):**
   ```
   Email : example@gmail.com
   Password : 1234
   ```

6. **Start the Development Server:**
   ```
   python manage.py runserver
   ```

7. Open your browser and visit [http://localhost:8000/](http://localhost:8000/)
