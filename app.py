from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
import random
import time

app = Flask(__name__)

# Configure MongoDB (adjust URI for your setup)
app.config["MONGO_URI"] = "mongodb://localhost:27017/quiz_db"
mongo = PyMongo(app)

# Timer limit for each quiz in seconds
QUIZ_TIME_LIMIT = 60


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/quiz')
def quiz():
    # Fetch all questions from MongoDB and randomize them
    questions = list(mongo.db.questions.aggregate([{"$sample": {"size": 5}}]))  # Get 5 random questions
    return render_template('quiz.html', questions=questions, timer=QUIZ_TIME_LIMIT)


@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve submitted answers
    answers = request.form.to_dict()
    total_score = 0
    question_ids = list(mongo.db.questions.find({}))

    # Check answers and calculate score
    for question in question_ids:
        if answers.get(str(question['_id'])) == question['correct_answer']:
            total_score += 1

    # Save score in MongoDB (optional)
    mongo.db.scores.insert_one({'score': total_score, 'timestamp': time.time()})

    return render_template('result.html', score=total_score)


if __name__ == '__main__':
    app.run(debug=True)
