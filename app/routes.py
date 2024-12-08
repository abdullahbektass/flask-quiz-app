from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, Question, load_user
from . import mongo, bcrypt
from bson import ObjectId

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def home():
    questions = mongo.db.questions.find()
    return render_template('home.html', questions=questions)

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        user_id = User.create_user({
            "fullname": fullname,
            "email": email,
            "password_hash": hashed_password,
            "high_score": 0
        })
        flash('Registration successful!', 'success')
        return redirect(url_for('main.login'))

    return render_template('signup.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if current_user.is_authenticated:
            return redirect(url_for('main.quiz'))
        email = request.form['email']
        password = request.form['password']
        user_data = mongo.db.users.find_one({"email": email})

        if user_data and bcrypt.check_password_hash(user_data['password_hash'], password):
            user = User(
                fullname=user_data['fullname'],
                email=user_data['email'],
                password_hash=user_data['password_hash'],
                high_score=user_data['high_score'],
                id=str(user_data['_id'])
            )
            login_user(user)
            if current_user.is_authenticated:
                print('Login successful!')
            flash('Login successful!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Login failed. Check email and password.', 'danger')

    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.login'))

@main.route('/add_question', methods=['GET', 'POST'])
@login_required
def add_question():
    if request.method == 'POST':
        text = request.form['text']
        answers = [
            request.form['answer1'],
            request.form['answer2'],
            request.form['answer3'],
            request.form['answer4'],
        ]
        correct_answer = int(request.form['correct_answer'])

        question_data = {
            "text": text,
            "answers": answers,
            "correct_answer": correct_answer
        }

        Question.create_question(question_data)
        flash('Question added successfully!', 'success')
        return redirect(url_for('main.home'))

    return render_template('add_question.html')


@main.route('/score', methods=['POST'])
@login_required
def score():
    questions = list(mongo.db.questions.find())
    total_questions = len(questions)
    user = load_user(current_user.id)
    score = 0
    is_high_score = False

    for question in questions:
        user_answer = request.form.get(f"question_{question['_id']}")
        if user_answer and int(user_answer) == question['correct_answer']:
            score += 1

    if score > user.high_score:
        mongo.db.users.update_one({'_id': ObjectId(user.id)}, {'$set': {'high_score': score}})
        is_high_score = True
    
    return render_template('score.html', score=score, total_questions=total_questions, is_high_score=is_high_score)
