from flask import Flask, render_template, url_for, flash, redirect
from forms import InputForm

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model): #creation of database
    id = db.Column(db.Integer, primary_key=True)
    name_of_subscription = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    billing_cycle = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.email}','{self.name_of_subscription}', '{self.billing_cycle}', {self.cost}) 


@app.route("/"):    #Home page (I just put something here as a placeholder)
    def home():
        return render_template('', subtitle = 'Home Page', text = 'this is the home page')
    
@app.route("/register", methods = ['GET', 'POST']): #the register page 
    def register():
        form = InputForm()
        if form.validate_on_submit(): #what happens when the user signs up for our reminder
            user = User(name_of_subscription=form.name_of_subscription.data, email=form.email.data, billing_cycle=form.billing_cycle.data, cost = form.cost.data)
            db.session.add(user)
            db.session.commit()
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('home')) # if so - send to home page
        return render_template('register.html', title='Register', form=form)

            
            
            
            
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
            
    