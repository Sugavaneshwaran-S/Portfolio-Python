from flask import Flask,render_template,request, redirect, session, url_for
from flask_pymongo import PyMongo
import bcrypt


app = Flask(__name__, template_folder= 'templates', static_folder= 'static')
app.config['MONGO_DBNAME'] = 'personal'
app.config['MONGO_URI'] = 'mongodb+srv://new-user-31:RsVcWaFohW2a7ero@application1.erodfdx.mongodb.net/personal'

mongo = PyMongo(app)

#database 

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.form == "POST":
        details = mongo.db.details
        login_user = details.find_one({'name': request.form['username']})

        if login_user:
             if bcrypt.hashpw(request.form['pswd'].encode('utf-8'),  login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
                return redirect(url_for('home'))
        else:
            return 'Invalid username or password'
    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        details = mongo.db.details
        existing_user = details.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pswd'].encode('utf-8'), bcrypt.gensalt())
            details.insert_one({'name':request.form['username'], 'password': hashpass,'Email': request.form["email"]})
            return redirect(url_for('login'))
        else: 
            return 'User Already Exists'
    else:
        return render_template('register.html')

@app.route('/home', methods = ['POST'])
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/skills')
def skills():
    return render_template("skills.html")

@app.route('/projects')
def project():
    return render_template("projects.html")

@app.route('/course')
def course():
    return render_template("course.html")

@app.route('/acadamic')
def acadamic():
    return render_template("acadamic.html")


if __name__ == "__main__":
    app.run(debug=True) 