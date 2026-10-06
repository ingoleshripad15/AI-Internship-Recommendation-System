# AI Internship Recommendation System

An AI-based web application that recommends relevant internships based on a user's skills, interests, and preferred domain. The system uses Natural Language Processing (NLP) and content-based recommendation to calculate internship relevance and display the best matching opportunities.

## Features

- User login and registration using MySQL
- Internship recommendation based on user skills and domain
- TF-IDF based text feature extraction
- Cosine similarity for internship matching
- Location and mode-based internship filtering
- Match scores for recommended internships
- Internship details and recommendation results pages
- MySQL database integration
- FastAPI backend with HTML, CSS, and JavaScript frontend
- Responsive and user-friendly web interface

## Technology Stack

### Programming Languages
- Python
- HTML
- CSS
- JavaScript
- SQL

### Backend
- FastAPI
- Uvicorn
- Jinja2

### Machine Learning
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- Natural Language Processing

### Database
- MySQL
- MySQL Connector/Python

### Development Tools
- Jupyter Notebook
- VS Code
- Git
- GitHub

## Project Architecture

```text
AI-Internship-Recommendation-System/
│
├── data/
│   └── internship_data.csv
│
├── sql/
│   └── login_database.sql
│
├── static/
│   ├── details_page.css
│   ├── hero-bg.jpg
│   ├── new_styles.css
│   ├── result_page.css
│   └── script.js
│
├── templates/
│   ├── new_details_page.html
│   ├── new_home_page.html
│   └── new_result_page.html
│
├── main.py
├── MLrecommendation.py
├── Recommendation_model.ipynb
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## How It Works

The recommendation process follows these steps:

1. The user enters their email and login information.
2. The user provides their preferred internship domain and skills.
3. The system combines internship title, domain, skills, and description into text features.
4. TF-IDF converts the text data into numerical feature vectors.
5. Cosine similarity compares the user's profile with available internships.
6. The system calculates a relevance score for each internship.
7. Matching internships are filtered according to the user's preferences.
8. The highest-scoring internships are displayed as recommendations.

## Machine Learning Approach

This project uses a **content-based recommendation approach**.

### TF-IDF

TF-IDF (Term Frequency-Inverse Document Frequency) converts internship-related text into numerical vectors by assigning importance to words based on their frequency and occurrence across documents.

The model uses information from:

- Internship title
- Domain
- Skills
- Internship description

### Cosine Similarity

Cosine similarity measures the similarity between the user's profile vector and each internship vector.

A higher similarity score indicates that the internship content is more relevant to the user's selected skills and interests.

## Database

MySQL is used to store user login and application-related information.

The SQL database setup is provided in:

```text
sql/login_database.sql
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Internship-Recommendation-System.git
cd AI-Internship-Recommendation-System
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root.

Use `.env.example` as a template:

```env
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=internship_db2
```

Do not upload the `.env` file to GitHub because it contains database credentials.

### 5. Configure MySQL

Create the required MySQL database and tables using:

```text
sql/login_database.sql
```

Make sure the database name in `.env` matches the database configured in MySQL.

## Running the Application

From the project root, activate the virtual environment and run:

```bash
uvicorn main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

Open the address in a web browser.

## Project Workflow

```text
User
  ↓
Login / Registration
  ↓
Enter Skills and Internship Preferences
  ↓
FastAPI Backend
  ↓
Recommendation Engine
  ↓
TF-IDF Vectorization
  ↓
Cosine Similarity
  ↓
Internship Matching
  ↓
Filter by Preferences
  ↓
Ranked Internship Recommendations
  ↓
Results Page
```

## Example Use Case

A user interested in:

```text
Domain: Data Science
Skills: Python, SQL, Machine Learning, Pandas
```

can receive internships whose titles, skills, domains, and descriptions have high textual similarity with the user's profile.

This allows the system to provide personalized recommendations instead of displaying internships without considering the user's skills and interests.

## Security

- Database credentials are stored using environment variables.
- `.env` is excluded from version control using `.gitignore`.
- `.env.example` is provided with placeholder credentials for configuration.
- Sensitive credentials should never be committed to GitHub.

## Future Improvements

- Add user feedback to improve recommendations
- Add collaborative filtering
- Add a larger and continuously updated internship dataset
- Add advanced ranking and recommendation models
- Deploy the application to a cloud platform
- Add an admin panel for internship management
- Add email notifications for recommended internships

## Skills Demonstrated

- Python Programming
- FastAPI
- REST API Development
- Natural Language Processing
- Machine Learning
- Recommendation Systems
- TF-IDF
- Cosine Similarity
- Pandas
- Scikit-learn
- MySQL
- SQL
- HTML
- CSS
- JavaScript
- Git and GitHub
- Environment Configuration
