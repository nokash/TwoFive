from flask import Flask, render_template, request, url_for, redirect, flash, session
from wtforms import Form, BooleanField, PasswordField, TextField, validators
from db_connect import connection
from passlib.hash import sha256_crypt
import MySQLdb
from MySQLdb import escape_string as thwart
import gc
from functools import wraps
import smtplib
from flask_mail import Mail, Message
import time as now
<<<<<<< HEAD
from content_manager import Content


TOPIC_DICT = Content()
=======
# from content_manager import Content, Get_Stuff
>>>>>>> 41f9199593e797a1bf1ffe0da30159d7fb849d10

app = Flask(__name__)
app.config.update(
        DEBUG = True,
        #EMAIL SETTINGS
        MAIL_SERVER = 'smtp.gmail.com',
        MAIL_PORT = 465,
        MAIL_USE_SSL = True,
        MAIL_USERNAME = 'ashfordnokash@gmial.com',
        MAIL_PASSWORD = "$5$rounds=535000$xfRqsuXbyjd0E.jh$eXJj9Ky/H4l.Tnd3Pgw4Ew2/MZWqcZBa95pLS58MpgD"
        )
mail = Mail(app)

# Post = Get_Stuff()
# TOPIC_DICT = Content()

@app.route('/')
def homepage():
        flash("Hapa ndo kwao!!!!")
	return render_template("home.html")

@app.route('/services/')
def services():
	return render_template("services.html")


@app.route('/train/')
def train():
	return render_template("train.html")

<<<<<<< HEAD
=======

def postlist():
>>>>>>> 41f9199593e797a1bf1ffe0da30159d7fb849d10

def postlist(id):
        try:
                c, conn = connection()


<<<<<<< HEAD
                x = c.execute("SELECT * FROM post where id = '%s'" % id)
                x = c.fetchall()
                for row in x:
                    Post = [dict(id=row[0],
                    Title=row[1],
                    Body=row[2],
                    Date=row[3],
                    Author=row[4],
                    Url=row[6])]
=======
                        x = c.execute("SELECT * FROM post")
                        Post = [dict(id=row[0],
                                      Title=row[1],
                                      Body=row[2],
                                      Date=row[3],
                                      Author=row[4],
                                      Url=row[6]) for row in c.fetchall()]

>>>>>>> 41f9199593e797a1bf1ffe0da30159d7fb849d10

                    c.close()
                    conn.close()

                return Post

        except Exception as exc:
                return (str(exc))

@app.route('/posts/', methods=["GET", "POST"])
def posts():
        # Post = postlist()


        try:
                c, conn = connection()

                if request.method == "GET":


                        x = c.execute("SELECT * FROM post ORDER BY ID DESC LIMIT 1")
                        Posts = [dict(id=row[0],
                                      Title=row[1],
                                      Body=row[2],
                                      Date=row[3],
                                      Author=row[4]) for row in c.fetchall()]


                        c.close()
                        conn.close()




                return render_template("posts.html", Posts=Posts,TOPIC_DICT=TOPIC_DICT)

        except Exception as exc:
                return (str(exc))



@app.route('/portfolio/')
def portfolio():
	return render_template("portfolio.html")

@app.route('/partners/')
def partners():
	return render_template("partners.html")

@app.route('/about/')
def about():
	return render_template("about.html")



@app.errorhandler(404)
def page_not_found():
     return render_template("error404.html")


@app.route('/register/', methods=["GET", "POST"])
def register_page():
        try:
                c, conn = connection()
                form = RegistrationForm(request.form)

                if request.method == "POST" and form.validate():
                        username = form.username.data
                        email = form.email.data
                        password = sha256_crypt.encrypt(str(form.password.data))
                        c, conn = connection()


                        x = c.execute("SELECT * FROM users WHERE username = (%s)", (thwart(username),))

                        if int(x) > 0:
                                flash("That username is already taken. Please try another!")
                                render_template("register.html", form = form)

                        else:
                                c.execute("INSERT INTO users (username, email, password) VALUES ('%s', '%s', '%s')" %
                                                  ((username), (email), (password)))

                                conn.commit()

                                flash("Thanks for registering")

                                c.close()
                                conn.close()

                                gc.collect()

                                session['logged_in'] = True
                                session['username'] = username

                                return redirect(url_for('homepage'))

                return render_template("register.html", form=form)



                #return render_template("register.html")
        except Exception as exc:
                return (str(exc))

def login_required(fn):
        @wraps(fn)
        def wrap(*args,**kwargs):
                if 'logged_in' in session:
                        return fn(*args, **kwargs)
                else:
                        flash("You need to log in first")
                        return redirect(url_for('login_page'))
        return wrap

def admin_required(fn):
        @wraps(fn)
        def wrap(*args,**kwargs):

                if 'username' in session:
                        username = session['username']
                        if username == 'admin':

                                return fn(*args, **kwargs)

                        else:
                                flash("You need to log in as admin first")
                                return redirect(url_for('login_page'))
        return wrap

def urllist():

        try:
                c, conn = connection()

                if request.method == "GET":

                        x = c.execute("SELECT * FROM post")

                        Urls = [dict(id=row[0],
                                      Title=row[1],
                                      Body=row[2],
                                      Date=row[3],
                                      Author=row[4],
                                      Url =row[6]) for row in c.fetchall()]

                        c.close()
                        conn.close()

<<<<<<< HEAD
                return Urls
=======
                        return Urls
>>>>>>> 41f9199593e797a1bf1ffe0da30159d7fb849d10

        except Exception as exc:
                return (str(exc))


@app.route('/adminpanel/', methods=["GET", "POST"])
@login_required
@admin_required
def publish():
<<<<<<< HEAD
    Urls = urllist()
=======
    Urls = postlist()
>>>>>>> 41f9199593e797a1bf1ffe0da30159d7fb849d10

    try:
                c, conn = connection()

                if 'username' in session:
                        username = session['username']


                if request.method == "POST":
                        title = thwart(request.form['title'])
                        url = "/%s/" % title.lower().replace("-","_").replace(")","").replace("(","").replace(".","").replace("/","-").replace("!","").replace(":","-").replace("'","").replace(" ","-")
                        body = thwart(request.form['body'])
                        date = now.strftime('%Y-%m-%d %H:%M:%S')
                        author = thwart(request.form['author'])

                        # TOPIC_DICT[title] = url
                        c, conn = connection()


                        c.execute("INSERT INTO post (title, body, date, author, url) VALUES ('%s','%s','%s', '%s', '%s')" %
                                                  ((title), (body), (date), (author), (url)))

                        conn.commit()



                        c.close()
                        conn.close()

                        gc.collect()



                        # flash(Urls)
                return render_template("adminpanel.html", Urls=Urls)



                #return render_template("register.html")
    except Exception as exc:
                return (str(exc))



@app.route('/logout/')
@login_required
def logout():
        session.clear()
        flash("You have been logged out")
        gc.collect()
        return redirect(url_for('homepage'))

@app.route('/login/', methods=["GET", "POST"])
def login_page():
        error = ""
        try:
                c, conn = connection()
                if request.method == "POST":
                        data = c.execute("SELECT * FROM users WHERE username = '%s'" % (thwart(request.form['username'])))
                        data = c.fetchone()[2]

#username = '%s' " % (request.form["username"]))
                        if sha256_crypt.verify(request.form['password'], data):
                                session['logged_in'] = True
                                session['username'] = request.form['username']

                                flash("You are now logged in")
                                return redirect(url_for('homepage'))
                        else:
                                error = "Invalid credentials, try again."

                gc.collect()

                return render_template("login.html", error = error)

        except Exception as exc:
                flash(exc)
                error = "Invalid credentials, try again."
                return render_template("login.html", error = error)





@app.errorhandler(405)
def method_not_found():
     return render_template("error405.html")

@app.errorhandler(500)
def server_isht():
     return render_template("error500.html")

@app.route(TOPIC_DICT["Articles"][5][1], methods = ["GET", "POST"])
def ggfg():
    url = TOPIC_DICT["Articles"][5][1]
    id = TOPIC_DICT["Articles"][5][2]
    Post = postlist(id)
    flash(id)
    flash(Post)
    return render_template("ggfg.html",TOPIC_DICT=TOPIC_DICT, Post=Post)





@app.route(TOPIC_DICT["Articles"][11][1], methods = ["GET", "POST"])
def hvgvjjbhj():
    url = TOPIC_DICT["Articles"][11][1]
    id = TOPIC_DICT["Articles"][11][2]
    Post = postlist(id)
    flash(id)
    flash(Post)
    return render_template("hvgvjjbhj.html",TOPIC_DICT=TOPIC_DICT, Post=Post)






@app.route(TOPIC_DICT["Articles"][20][1], methods = ["GET", "POST"])
def sasdsadsaddsa():
    url = TOPIC_DICT["Articles"][20][1]
    id = TOPIC_DICT["Articles"][20][2]
    Post = postlist(id)
    flash(id)
    flash(Post)
    return render_template("sasdsadsaddsa.html",TOPIC_DICT=TOPIC_DICT, Post=Post)





@app.route(TOPIC_DICT["Articles"][21][1], methods = ["GET", "POST"])
def Conspiracy():
    url = TOPIC_DICT["Articles"][21][1]
    id = TOPIC_DICT["Articles"][21][2]
    Post = postlist(id)
    flash(id)
    flash(Post)
    return render_template("conspiracy.html",TOPIC_DICT=TOPIC_DICT, Post=Post)






def uyyyuuhhjbiuinjjjjnmnmn():
    url = TOPIC_DICT["Articles"][24][1]
    id = TOPIC_DICT["Articles"][24][2]
    Post = postlist(id)
    flash(id)
    flash(Post)
    return render_template("uyyyuu-hhjbiui-njjjj-nmnmn-.html",TOPIC_DICT=TOPIC_DICT, Post=Post)





@app.route(TOPIC_DICT["Articles"][25][1], methods = ["GET", "POST"])
def Arch():
    url = TOPIC_DICT["Articles"][25][1]
    id = TOPIC_DICT["Articles"][25][2]
    Post = postlist(id)
    flash(id)
    flash(Post)
    return render_template("arch.html",TOPIC_DICT=TOPIC_DICT, Post=Post)




class RegistrationForm(Form):
	username = TextField('Username', [validators.Length(min=4, max=20)])
	email = TextField('Email Address', [validators.Required('Please enter your email address'), validators.Email("Please enter a valid email address.")])
	password = PasswordField('Password', [validators.Required(),
                                              validators.EqualTo('confirm', message = "Passwords must match, dude!")])
	confirm = PasswordField('Repeat Password')
	tos_commit = BooleanField('I agree to the <a href="/tos/">Terms of Service </a> and <a href="/privacy/">Privacy policy notice<a/>(Last updated June 2016)', [validators.Required()])



if __name__ == "__main__":
     app.secret_key = 'M_Pure822'
     app.config['SESSION_TYPE'] = 'filesystem'

     #sess.init_app(app)
    # app.debug = True
     app.run()
