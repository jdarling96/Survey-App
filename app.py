from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import *

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

responses = []
questions = satisfaction_survey.questions






@app.route('/')
def home_page():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('home.html', title=title, instructions=instructions)

@app.route('/questions/0')
def question_0():
    n = len(responses)
   
    if n == 0:
        return render_template('question-0.html', question=questions[0].question, choices=questions[0].choices)
    if n == 4:
        flash("SURVEY COMPLETE!")
        return redirect('/thank-you') 
    else:
        flash("INVALID QUESTION IN SURVEY SEQUENCE!")
        return redirect(f'/questions/{n}')    

@app.route('/answer', methods=["POST"])
def get_awnser():
    data = request.form['choice']
    responses.append(data)
    n = len(responses)

    if len(questions) == n:
        return redirect('/thank-you')
    else:
        return redirect(f'/questions/{n}')


@app.route('/questions/1')
def question_1():
    n = len(responses)
    if n == 1:
        return render_template('question-1.html', question=questions[1].question, choices=questions[1].choices)
    if n == 4:
        flash("SURVEY COMPLETE!")
        return redirect('/thank-you')
    else:
        flash("INVALID QUESTION IN SURVEY SEQUENCE!")
        return redirect(f'/questions/{n}')

@app.route('/questions/2')
def question_2():
    n = len(responses)
    if n == 2:
        return render_template('question-2.html', question=questions[2].question, choices=questions[2].choices)
    if n == 4:
        flash("SURVEY COMPLETE!")
        return redirect('/thank-you') 
    else:
        flash("INVALID QUESTION IN SURVEY SEQUENCE!")
        return redirect(f'/questions/{n}')     

@app.route('/questions/3')
def question_3():
    n = len(responses)
    if n == 3:
        return render_template('question-2.html', question=questions[3].question, choices=questions[3].choices)
    if n == 4:
        flash("SURVEY COMPLETE!")
        return redirect('/thank-you') 
    else:
        flash("INVALID QUESTION IN SURVEY SEQUENCE!")
        return redirect(f'/questions/{n}')


@app.route('/thank-you')
def question_4():
     return render_template('thank-you.html')


