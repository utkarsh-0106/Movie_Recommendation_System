# 🎬 CineMatch - Time Based Movie Recommendation System

## 📌 Overview

CineMatch is a movie recommendation system that suggests movies based on the user's preferred time of watching. Unlike traditional recommendation systems that rely on ratings or viewing history, CineMatch uses basic human psychology to recommend suitable movie genres for different times of the day.

The system assumes that people's moods and entertainment preferences change throughout the day. Based on the selected time, the system recommends genres and then suggests movies from the dataset that match those genres.

---

## 🚀 Problem Statement

With thousands of movies available online, users often struggle to decide what to watch.

CineMatch solves this problem by:

- Reducing decision fatigue
- Suggesting genres based on human psychology
- Providing quick movie recommendations
- Making movie selection easier and faster

---

## 💡 Idea Behind the Project

Research suggests that people often prefer different types of content at different times of the day.

| Time of Day | Recommended Genre |
|------------|------------------|
| Morning | Motivational, Biography, Documentary |
| Afternoon | Action, Adventure, Sci-Fi |
| Evening | Romance, Family, Fantasy |
| Night | Horror, Thriller, Mystery |

The system follows this psychology-based mapping to provide recommendations.

---

## ⚙️ Methodology

### Step 1: Time Selection
User selects the preferred movie watching time:
- Morning
- Afternoon
- Evening
- Night

### Step 2: Genre Recommendation
Based on the selected time, the system displays suitable genres.

### Step 3: Genre Selection
User selects one of the suggested genres.

### Step 4: Movie Filtering
The backend filters movies from the dataset based on genre keywords.

### Step 5: Movie Recommendation
Matching movies are displayed with:
- Movie Title
- Genre
- Overview

---

## 🛠️ Technology Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Data Processing
- Pandas

### Dataset
- CSV Dataset (`movies_list.csv`)

---

## 📂 Project Structure

```bash
Movie_Recommendation_System/
│
├── static/
│
├── templates/
│   └── index.html
│
├── movies_list.csv
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

---

## 🔍 Algorithm Used

This project uses a **Rule-Based Recommendation Algorithm**.

### Rule-Based Filtering

The recommendation process follows predefined rules:

```python
Morning → Motivational
Afternoon → Action
Evening → Romantic
Night → Horror
```

The system then filters movies from the dataset using keyword matching on movie genres.

### Genre Matching

Example:

```python
motivational = [
    "biography",
    "sports",
    "documentary",
    "inspirational"
]
```

Movies containing these genres are recommended.

---

## 📊 Features

- Time-based movie recommendations
- Psychology-inspired genre selection
- Fast recommendations
- Dark Mode support
- Responsive UI
- Easy-to-use interface
- CSV-based movie database

---

## 📷 Workflow

```text
User Selects Time
        ↓
Genre Suggestions Displayed
        ↓
User Selects Genre
        ↓
Flask Backend Receives Request
        ↓
Dataset Filtered Using Genre Keywords
        ↓
Recommended Movies Displayed
```

---

## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/utkarsh-0106/Movie_Recommendation_System.git
```

### Move into Project Directory

```bash
cd Movie_Recommendation_System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

## 📁 Dataset Format

The CSV dataset should contain:

| title | genres | overview |
|---------|---------|---------|
| Interstellar | Sci-Fi, Adventure | Space exploration movie |
| The Conjuring | Horror, Thriller | Paranormal investigation |

---

## 🎯 Future Improvements

- User Login System
- Movie Posters using TMDB API
- Personalized Recommendations
- User Ratings and Reviews
- AI-Based Mood Detection
- Hybrid Recommendation System
- Watchlist Feature

---

## 📚 Learning Outcomes

This project helped in understanding:

- Flask Web Development
- Frontend-Backend Integration
- CSV Data Handling
- Recommendation Systems
- Rule-Based Filtering
- Human Psychology in Entertainment

---

## 👨‍💻 Author

**Utkarsh Kumar**

GitHub: https://github.com/utkarsh-0106

---

## 📄 License

This project is developed for educational and academic purposes.
