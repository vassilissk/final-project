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
    salary_list = []
    for dep in res:
        sum_salary = 0
        counter = 0
        list_of_employees = Employee.query.filter(Employee.department_id == dep.id)
        print('--------------')
        for i in list_of_employees:
            sum_salary += i.salary
            counter += 1
        if counter != 0:
            salary_list.append(round(sum_salary/counter, 2))
        else:
            salary_list.append(0)
    print(res)
    result = zip(res, salary_list)
    return render_template('departments.html', result=result)


@app.route('/add_dep', methods=['POST', 'GET'])
def add_dep():
    if request.method == 'POST':
        print(request.form)
        dep = Department(name=request.form.get('first', False))
        db.session.add(dep)
        db.session.commit()

    return render_template('add_dep.html')


@app.route('/edit_dep', methods=['POST', 'GET'])
def edit_dep():
    if request.method == 'POST':
        print(request.form)
        dep = Department(name=request.form.get('first', False))
        db.session.add(dep)
        db.session.commit()

    return render_template('edit_dep.html')


@app.route('/department/<dep_id>')
def department(dep_id):
    res = Employee.query.filter(Employee.department_id == dep_id)
    return render_template('department.html', dep_id=dep_id, res=res)


@app.route('/profile/<user_id>')
def profile(user_id):
    res = Employee.query.filter(Employee.id == user_id)
    print(res)
    return render_template('profile.html', res=res[0])


@app.route('/del_dep/<dep_id>', methods=['POST', 'GET'])
def del_dep(dep_id):
    res = Department.query.filter(Department.id == dep_id)
    db.session.delete(res[0])
    db.session.commit()
    return redirect(url_for('departments', dep_id=dep_id))
