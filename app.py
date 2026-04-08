from flask import Flask, request, jsonify, render_template
import pandas as pd
import os

app = Flask(__name__)

# Load movie dataset safely
CSV_FILENAME = 'movies_list.csv'

try:
    file_path = os.path.join(os.path.dirname(__file__), CSV_FILENAME)
    if os.path.exists(file_path):
        # 🔥 on_bad_lines='skip' handles the "Expected 3 fields, saw 4" error
        # encoding='utf-8' handles special characters in movie titles
        movies_list_df = pd.read_csv(file_path, on_bad_lines='skip', encoding='utf-8')
        
        if not movies_list_df.empty:
            print(f"✅ {CSV_FILENAME} loaded successfully. Found {len(movies_list_df)} movies.")
        else:
            print(f"⚠️ {CSV_FILENAME} loaded but it appears to be empty.")
    else:
        print(f"❌ {CSV_FILENAME} NOT FOUND at {file_path}")
        movies_list_df = pd.DataFrame()
except Exception as e:
    print(f"❌ Error loading movies dataset: {e}")
    movies_list_df = pd.DataFrame()

@app.route('/')
def index():
    if not movies_list_df.empty:
        movies_list = movies_list_df.to_dict(orient='records')
        # This requires a folder named 'templates' with 'index.html' inside
        return render_template('index.html', movies=movies_list)
    else:
        return f"<h1>Error</h1><p>Dataset '{CSV_FILENAME}' could not be loaded or is empty.</p>", 500

@app.route('/recommend', methods=['POST'])
def recommend_movies():
    try:
        data = request.get_json()
        genre = data.get('genre', '').lower()

        if not genre:
            return jsonify({'error': 'Please provide a genre'}), 400

        if movies_list_df.empty:
            return jsonify({'error': 'Database is empty'}), 500

        filtered_movies = movies_list_df[
            movies_list_df['genres'].str.lower().str.contains(genre, na=False)
        ]

        recommended_movies = filtered_movies[['title', 'genres', 'overview']].to_dict(orient='records')
        return jsonify({'movies': recommended_movies})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
