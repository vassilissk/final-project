from flask import render_template, url_for, request, redirect
from setup import app, db
from models.dbmodels import Department, Employee
from datetime import datetime, date


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
            salary_list.append(round(sum_salary / counter, 2))
        else:
            salary_list.append(0)
    print(res)
    result = zip(res, salary_list)
    return render_template('departments.html', result=result)


@app.route('/add_dep', methods=['POST', 'GET'])
def add_dep():
    print(request.method)
    if request.method == 'POST':
        print(request.form)
        dep = Department(name=request.form.get('name', False))
        db.session.add(dep)
        db.session.commit()
        return redirect('departments')
    return render_template('add_dep.html')


@app.route('/edit_dep/<dep_id>', methods=['POST', 'GET'])
def edit_dep(dep_id):
    edited_dep = Department.query.filter(Department.id == dep_id)[0]
    if request.method == 'POST':
        dep = Department(name=request.form.get('name', False))
        edited_dep.name = dep.name
        db.session.commit()

        return redirect(url_for('departments'))
    return render_template('edit_dep.html', dep_name=edited_dep.name)


@app.route('/department/<dep_id>')
def department(dep_id):
    res = Employee.query.filter(Employee.department_id == dep_id)
    return render_template('department.html', dep_id=dep_id, res=res)


@app.route('/profile/<user_id>')
def profile(user_id):
    res = Employee.query.filter(Employee.id == user_id)
    print(res)
    return render_template('profile.html', res=res[0])


@app.route('/del_dep/<dep_id>', methods=['GET'])
def del_dep(dep_id):
    res = Employee.query.filter(Employee.department_id == dep_id)
    for i in res:
        db.session.delete(i)
    db.session.commit()
    res = Department.query.filter(Department.id == dep_id)
    db.session.delete(res[0])
    db.session.commit()

    return redirect(url_for('departments', dep_id=dep_id))


@app.route('/department/<dep_id>/add_employee', methods=['POST', 'GET'])
def add_employee(dep_id):
    if request.method == 'POST':
        employee = Employee(department_id=dep_id,
                            name=request.form.get('name', False),
                            date_of_birth=datetime.strptime(request.form.get('birth'), '%Y-%m-%d'),
                            salary=request.form.get('salary', False)
                            )
        db.session.add(employee)
        db.session.commit()
        print(employee.name, type(employee.date_of_birth), employee.department_id, employee.salary)
        return redirect(url_for('department', dep_id=dep_id))
    return render_template('add_employee.html')


@app.route('/del_profile/<profile_id>', methods=['POST', 'GET'])
def del_profile(profile_id):
    res = Employee.query.filter(Employee.id == profile_id)
    print(res[0].id)
    temp = res[0].department_id
    db.session.delete(res[0])
    db.session.commit()
    return redirect(url_for('department', dep_id=temp))


@app.route('/edit_profile/<profile_id>', methods=['POST', 'GET'])
def edit_profile(profile_id):
    edited_profile = Employee.query.filter(Employee.id == profile_id)[0]
    if request.method == 'POST':
        print('request.form= ', request.form)

        profile = Employee(department_id=request.form.get('department', False),
                           name=request.form.get('name', False),
                           date_of_birth=datetime.strptime(request.form.get('birth'), '%Y-%m-%d'),
                           salary=request.form.get('salary', False))

        edited_profile.name = profile.name
        edited_profile.department_id = profile.department_id
        edited_profile.date_of_birth = profile.date_of_birth
        edited_profile.salary = profile.salary

        db.session.commit()
        # db.session.close()
        return redirect(url_for('profile', user_id=profile_id))
    return render_template('edit_profile.html', name=edited_profile.name,
                           department_id=edited_profile.department_id,
                           date_of_birth=edited_profile.date_of_birth,
                           salary=edited_profile.salary)


@app.route('/search/<dep_id>', methods=['POST', 'GET'])
def search(dep_id):
    print(dep_id)
    first = request.form.get('first', False)
    second = request.form.get('second', False)
    if second:
        res = Employee.query.filter(Employee.department_id == dep_id).\
            filter(Employee.date_of_birth >= first).\
            filter(Employee.date_of_birth <= second)
    else:
        res = Employee.query.filter(Employee.department_id == dep_id). \
            filter(Employee.date_of_birth == first)
    for i in res:
        print(i)
    return render_template('search.html', res=res)
