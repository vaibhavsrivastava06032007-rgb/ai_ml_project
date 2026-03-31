# 🎬 Movie Recommendation System

## ❓ Problem Statement

Users often struggle to decide what to watch, especially when they are looking for movies in a specific genre like romance, comedy, or thriller.

> This project solves the problem of quickly recommending movies based on user preferences without manually searching through large datasets.

---

## 🎯 Objectives

- Build a simple movie recommendation system  
- Recommend movies based on user-input genre  
- Handle multiple genres per movie (e.g., "Romance Drama")  
- Maintain a clean and modular project structure  
- Keep the system beginner-friendly  

---

## 📁 Project Structure
movie-recommendation/
│── main.py # Runs the program (user interaction)
│── data_loader.py # Loads and cleans dataset
│── recommender.py # Recommendation logic
│── utils.py # Helper functions (show genres)
│── movies.csv # Movie dataset
│── README.md # Documentation
│── requirements.txt # Dependencies


---

## 📊 Dataset Description

The dataset (`movies.csv`) contains two columns:

| Column | Description |
|--------|------------|
| title  | Movie name |
| genres | One or more genres |

### Example
Titanic,Romance Drama
Avengers,Action Sci-Fi
Frozen,Animation Family


---

## ⚙️ How It Works

1. Load dataset using pandas  
2. Convert genres into lowercase  
3. Split genres into lists  
   - `"Romance Drama"` → `["romance", "drama"]`  
4. User inputs a genre  
5. System filters movies containing that genre  
6. Displays:
   - List of movies  
   - One random suggestion  

---

## 🧠 Approach

- Used **pandas** for reading CSV data  
- Cleaned and transformed genre data  
- Implemented filtering using list matching  
- Used modular design for clarity and scalability  

---

## 🔑 Key Concepts Used

- Python basics  
- Functions and modular programming  
- File handling (CSV)  
- Pandas for data processing  
- List operations and filtering  
- User input handling  
- Random selection  

---

## 💡 Example Usage
🎬 Movie Recommender System

Available genres:

action
comedy
romance
thriller

Enter a genre: romance

Movies you can watch:

Titanic
The Notebook
La La Land

👉 Suggested for you: Titanic


---

## ▶️ How to Run



## ⚠️ Limitations

- ❌ No machine learning used  
- 👤 No personalization (same results for all users)  
- 📉 Limited dataset compared to real-world systems  
- 🎭 Only genre-based recommendation  
- 💻 Command-line interface only (no GUI)

## 🚀 Future Improvements

- 🔍 Recommend based on movie name (content-based filtering)  
- 🤖 Add machine learning algorithms  
- 🌐 Build web application (Flask / Streamlit)  
- ⭐ Add user ratings and reviews  
- 📈 Expand dataset for better accuracy  
- 🧠 Add smart matching (e.g., "romantic" → "romance")

  ## 📚 What I Learned

- 🏗️ Structuring Python projects  
- 📊 Working with datasets using pandas  
- 🧹 Cleaning and transforming data  
- 🎭 Handling multi-genre data  
- 🤖 Building a basic recommendation system  
- ✍️ Writing modular and maintainable code

  ## 🧩 Challenges Faced

### 1. Genre Matching Issue

**Problem:**
Romance Drama → romancedrama


This caused matching failures when users typed `"romance"`.

**Solution:**
Split genres into lists.

---

### 2. Limited Dataset

**Problem:**
Earlier dataset had fewer genres, causing:


"No results found"



**Solution:**
Expanded dataset with more genres and combinations.

---

## 🙌 Acknowledgment

This project was developed as a beginner-level implementation to understand the fundamentals of recommendation systems.

---

### 📌 Optional Enhancements

If you'd like to improve this project further, you can:

- 🏷️ Add badges (GitHub stats, Python version, etc.)  
- 💼 Make it more professional for your portfolio  
- 🖼️ Convert it into a GitHub-ready README with screenshots  
