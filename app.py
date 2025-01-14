from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)

# Load movie dataset
try:
    movies_list_df = pd.read_csv('movies_list.csv')
    print("Movies dataset loaded successfully.")
except Exception as e:
    print("Error loading movies dataset:", e)
    movies_list_df = pd.DataFrame()  # Create an empty DataFrame to prevent app crash

@app.route('/')
def index():
    if not movies_list_df.empty:
        movies_list = movies_list_df.to_dict(orient='records')
        return render_template('index.html', movies=movies_list)
    else:
        return "Movies dataset could not be loaded.", 500

@app.route('/recommend', methods=['POST'])
def recommend_movies():
    data = request.json
    genre = data.get('genre')

    if not genre:
        return jsonify({'error': 'Please provide a genre'}), 400

    # Filter movies based on the genre
    filtered_movies = movies_list_df[
        movies_list_df['genres'].str.lower().str.contains(genre, na=False)
    ]

    if filtered_movies.empty:
        return jsonify({'movies': []})

    recommended_movies = filtered_movies[['title', 'genres', 'overview']].to_dict(orient='records')
    return jsonify({'movies': recommended_movies})

if __name__ == '__main__':
    app.run(debug=True)
