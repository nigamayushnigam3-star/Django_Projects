# 🐍 Django Projects

A collection of Django projects built using **Function Based Views**, **Model Forms**, and **Django ORM**.

---

## 📁 Projects

### 1. 📸 Django Image Uploader (`Project/`)

A simple Django project that allows users to upload images using **Django Model Forms**. Uploaded images are stored in the database through Django's **ORM**, while the image files are saved in the configured media directory.

#### 🚀 Features
* Upload images using Django Model Forms
* Store image information using Django ORM
* Save uploaded files in the media folder
* Display uploaded images on the webpage
* Simple and beginner-friendly project structure

#### 📂 Project Structure
```text
Project/
├── app/
├── media/
├── templates/
├── manage.py
└── db.sqlite3
```

---

### 2. 🗃️ Django CRUD Project (`CRUD_Project/`)

A Function Based View CRUD project that allows users to **Add**, **Update**, and **Delete** student records using **Django Model Forms** and **Django ORM**.

#### 🚀 Features
* Add new student records using Django Model Forms
* Display all student records in a table
* Update existing student records
* Delete student records
* Clean and responsive UI with Bootstrap

#### 📂 Project Structure
```text
CRUD_Project/
├── CRUD_Project/
├── crud/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── manage.py
└── db.sqlite3
```

---

## 🛠️ Technologies Used

* Python
* Django
* HTML
* CSS
* Bootstrap
* SQLite (Default Django Database)

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/nigamayushnigam3-star/Django_Projects.git
```

### 2. Navigate to the Project Directory

```bash
cd Django_Projects/Project      # for Image Uploader
cd Django_Projects/CRUD_Project # for CRUD Project
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install django
```

### 6. Apply Migrations

```bash
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:
```
http://127.0.0.1:8000/
```

---

## 📚 Concepts Covered

* Django Models
* Django Model Forms
* Django ORM
* Function Based Views
* CRUD Operations
* File Upload Handling
* Media Files Configuration
* Templates & Template Inheritance
* URL Routing
* Database Integration

---

## 👨‍💻 Author

**Ayush Nigam**

If you found this helpful, consider giving it a ⭐ on GitHub!
