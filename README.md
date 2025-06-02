# Django Instagram Clone 📸

An Instagram-like social media platform built using **Django**, with core features such as user registration, login, following/unfollowing users, posting content, liking, commenting, messaging (DMs), and searching for users.

## 🔧 Features

### ✅ Authentication

* User registration
* Secure login/logout system
* Redirect unauthenticated users to login page

### 👤 Profile

* View own and others' profile pages
* Follow and unfollow users
* Follower and following counts

### 📸 Posts

* Users can create and view posts
* Like and comment on posts
* View total likes and comments per post



## 🗂 Project Structure

```
instagram_clone/
├── users/               # User registration, login, profile, follow system
├── posts/               # Create/view/like/comment on posts
├── messages_app/        # Direct messages between users
├── templates/           # HTML templates (register, login, profile, inbox, etc.)
├── static/              # Static files (CSS, JS)
├── db.sqlite3           # SQLite database
├── manage.py
└── README.md
```

## 🛠️ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/instagram-clone.git
   cd instagram-clone
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

7. **Open in browser**

   ```
   http://127.0.0.1:8000/
   ```

## 🧪 Sample Features in Action

* Sign up and log in to your account
* Create a post and see it on the home page
* Visit another user's profile and follow them
* Like/comment on posts
* Use the search modal to find users and send DMs

## ✨ To-Do / Upcoming Features

* User stories (reels/shorts)
* Notification system
* Comment threading
* Message read/unread status
* Media uploads (with cloud support)
* Responsive mobile UI

## 📌 Technologies Used

* **Backend:** Django
* **Frontend:** HTML, CSS, JS (vanilla, optionally React in future)
* **Database:** SQLite (default, can be switched to PostgreSQL)
* **Auth:** Django’s built-in auth system

## 🤝 Contributing

Contributions are welcome! Fork the repo and submit a pull request.


