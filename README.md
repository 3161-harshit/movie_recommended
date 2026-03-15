# 🎬 Movie Recommendation System

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Recommendation%20System-green)
![NLP](https://img.shields.io/badge/NLP-Text%20Processing-orange)
![License](https://img.shields.io/badge/License-MIT-red)

A **Content-Based Movie Recommendation System** built using **Python and Machine Learning**.
The system recommends movies similar to the movie selected by the user by analyzing features such as **genres, cast, keywords, and movie overview**.

This project demonstrates how **Natural Language Processing (NLP)** and **similarity algorithms** can be used to build an intelligent recommendation engine similar to those used by modern streaming platforms.

---

# 📌 Project Overview

Recommendation systems are widely used by platforms such as:

* Netflix
* Amazon
* YouTube

These platforms use recommendation algorithms to **suggest personalized content to users**.

This project implements a **content-based filtering approach** to recommend movies based on similarity.

---

# 🚀 Features

✔ Content-based movie recommendations
✔ Cosine similarity ranking
✔ Data preprocessing and feature engineering
✔ Simple user interface
✔ Built using Python data science libraries

---

# 🧠 System Architecture

```
User Input (Movie Name)
        ↓
Data Preprocessing
        ↓
Feature Extraction
        ↓
Vectorization
        ↓
Similarity Calculation
        ↓
Top 5 Movie Recommendations
```

---

# ⚙️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-learn

### Framework

* Streamlit

### Dataset

Movie dataset from
Kaggle

---

# 📊 Methodology

## 1️⃣ Data Collection

The system loads movie datasets containing information such as:

* Movie title
* Genres
* Cast
* Keywords
* Overview

Example:

```python
movies = pd.read_csv("movies.csv")
credits = pd.read_csv("credits.csv")
```

---

## 2️⃣ Data Preprocessing

Cleaning and preparing the dataset:

* Removing null values
* Merging datasets
* Selecting important columns

```python
movies = movies.merge(credits, on='title')
movies.dropna(inplace=True)
```

---

## 3️⃣ Feature Engineering

Combining important movie attributes into a **tags column**.

```python
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords']
```

---

## 4️⃣ Vectorization

Converting text data into numerical vectors using **CountVectorizer**.

```python
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000)
vectors = cv.fit_transform(movies['tags']).toarray()
```

---

## 5️⃣ Similarity Calculation

Using **Cosine Similarity** to find similar movies.

```python
from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vectors)
```

Movies with the highest similarity score are recommended.

---

# 🎥 Example

Input:

```
Movie: Batman
```

Output:

```
Recommended Movies:

1. The Dark Knight
2. Batman Begins
3. Joker
4. Man of Steel
5. Justice League
```

---

# ▶️ How to Run the Project

Clone the repository:

```bash
git clone https://github.com/3161-harshit/movie_recommended.git
```

Navigate to the project folder:

```bash
cd movie_recommended
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

# 📈 Future Improvements

Possible enhancements include:

* Hybrid recommendation systems
* Deep learning-based recommendation models
* Real-time recommendation systems
* User preference learning

Advanced systems use tools like:

* TensorFlow
* PyTorch
* Apache Spark

---

# 👨‍💻 Author

**Harshit**
AI & Machine Learning Enthusiast

Student at
Kalinga Institute of Industrial Technology

GitHub
[https://github.com/3161-harshit](https://github.com/3161-harshit)
