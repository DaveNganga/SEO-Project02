from flask import Flask, render_template, url_for, request, flash, redirect
from form import LoginForm, RegistrationForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '6849ddabd6659cb932e048b24afa64d71de66d5a9b4a5974'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newdb.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class User(db.Model): 
#create database for registering
      id = db.Column(db.Integer, primary_key=True)
      username = db.Column(db.String(20), unique=True, nullable=False)
      email = db.Column(db.String(120), unique=True, nullable=False)
      password = db.Column(db.String(60), nullable=False)
      
      def __repr__(self):
            return f"User('{self.username}', '{self.email}')"

class UserSubscription(db.Model): 
#creation of database for subscription data
      id = db.Column(db.Integer, primary_key=True)
      name_of_subscription = db.Column(db.String(20), unique=True, nullable=False)
      email = db.Column(db.String(120), unique=True, nullable=False)
      billing_cycle = db.Column(db.Integer, nullable=False)
      cost = db.Column(db.String(60), nullable=False)

      def __repr__(self):
            return f"UserSubscription('{self.email}','{self.name_of_subscription}', '{self.billing_cycle}', '{self.cost}')"       

        
@app.route("/")    #Home page (I just put something here as a placeholder)
def home():
      return render_template('homepage.html')

  
@app.route("/signup", methods = ['GET', 'POST']) #the register page 
def signup():
    form = RegistrationForm()
    if form.validate_on_submit(): #what happens when the user signs up for an account
        new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home')) # if so - send to home page
    return render_template('signup.html', title='Sign up', form=form)

  
@app.route("/login", methods = ['GET', 'POST']) 
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
#       user = User.query.filter_by(email=form.email.data).first()
        if not user:
            flash(f'User not found for {form.username.data}!')
            return redirect(url_for('signup'))
        if form.password.data != user.password:
            flash('password is incorrect! Please try again')
            return redirect(url_for('login'))
        return redirect(url_for('homepageLogged'))
    return render_template('login.html', title="log in", form=form)

      
@app.route('/logout')
def logout():
    return render_template('homepage.html')     
  
@app.route('/homepage_logged')
def homepageLogged():
    return render_template('homepage_logged.html')  
  
@app.route('/profile')
def profile():
    return render_template('profile.html')
      
@app.route("/dashboard")    #Home page (I just put something here as a placeholder)
def dashboard():
      return render_template('dashboard.html')

@app.route("/help")    #Home page (I just put something here as a placeholder)
def help():
      return render_template('faq.html')

@app.route("/register", methods = ['GET', 'POST']) #the register subscription page 
def register_sub():
      form = InputForm()
      if form.validate_on_submit(): #what happens when the user signs up for our reminder
         user = UserSubscription(name_of_subscription=form.name_of_subscription.data, email=form.email.data, billing_cycle=form.billing_cycle.data, cost = form.cost.data)
         db.session.add(user)
         db.session.commit()
         flash(f'Account created for {form.name_of_subscription.data}!', 'success')
         return redirect(url_for('home')) # if so - send to home page
      return render_template('register_sub.html', title='Register Subscription', form=form)
                  
if __name__ == '__main__':
      app.run(debug=True, host="0.0.0.0")
            
    