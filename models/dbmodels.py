from setup import db
from datetime import *


class Department(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return self.name


class Employee(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    name = db.Column(db.Integer())
    date_of_birth = db.Column(db.Date, nullable=False)
    salary = db.Column(db.Integer())

    def __repr__(self):
        return str(self.id)+' '+self.name+' '+str(self.date_of_birth)+' '+str(self.salary)+' '+str(self.department_id)
