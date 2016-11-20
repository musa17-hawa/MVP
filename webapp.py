from flask import Flask, render_template, request, redirect, url_for
from flask import session as web_session
app = Flask(__name__)

app.secret_key = ''
#SQLAlchemy stuff
from database import Base, User, Contact #tables
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///Webpage.db')
Base.metadata.create_all(engine) 
DBSession = sessionmaker(bind=engine)
session = DBSession()
#CODE GOES HERE

@app.route('/')
def index ():
	return render_template('index.html')


if __name__ == '__main__':
    app.run(host = "0.0.0.0", debug=True)