from flask import render_template, url_for, request, redirect
from setup import app, db
from models.dbmodels import Department, Employee


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


@app.route('/add_dep', methods=['POST', 'GET'])
def add_dep():
    if request.method == 'POST':
        print(request.form)
        dep = Department(name=request.form.get('first', False))
        db.session.add(dep)
        db.session.commit()

    return render_template('add_dep.html')


@app.route('/department/<dep_id>')
def department(dep_id):
    res = Employee.query.filter(Employee.department_id == dep_id)
    for i in res:
        print(i)
    return render_template('department.html', dep_id=dep_id, res=res)


@app.route('/profile/<user_id>')
def profile(user_id):
    res = Employee.query.filter(Employee.id == user_id)
    print(res)
    return render_template('profile.html', res=res[0])
