# 🏨 Booking / Reservation System (Django)

A simple **Booking / Reservation System** built with **Django**.  
This project is designed for learning Django fundamentals and working with a real-world project structure.

Users can register, log in, and create reservations.  
An admin panel is available for managing users and reservations.

---

## 🚀 Features
- User authentication (login & signup)
- Create and view reservations
- Django Forms for handling user input
- Admin panel for managing bookings
- Clean and simple project structure

---

## 🛠 Tech Stack
- Python 3.x
- Django
- SQLite (default database)
- Django Templates (HTML / CSS)

---

## ⚙️ Getting Started

Follow the steps below to run the project on your local machine.

---

### 1️⃣ Clone the repository
```bash
git clone https://github.com/arshia-iz/booking.git
cd booking
2️⃣ Create a virtual environment
bash
Copy code
python -m venv venv
Activate it:

Windows

bash
Copy code
venv\Scripts\activate
Linux / macOS

bash
Copy code
source venv/bin/activate

3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt

4️⃣ Apply database migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate

5️⃣ Create a superuser (optional)
bash
Copy code
python manage.py createsuperuser

6️⃣ Run the development server
bash
Copy code
python manage.py runserver
Open your browser and visit:

cpp
Copy code
http://127.0.0.1:8000/
Admin panel:

arduino
Copy code
http://127.0.0.1:8000/admin/
📂 Project Structure
csharp
Copy code
booking/
│── core/          # Project settings
│── expense/          # Main app (booking & reservations)
│── templates/        # HTML templates
│── static/           # Static files
│── manage.py
│── requirements.txt
│── db.sqlite3
❗ Notes
SQLite is used as the default database.

No environment variables are required.

This project is intended for learning and educational purposes.

🤝 Contributing
You are welcome to fork this repository and submit pull requests.

📜 License
This project is licensed under the MIT License.