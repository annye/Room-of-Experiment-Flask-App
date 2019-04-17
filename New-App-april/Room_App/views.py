"""
Routes and views for the flask application.
Created on  Tuesday, 9 April 2019
@author: A.Braca
"""

from datetime import datetime
from flask import render_template , request, session, redirect, url_for, render_template, flash
from Room_App import app
from .models import User, display
from werkzeug.debug import DebuggedApplication
from flask_paginate import Pagination, get_page_args
import pandas as pd 
import sys
import pdb
import os
from multiprocessing import Value

counter = Value('i', 0)

app.secret_key = os.urandom(24)


@app.route('/')
def index():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method =="POST":
        username = request.form["username"]
        password = request.form["password"]
        
        user = User(username)

        if not user.register(password):
            flash("Alredy alredy exists")
        else:
            flash("Success")
            return redirect(url_for("login"))
    return render_template('register.html')



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
       
        password = request.form["password"]

        user = User(username)

        if not user.verify_password(password):
            flash("Invalid login.")
        else:
            flash("Successfully logged in.")
            session["username"] = user.username
            flash (session["username"])
            return redirect(url_for("survey"))

    return render_template("login.html")


@app.route("/survey", methods=["GET","POST"])
def survey():
    return render_template("survey.html")

@app.route("/add_survey", methods=["POST"])
def add_survey():
    gender = request.form["gender"]
    sexuality = request.form["sexuality"]
    ethnicity = request.form["ethnicity"]
    occupation = request.form["occupation"]
    marital_status = request.form["marital_status"]
    education = request.form["education"]
    vehicle = request.form["vehicle"]
    recreation = request.form["recreation"]
    age = request.form["age"]
    religion = request.form["religion"]
    

    user = User(session["username"])

    if not sexuality or not vehicle or not education:
        flash("You must answer all the questions.")
    else:
        user.add_survey(gender,
                        sexuality,
                        ethnicity,
                        occupation,
                        marital_status,
                        education,
                        vehicle,
                        age,
                        religion,
                        recreation)

    return redirect(url_for("index"))


@app.route("/values", methods=["GET","POST"])
def values():
    return render_template("values.html")


@app.route("/add_values", methods=["POST"])
def add_values():
    values_list = ["v1","v2","v3","v4","v5","v6","v7","v8","v9","v10","v11","v12","v13",
                    "v14","v15","v16","v17","v18","v19","v20","v21","v22","v23","v24",
                    "v25","v26","v27","v28","v29","v30","v31","v32","v33"]
    likert = []
    for element in values_list:
        score = request.form[element]
        likert.append(score)
    user = User(session["username"])
    
    user.add_values(likert)
    return redirect(url_for("index"))

@app.route("/personality", methods=["GET","POST"])
def personality():
    return render_template("personality.html")

@app.route("/add_personality", methods=["POST"])
def add_personality():
    personality_list = ["p1", "p2", "p5", "p8", "p10", "p12", "p18",
                        "p19", "p20", "p24", "p27", "p28", "p29", "p30",
                        "p31", "p32", "p33", "p34", "p36", "p37", "p39",
                        "p40", "p42", "p44", "p46", "p47", "p48", "p49",
                        "p50", "p51"] 
    likert = []
    for element in personality_list:
        score = request.form[element]
        likert.append(score)
    user = User(session["username"])
    user.add_personality(likert)
    return redirect(url_for("index"))

@app.route("/sensory", methods=["GET","POST"])
def sensory():
    return render_template("sensory.html")

@app.route("/add_sensory", methods=["POST"])
def add_sensory():
    s1=request.form["s1"]
    s2=request.form["s2"]
    s3=request.form["s3"]
    s4=request.form["s4"]
    s5=request.form["s5"]
    s6=request.form["s6"]

    user = User(session["username"])
    user.add_sensory(s1,s2,s3,s4,s5,s6)
    return redirect(url_for("index"))
    


@app.route("/odontophobia", methods=["GET","POST"])
def odontophobia():
    return render_template("odontophobia.html")


@app.route("/add_odontophobia", methods=["POST"])
def add_odontophobia():
    odontophobia_list = ["f1","f2","f3","f4","f5","f6","f7","f8","f9","f10"]
    likert = []
    for element in odontophobia_list:
        score = request.form[element]
        likert.append(score)
    user = User(session["username"])
    user.add_odontophobia(likert)
    print(likert)
    return redirect(url_for("index"))


@app.route("/add_oral_q", methods=["POST"])
def add_oral_q():
    return redirect(url_for("index"))





@app.route("/oral_q", methods=["GET","POST"])
def oral_q():
    return render_template("dental_believes.html")



@app.route("/table1", methods=["GET",'POST'])
def table1():
    return render_template("table1.html")

@app.route("/add_table_1",methods=["POST"])
def add_table_1():
    rates1=request.form['rates1']
    rates2=request.form['rates2']
    rates3=request.form['rates3']
    rates4=request.form['rates4']
    rates5=request.form['rates5']

    user = User(session["username"])
    user.add_table_1(rates1,rates2,rates3,rates4,rates5)
    return redirect(url_for("r_answers"))


@app.route("/table2", methods=["GET",'POST'])
def table2():
    return render_template("table2.html")


@app.route("/add_table_2",methods=["POST"])
def add_table_2():
    r_1=request.form['r_1']
    r_2=request.form['r_2']
    r_3=request.form['r_3']
    r_4=request.form['r_4']
    r_5=request.form['r_5']

    user = User(session["username"])
    user.add_table_2(r_1,r_2,r_3,r_4,r_5)
    return redirect(url_for("r_answers"))



@app.route("/table3", methods=["GET",'POST'])
def table3():
    return render_template("table3.html")

@app.route("/add_table_3",methods=["POST"])
def add_table_3():
    tq_1=request.form['tq_1']
    tq_2=request.form['tq_2']
    tq_3=request.form['tq_3']
    tq_4=request.form['tq_4']
    tq_5=request.form['tq_5']

    user = User(session["username"])
    user.add_table_3(tq_1,tq_2,tq_3,tq_4,tq_5)
    return redirect(url_for("r_answers"))



@app.route("/table4", methods=["GET",'POST'])
def table4():
    return render_template("table4.html")

@app.route("/add_table_4",methods=["POST"])
def add_table_4():
    sq_1=request.form['sq_1']
    sq_2=request.form['sq_2']
    sq_3=request.form['sq_3']
    sq_4=request.form['sq_4']
    sq_5=request.form['sq_5']

    user = User(session["username"])
    user.add_table_4(sq_1,sq_2,sq_3,sq_4,sq_5)
    return redirect(url_for("r_answers"))

@app.route("/table5", methods=["GET",'POST'])
def table5():
    return render_template("table5.html")

@app.route("/add_table_5",methods=["POST"])
def add_table_5():
    ssq_1=request.form['ssq_1']
    ssq_2=request.form['ssq_2']
    ssq_3=request.form['ssq_3']
    ssq_4=request.form['ssq_4']
    ssq_5=request.form['ssq_5']
    ssq_6=request.form['ssq_6']
    ssq_7=request.form['ssq_7']

    user = User(session["username"])
    user.add_table_5(ssq_1,ssq_2,ssq_3,ssq_4,ssq_5,ssq_6,ssq_7)
    return redirect(url_for("r_answers"))

@app.route("/table6", methods=["GET",'POST'])
def table6():
    return render_template("table6.html")

@app.route("/table7", methods=["GET",'POST'])
def table7():
    return render_template("table7.html")

@app.route("/add_table_7",methods=["POST"])
def add_table_7():
    m_1=request.form['m_1']
    m_2=request.form['m_2']
    m_3=request.form['m_3']
    m_4=request.form['m_4']
    m_5=request.form['m_5']

    user = User(session["username"])
    user.add_table_7(m_1,m_2,m_3,m_4,m_5)
    return redirect(url_for("r_answers"))

@app.route("/add_argument", methods=["POST"])
def add_argument():
    issue = request.form["issue"]
    side = request.form["side"]
    type_schema = request.form["type_schema"]
    premise_type=request.form["premise_type"]
    argu = request.form["argu"] 
    major_premise = request.form["major_premise"]
    minor_premise = request.form["minor_premise"]
    conclusion = request.form["conclusion"]
    type_dialog = request.form["type_dialog"]
    influence_social = request.form["influence_social"]
    support = request.form["support"]
    source =request.form["source"]
    
    
    user = User(session["username"])
   
    user.add_arguments(issue, 
                        side,
                        type_schema,
                        premise_type, 
                        argu, 
                        major_premise,
                        "",
                        minor_premise,
                        conclusion,
                        type_dialog,
                        influence_social,
                        support,
                        source)

    return redirect(url_for("index"))

@app.route("/room_discussions", methods=["GET","POST"])
def room_discussions():
    return render_template("dialogs_front.html") 


@app.route('/dialogs')
def dialogs():
    """Renders the dialogs page."""
    postsA, postsB, posts = display()
    posts = [item for pair in zip(postsA, postsB) for item in pair]
    #import pdb; pdb.set_trace()
    if (counter.value <= len(posts)-2):
        range_posts = list(range(0, counter.value + 2, 2))
        counter.value = counter.value + 2
    else:
        range_posts = list(range(0, counter.value, 2))
    return render_template('dialogs.html', posts=posts, range_posts=range_posts)
                        
@app.route('/r_answers')
def r_answers():
    return render_template("r_answers.html")

@app.route("/statements", methods=["GET","POST"])
def statements():
    return render_template("argument_save.html")


@app.route("/like_argument/<argument_id>")
def like_argument(argument_id):
    username = session.get("username")
    if not username:
        flash("You must be logged in to participate in the experiment.")
        return redirect(url_for("login"))
    user = User(username)
    user.like_argument(argument_id,6)
    flash("Liked Dialogs.")
    return redirect(request.referrer)


@app.route("/like_argument_5/<argument_id>")
def like_argument_5(argument_id):
    username = session.get("username")
    if not username:
        flash("You must be logged in to participate in the experiment.")
        return redirect(url_for("login"))
    user = User(username)
    user.like_argument(argument_id, 5)
    flash("Rated 5 stars .")
    return redirect(request.referrer)


@app.route("/like_argument_4/<argument_id>")
def like_argument_4(argument_id):
    username = session.get("username")
    if not username:
        flash("You must be logged in to participate in the experiment.")
        return redirect(url_for("login"))
    user = User(username)
    user.like_argument(argument_id, 4)
    flash("Rated 4 stars.")
    return redirect(request.referrer)


@app.route("/like_argument_3/<argument_id>")
def like_argument_3(argument_id):
    username = session.get("username")
    if not username:
        flash("You must be logged in to participate in the experiment.")
        return redirect(url_for("login"))
    user = User(username)
    user.like_argument(argument_id, 3)
    flash("Liked Dialogs.")
    return redirect(request.referrer)


@app.route("/like_argument_2/<argument_id>")
def like_argument_2(argument_id):
    username = session.get("username")
    if not username:
        flash("You must be logged in to participate in the experiment.")
        return redirect(url_for("login"))
    user = User(username)
    user.like_argument(argument_id, 2)
    flash("Liked Dialogs.")
    return redirect(request.referrer)


@app.route("/like_argument_1/<argument_id>")
def like_argument_1(argument_id):
    username = session.get("username")
    if not username:
        flash("You must be logged in to participate in the experiment.")
        return redirect(url_for("login"))
    user = User(username)
    user.like_argument(argument_id, 1)
    flash("Liked Dialogs.")
    return redirect(request.referrer)


@app.route('/buy_car')
def buy_car():
    """Renders the cars template page."""
    return render_template('buy_car.html')
                   

@app.route('/q_life')
def q_life():
    """Renders the cars template page."""
    return render_template('q_life.html')

@app.route('/tablets')
def tablets():
    """Renders the cars template page."""
    return render_template('tablets.html')

@app.route("/add_tablets/", methods=["POST"])
def add_tablets():
     """Save rates tables."""
     return redirect(url_for("index"))
      



@app.route("/add_ratings/", methods=["POST"])
def add_ratings():
    """Save rates table."""

    rating = int(request.form["rating_value"])
    user = User(session["username"])
    user.add_ratings(rating)  # One of 1, 2, 3, 4, 5
    return "OK"

@app.route("/rates_argument/<argument_id>")
def rates_argu(argument_id):
    username = session.get("username")
    if not username:
        flash("You must be logged in to participate in the experiment.")
        return redirect(url_for("login"))
    user = User(username)
    user.like_argument(argument_id)
    flash("Liked Dialogs.")
    return redirect(request.referrer)

# --------Display the  dialog experimemts###
@app.route("/profile/<username>")
def profile(username):
    user1 = User(session.get("username"))
    posts = display()
    return render_template("profile.html", username=username, posts=posts)

@app.route('/postquestions')
def postquestions():
    """Renders the post experiments page."""

    return render_template("post_questions01.html")

@app.route('/postquestions_02')
def post_questions02():
    """Renders the post experiments page."""

    return render_template("post_questions02.html")

@app.route("/logout")
def logout():
    session.pop("username")

    flash("Logged out.")
    return redirect(url_for("index"))
