🎬 CineMatch - Time Based Movie Recommendation System

A smart movie recommendation system that suggests movies based on the time of the day and human psychology. Instead of asking users to search through hundreds of movies, CineMatch recommends suitable genres according to the selected time period and then displays movies from the chosen genre.

🌐 Live Demo

🚀 Try the application here:

CineMatch Live Demo

📌 Project Overview

People often spend more time deciding what to watch than actually watching a movie. CineMatch solves this problem by recommending genres based on common psychological preferences associated with different times of the day.

Time-Based Genre Recommendations
Time	Recommended Genres
🌅 Morning	Motivational, Comedy, Drama
☀️ Afternoon	Action, Adventure, Sci-Fi
🌇 Evening	Romantic, Family, Fantasy
🌙 Night	Horror, Thriller, Mystery

After selecting a genre, the system fetches and displays movies from the movie database.

🎯 Problem Statement

Users often face:

Too many movie choices
Difficulty selecting movies according to their mood
Time wasted browsing streaming platforms

CineMatch provides quick recommendations based on psychological viewing patterns and time of day.

💡 Proposed Solution

The system follows a simple recommendation methodology:

User selects a preferred viewing time.
System suggests suitable genres based on psychological research.
User chooses a genre.
Backend filters movies from the dataset.
Recommended movies are displayed instantly.
⚙️ Methodology
Step 1: Time Selection

The user chooses one of:

Morning
Afternoon
Evening
Night
Step 2: Genre Recommendation

The system maps the selected time to predefined genres.

Step 3: Movie Filtering

Movies are filtered using genre matching from the dataset.

Step 4: Recommendation Display

Relevant movie titles, genres, and descriptions are displayed to the user.

🧠 Algorithm Used
Rule-Based Recommendation System

This project uses a Rule-Based Filtering Algorithm.

Unlike Netflix-style recommendation systems that require user history, CineMatch uses predefined psychological rules.

Example:

Morning → Motivational
Afternoon → Action
Evening → Romantic
Night → Horror
Genre Matching

The backend filters movies using keyword matching in the movie dataset.

motivational → biography, sports, documentary
romantic → romance, love
horror → horror

Movies containing matching genres are recommended to the user.

🛠️ Tech Stack
Frontend
HTML5
CSS3
JavaScript
Backend
Python
Flask
Data Processing
Pandas
Database
CSV Dataset (movies_list.csv)
Deployment
Render
📂 Project Structure
Movie_Recommendation_System/
│
├── static/
│   ├── style.css
│
├── templates/
│   ├── index.html
│
├── movies_list.csv
├── app.py
├── requirements.txt
├── README.md
│
└── screenshots/
📊 Dataset

The project uses a custom movie dataset containing:

Movie Title
Genre
Movie Overview

Example:

Title	Genre	Overview
Rocky	Sports, Drama	Inspirational boxing journey
The Conjuring	Horror, Thriller	Paranormal investigation
Titanic	Romance, Drama	Love story on a doomed ship
✨ Features

✅ Time-based movie recommendations

✅ Psychology-inspired genre suggestions

✅ Clean and responsive user interface

✅ Dark Mode support

✅ Dynamic movie fetching using Flask

✅ Fast recommendations using genre filtering

✅ Easy to use

🚀 Installation
Clone Repository
git clone https://github.com/utkarsh-0106/Movie_Recommendation_System.git
Navigate to Project Folder
cd Movie_Recommendation_System
Install Dependencies
pip install -r requirements.txt
Run Application
python app.py
Open Browser
http://127.0.0.1:5000
📸 Screenshots
Home Page

Add your project screenshots here:

screenshots/homepage.png
Movie Recommendation Page
screenshots/recommendations.png
🔮 Future Improvements
User Rating System
Movie Posters Integration
TMDB API Integration
Personalized Recommendations
Watchlist Feature
Machine Learning Based Recommendation Engine
Mood Detection Based Recommendations
🎓 Academic Relevance

This project demonstrates concepts of:

Recommendation Systems
Human Psychology and User Behavior
Web Development with Flask
Dataset Filtering
Frontend-Backend Integration

It is suitable as a Mini Project for BCA, B.Tech, MCA, or Computer Science students.

👨‍💻 Author

Utkarsh

GitHub:

GitHub Profile

📜 License

This project is developed for educational and learning purposes.
