# 📸 Django Image Uploader

A simple Django project that allows users to upload images using **Django Model Forms**. Uploaded images are stored in the database through Django's **ORM (Object Relational Mapper)**, while the image files are saved in the configured media directory.

---

## 🚀 Features

* Upload images using Django Model Forms
* Store image information using Django ORM
* Save uploaded files in the media folder
* Display uploaded images on the webpage
* Simple and beginner-friendly project structure
* Clean and responsive user interface

---

## 🛠️ Technologies Used

* Python
* Django
* HTML
* CSS
* Bootstrap
* SQLite (Default Django Database)

---

## 📂 Project Structure

```text
ImageUploader/
│── app/
│── media/
│── templates/
│── static/
│── manage.py
│── db.sqlite3
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ImageUploader.git
```

### 2. Navigate to the Project Directory

```bash
cd ImageUploader
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
pip install -r requirements.txt
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

## 📷 How It Works

1. User selects an image from their device.
2. Django Model Form validates the uploaded file.
3. Django ORM stores the image details in the SQLite database.
4. The image file is saved inside the **media/** folder.
5. Uploaded images can be displayed on the website.

---

## 📚 Concepts Covered

* Django Models
* Django Model Forms
* Django ORM
* File Upload Handling
* Media Files Configuration
* Templates
* URL Routing
* Views
* Database Integration

---

## 🎯 Learning Outcome

This project demonstrates how Django handles image uploads using Model Forms and ORM. It provides hands-on experience with file handling, database operations, and media file management, making it an excellent beginner-level Django project.

---

## 👨‍💻 Author

**Ayush Nigam**

If you found this project helpful, consider giving it a ⭐ on GitHub!
