from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///articlecard.db'
db = SQLAlchemy(app)


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column('Created', db.DateTime, default=datetime.datetime.now)
    name = db.Column('Author Name', db.String())
    title = db.Column('Title', db.String())
    sub_title = db.Column('Sub-Title', db.String())
    url = db.Column('URL', db.String())
    body = db.Column('Body', db.Text())
    

    def __repr__(self):
        return f'''<Articles (Name: {self.name}
                Title: {self.title} 
                Sub-Title: {self.sub_title}
                Body: {self.body}
                URL: {self.url})'''