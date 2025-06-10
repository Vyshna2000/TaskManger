🗂️ Task Manager Web Application
A simple and user-friendly web application to manage daily tasks efficiently. Users can register, log in, and manage tasks with due dates, priorities, and statuses.

🔧 Tech Stack
Backend: Django, Python

Database: SQLite

Frontend: HTML, CSS, Bootstrap

✨ Key Features
🔐 User Authentication
Secure login and signup system.

Separate access for admin and normal users.

📝 Task Management (CRUD)
Add, update, delete, and view daily tasks.

📅 Due Dates & ⏫ Priorities
Set deadlines for tasks.

Assign priority levels (Low, Medium, High).

📊 Task Status Tracking
Mark tasks as Pending, In Progress, or Completed.

📸 Screenshots


🚀 Getting Started
Follow these steps to run the project locally:

# 1. Clone the repository
git clone  https://github.com/Vyshna2000/TaskManger/
cd task-manager

# 2. Set up a virtual environment
python3 -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create a superuser (optional)
python manage.py createsuperuser

# 6. Start the server
python manage.py runserver
Visit http://127.0.0.1:8000 in your browser.

🤝 Contributions
Contributions are welcome!
You can fork the repo, work on a new feature, and open a pull request.

