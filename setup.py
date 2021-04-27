from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
#from models.dbmodels import Department, Employee

app = Flask(__name__)
app.debug = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
app.config['SECRET_KEY'] = 'a really really really really long secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:\\Python\\Python_courses\\final_project\\service\\database.db'
app.config[SQLALCHEMY_TRACK_MODIFICATIONS] = False

from views.views import *

manager = Manager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


# Use 'flask db init' to create migrations

#class Department(db.Model):
#    id = db.Column(db.Integer(), primary_key=True)
#    name = db.Column(db.String(255), nullable=False)
#
#    def __repr__(self):
#        return self.id, self.name
#
#
#class Employee(db.Model):
#    id = db.Column(db.Integer(), primary_key=True)
#    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
#    name = db.Column(db.Integer())
#    date_of_birth = db.Column(db.Date, nullable=False)
#    salary = db.Column(db.Integer())
#
#    def __repr__(self):
#        return self.id, self.department_id, self.name, self.date_of_birth, self.salary


if __name__ == "__main__":
    app.run()
