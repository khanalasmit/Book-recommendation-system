# 📚 Book Recommendation System

A hybrid recommendation system combining **popularity-based** and **collaborative filtering** approaches to provide intelligent book recommendations. Includes a Flask web application for easy access.

**🌐 Live Demo**: https://book-recommendation-system-6-bpey.onrender.com/

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Website Features](#website-features)
- [Algorithms](#algorithms)
- [Performance](#performance)
- [License](#license)

---

## Overview

This project implements a book recommendation engine that discovers books users are likely to enjoy. It processes 1.1M ratings from 278K users across 271K books, using two recommendation strategies:

1. **Popularity-Based**: Identifies trending books with high ratings
2. **Collaborative Filtering**: Recommends similar books based on rating patterns

The system filters data to focus on 1,949 active users (200+ ratings) and 706 famous books (50+ ratings).

---

## Features

✅ **Dual Recommendation Approach** - Popularity-based + Collaborative filtering  
✅ **Live Web Application** - Deployed on Render, accessible anywhere  
✅ **Efficient Processing** - Memory-mapped files & batch computation  
✅ **Fast Recommendations** - 5-10ms per query  
✅ **Scalable Architecture** - Handles large datasets efficiently  

---

## Installation

### Prerequisites
- Python 3.7+
- pip package manager

### Local Setup

```bash
# Install dependencies
pip install pandas numpy scikit-learn flask jupyter

# Clone repository
git clone https://github.com/khanalasmit/Book-recommendation-system.git
cd BookRecommendationSystem

# Place CSV files in project directory
# - Books.csv
# - Ratings.csv
# - Users.csv

# Run Jupyter notebook to generate pickle files
jupyter notebook 1.IPYNB

# Run Flask app
cd flaskenc
python app.py
```

Access the website at `http://localhost:5000`

### Live Website
Visit: **https://book-recommendation-system-6-bpey.onrender.com/**

---

## Project Structure

```
BookRecommendationSystem/
├── 1.IPYNB                          # Main analysis notebook
├── Books.csv, Ratings.csv, Users.csv # Dataset
├── flaskenc/
│   ├── app.py                       # Flask application
│   ├── popular.pkl, pt.pkl, similarity.pkl, books.pkl
│   └── templates/
│       ├── index.html               # Home page
│       └── recommend.html           # Recommendation page
└── readme.md
```

---

## Usage

### In Jupyter Notebook

```python
# Popularity-based recommendations
popular_books = popularity_df[popularity_df['Num-Ratings'] > 250]\
    .sort_values('Book-Rating', ascending=False)
print(popular_books.head(10))

# Collaborative filtering
recommend('1984', top_n=5)
```

### On Website

1. **Home Page** (`/`) - Browse top 50 popular books with ratings and cover images
2. **Recommend Page** (`/recommend`) - Search for a book and get 5 similar recommendations
3. **Navigation** - Easy links between Home, Recommend, and Contact pages

---

## Website Features

### 🏠 Home Page
- **Display**: Top 50 trending books filtered by 250+ ratings
- **Information**: Book title, author, number of ratings, average rating
- **Design**: Bootstrap grid layout with book covers, dark theme with green accent
- **Purpose**: Quick discovery of popular books without any search

### 📖 Recommendation Page
- **Search**: Text input to search for any book in the dataset
- **Results**: Top 5 similar books with similarity scores (0-1 range)
- **Error Handling**: Clear error message if book not found in dataset
- **Design**: Clean form with organized results display
- **Example Search**: Try "1984", "The Hobbit", "Harry Potter"

### 🎨 User Interface
- **Color Scheme**: Black background with green (#00a65a) accents
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Bootstrap 3**: Professional styling and smooth components
- **Navigation Bar**: Easy access to all pages with hover effects
- **Book Covers**: Display book images from dataset for visual appeal

### 📱 Mobile Optimized
- Fully responsive layout
- Touch-friendly buttons and inputs
- Fast loading times
- Works on all devices

---

## Algorithms

### Popularity-Based Filtering
```python
# Filter books with 250+ ratings, sort by average rating
popular_books = popularity_df[popularity_df['Num-Ratings'] > 250]\
    .sort_values('Book-Rating', ascending=False)
```
**Best for**: New users, discovering trending books  
**Algorithm**: Rating average + number of votes

### Item-Based Collaborative Filtering
```python
# Create pivot table (Books × Users)
pt = final_ratings.pivot_table(index='Book-Title', columns='User-ID', values='Book-Rating')

# Compute cosine similarity with batch processing
sim = cosine_similarity(pt.values)

# For query book, return top-k similar books
def recommend(book_name, top_n=5):
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(sim_matrix[index])), 
                          key=lambda x: x[1], reverse=True)[1:top_n+1]
    return similar_items
```
**Metric**: Cosine Similarity (0-1 range)  
**Best for**: Personalized recommendations based on user rating patterns

---

## Performance

### Memory Efficiency
- ❌ Original: 155,845 books = 181 GB RAM needed
- ✅ Optimized: 706 books = 2 MB RAM

### Speed
- Data processing: 2-5 seconds
- Similarity computation: 300-500 ms
- Single recommendation: 5-10 ms
- Website response time: < 200ms

### Dataset Stats
| Metric | Value |
|--------|-------|
| Total Books | 271,360 |
| Total Ratings | 1,149,780 |
| Active Users | 1,949 |
| Famous Books (analyzed) | 706 |
| Memory Usage | 2 MB |

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Backend | Flask, Python |
| Frontend | HTML5, Bootstrap 3, CSS |
| Data Science | Pandas, NumPy, Scikit-learn |
| Analysis | Jupyter Notebook |
| Deployment | Render |
| Database | Pickle (serialized Python objects) |

---

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open Pull Request

---

## License

MIT License - see LICENSE file for details

---

## Citation

```bibtex
@software{bookrec2025,
  author = {Khan, Asmit},
  title = {Book Recommendation System},
  year = {2025},
  url = {https://github.com/khanalasmit/Book-recommendation-system}
}
```

---

## Contact

- **GitHub**: [@khanalasmit](https://github.com/khanalasmit)
- **Live Website**: https://book-recommendation-system-6-bpey.onrender.com/
- **Issues**: [GitHub Issues](https://github.com/khanalasmit/Book-recommendation-system/issues)

---

**Status**: ✅ Production Ready | **Deployment**: Render | **Last Updated**: November 2025