from models.dbmodels import *
from datetime import date

# db.create_all()
# d = Department(name='first department')
# db.session.add(d)
# db.session.commit()
#e = Employee(department_id=3,
#             name='Mary',
#             date_of_birth=date(2001, 4, 30),
#             salary=19800)
#db.session.add(e)
#db.session.commit()
a = Department.query.all()
res = db.session.query(Department, Employee).join(Employee).filter(Employee.department_id == 1)
# resdep = Department.query.all()
# print(res[0].date_of_birth)

print(len(a))
for person in res:
   print(person)
