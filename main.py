from flask import Flask, render_template, url_for, flash, redirect
from form import InputForm, RegistrationForm
from flask_sqlalchemy import SQLAlchemy
from models import *
app = Flask(__name__, template_folder='templates')


app = Flask(__name__)
app.config['SECRET_KEY'] = '6849ddabd6659cb932e048b24afa64d71de66d5a9b4a5974'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

@app.route("/", methods = ['GET', 'POST'])    #Home page (I just put something here as a placeholder)
def home(): 
    form = RegistrationForm()
    if form.validate_on_submit(): #what happens when the user signs up for an account
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('/dashboard.html'))
    elif form.is_submitted(): 
        flash('error: account not created')
        return redirect(url_for('home', _anchor='login'))
    else:
        return render_template('homepage.html', title="Homepage", form=form)

@app.route("/register_account", methods = ['GET', 'POST']) #the register page 
def register_account():
    form = RegistrationForm()
    if form.validate_on_submit(): #what happens when the user signs up for an account
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home')) # if so - send to home page
    print(form.errors)
    return render_template('register_account.html', title='Register account', form=form)
     
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
    return render_template('faq_logged.html', subtitle = 'FAQ', text1 = 'When will I get my remind Email?',
                          text2 = 'You will get your remind email 24 hours befroe the next billing date.',
                          text3 = 'How many app can I register on my account',
                          text4 = 'You can add as many as you would like.',
                          text5 = 'Can I cancel my account?',
                          text6 = 'Yes, you can cancel your account at anytime.')

@app.route("/home_logged")    #Home page (I just put something here as a placeholder)
def loggedHome():
    return render_template('homepage_logged.html')
                    

if __name__ == '__main__':
      app.run(debug=True, host="0.0.0.0")
            
    