from flask import render_template, url_for, request,redirect
from setup import app,db
from models.dbmodels import *


@app.route('/')
@app.route('/homepage')
def homepage():
    print(url_for('homepage'))
    return render_template('homepage.html')


@app.route('/departments')
def departments():
    res = Department.query.all()
    print(res)
    return render_template('departments.html', res=res)


@app.route('/add_department', methods=['POST', 'GET'])
def add_department():
    print(request.form.get('name'))
    dep = Department(name=request.form.get('name'))
    db.session.add(dep)
    db.session.commit()
    return render_template('add_department.html', form='form')
