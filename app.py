from test import app, db, Question  # importing app, db, and Question from your Flask app

# This is a list of dictionaries, where each dictionary represents a question.
questions = [
    {
        "text": "Qui est considéré comme le père de la sociologie ?",
        "option1": "Émile Durkheim",
        "option2": "Max Weber",
        "option3": "Karl Marx",
        "option4": "Auguste Comte",
        "correct_option": 4,
    },
    {
        "text": "Quel concept Durkheim utilise pour expliquer le lien social dans les sociétés modernes ?",
        "option1": "La solidarité mécanique",
        "option2": "La solidarité organique",
        "option3": "L'anomie",
        "option4": "Le fait social",
        "correct_option": 2,
    },
    {
        "text": "Quel sociologue a développé le concept de 'l'idéal-type' ?",
        "option1": "Karl Marx",
        "option2": "Émile Durkheim",
        "option3": "Max Weber",
        "option4": "Pierre Bourdieu",
        "correct_option": 3,
    },
    # Add the rest of your questions here...
]

with app.app_context():  # This creates an application context
    # This loop goes through the list of questions and adds each one to the database.
    for q in questions:
        question = Question(
            text=q["text"],
            option1=q["option1"],
            option2=q["option2"],
            option3=q["option3"],
            option4=q["option4"],
            correct_option=q["correct_option"],
        )
        db.session.add(question)

    # This commits the changes and adds the questions to the database.
    db.session.commit()
