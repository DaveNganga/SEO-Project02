from flask import Flask, render_template, url_for, flash, redirect
from form import InputForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')

app.config['SECRET_KEY'] = '6849ddabd6659cb932e048b24afa64d71de66d5a9b4a5974'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model): #creation of database
    id = db.Column(db.Integer, primary_key=True)
    name_of_subscription = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    billing_cycle = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.email}','{self.name_of_subscription}', '{self.billing_cycle}', {self.cost})" 


@app.route("/")    #Home page (I just put something here as a placeholder)
def home():
    return render_template('homepage.html')
    
@app.route("/register", methods = ['GET', 'POST']) #the register page 
def register():
    form = InputForm()
    if form.validate_on_submit(): #what happens when the user signs up for our reminder
        user = User(name_of_subscription=form.name_of_subscription.data, email=form.email.data, billing_cycle=form.billing_cycle.data, cost = form.cost.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home')) # if so - send to home page
    return render_template('register.html', title='Register', form=form)

@app.route("/login")    #Home page (I just put something here as a placeholder)
def login():
    return render_template('login.html')

@app.route("/dashboard")    #Home page (I just put something here as a placeholder)
def dashboard():
    return render_template('dashboard.html')

@app.route("/help")    #Home page (I just put something here as a placeholder)
def help():
    return render_template('faq.html', subtitle = 'FAQ', text1 = 'When will I get my remind Email?',
                          text2 = 'You will get your remind email 24 hours befroe the next billing date.',
                          text3 = 'How many app can I register on my account',
                          text4 = 'You can add as many as you would like.',
                          text5 = 'Can I cancel my account?',
                          text6 = 'Yes, you can cancel your account at anytime.')

@app.route("/help_logged")    #Home page (I just put something here as a placeholder)
def loggedhelp():
    return render_template('faq_logged.html')

@app.route("/home_logged")    #Home page (I just put something here as a placeholder)
def loggedHome():
    return render_template('homepage_logged.html')
            
            
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
            
    