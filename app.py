from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import *

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


questions = satisfaction_survey.questions






@app.route('/')
def home_page():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('home.html', title=title, instructions=instructions)

@app.route('/store-session', methods=["POST"])
def store_sessions():
    """POST request to server setting session of survey choices to an empty list """
    session["res"] = []  
    return redirect('/questions/0') 

@app.route('/questions/0')

def question_0():
    n = len(session["res"])
   
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
    
    
    res = session["res"]
    res.append(data)
    session["res"] = res
    
    n = len(session["res"])

    if len(questions) == n:
        return redirect('/thank-you')
    else:
        return redirect(f'/questions/{n}')


@app.route('/questions/1')
def question_1():
    n = len(session["res"])
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
    n = len(session["res"])
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
    n = len(session["res"])
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
    print("*********************")
    print(session['res'])
    print("*********************")
    return render_template('thank-you.html')


