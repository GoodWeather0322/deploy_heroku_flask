from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgres://elfclzrpukiuxw:595d934771e1b017c13dda2b174222a2569c098e2ba4ca2c1998abf01bc49878@ec2-54-225-230-142.compute-1.amazonaws.com:5432/d44ab577jjljcb'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class UserData(db.Model):
    __tablename__ = 'UserData'

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64))
    Description = db.Column(db.String(256))
    CreateDate = db.Column(db.DateTime)

    def __init__(self
                 , Name
                 , Description
                 , CreateDate
                 ):
        self.Name = Name
        self.Description = Description
        self.CreateDate = CreateDate


if __name__ == '__main__':
    manager.run()
