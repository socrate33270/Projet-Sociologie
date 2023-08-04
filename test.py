from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///messages.db')
db = SQLAlchemy(app)

class Message(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)

class Question(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    option1 = db.Column(db.String(200), nullable=False)
    option2 = db.Column(db.String(200), nullable=False)
    option3 = db.Column(db.String(200), nullable=False)
    option4 = db.Column(db.String(200), nullable=False)
    correct_option = db.Column(db.Integer, nullable=False)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/fiche')
def fiche():
    return render_template('fiche.html')

@app.route('/quizz')
def quizz():
    questions = Question.query.order_by(func.random()).all()
    questions_dict = []
    for question in questions:
        question_dict = {
            'id': question.id,
            'text': question.text,
            'options': [question.option1, question.option2, question.option3, question.option4],
            'correct_option': question.correct_option
        }
        questions_dict.append(question_dict)
    return render_template('quizz.html', questions=questions_dict)

@app.route('/submit_quizz', methods=['POST'])
def submit_quizz():
    score = 0
    questions = Question.query.all()
    for question in questions:
        user_answer = request.form.get('question' + str(question.id))
        if user_answer is None:
            user_answer = 0
        else:
            user_answer = int(user_answer)
        if question.correct_option == user_answer:
            score += 1
    return render_template('quizz_results.html', score=score)

@app.route('/cours')
def cours():
    return render_template('cours.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message_text = request.form.get('message')
        message = Message(name=name, email=email, message=message_text)
        db.session.add(message)
        db.session.commit()
        return render_template('contact.html', message="Votre message a été envoyé !")
    return render_template('contact.html')

@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        return render_template('confirmation.html', name=name)
    return render_template('inscription.html')

if __name__ == '__main__':
    with app.app_context(): 
        db.create_all()
    app.run(debug=True)
