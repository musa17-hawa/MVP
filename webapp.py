from flask import Flask, render_template, request, redirect, url_for
from flask import session as web_session
app = Flask(__name__)

app.secret_key = ''
#SQLAlchemy stuff
from database import Base, Item, Contact #tables
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///Webpage.db')
Base.metadata.create_all(engine) 
DBSession = sessionmaker(bind=engine)
session = DBSession()
#CODE GOES HERE

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/helmets')
def helmets():
	return render_template('index.html')

@app.route('/helmets/item/<int:item_id>', methods = ['GET', 'POST'])
def item(item_id):
	if request.method == 'GET':
		itm = session.query(Item).filter_by(id = item_id).first()
		return render_template("item.html", itm = itm, item_id = itm.id)
	else:	
		itm = session.query(Item).filter_by(id = item_id).first()
		return render_template("item.html", itm = itm, item_id = itm.id)

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
	if request.method == 'GET':
		return render_template('upload.html')
	else:
		new_itmname = request.form['itmname']
		new_itmprice = request.form['itmprice']
		new_itmdis = request.form['itmdis']
		new_itmpic = request.form['itmpic']

		itm = Item(itmname = new_itmname, itmprice = new_itmprice, itmpic = new_itmpic, itmdis = new_itmdis)
		session.add(itm)
		session.commit()
		return redirect(url_for('item', item_id = itm.id))



if __name__ == '__main__':
    app.run(host = "0.0.0.0", debug = True)