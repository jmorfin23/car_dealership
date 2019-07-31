from app import app
from flask import render_template, url_for, redirect, flash
from app.forms import FindForm
from app.models import Account


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/who_we_are')
def who_we_are():
    return render_template('who_we_are.html', title='Who We Are' )

@app.route('/cars')
def cars():
    return render_template('cars.html', title='Cars')

@app.route('/find', methods=['GET', 'POST'])
def find():
    form = FindForm()
    if form.validate_on_submit():
        # select top(1) from public.account where account_id = form.name.data
        name = Account.query.filter_by(account_id=int(form.name.data)).first()
        print(name)
        if name:
            return redirect(url_for('find'))

        if user is None:
            flash('Incorrect name.')
            return redirect(url_for('find'))
        return redirect('/find')

    return render_template('find.html', title='Find', form=form)
