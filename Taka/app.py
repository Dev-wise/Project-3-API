from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/enternew')
def add_new():
	return render_template('addnew.html')


@app.route('/addrec', methods=["POST","GET"])
def addrec():
	if request.method == 'POST':
		try:
			name = request.form['name']
			brand = request.form['brand_name']
			reg_p_v = request.form['regular_price_value']
			offer_p_v = request.form['offer_price_value']
			curr = request.form['currency']
			cl1 = request.form['classification_l1']
			cl2 = request.form['classification_l2']
			cl3 = request.form['classification_l3']
			cl4 = request.form['classification_l4']
			
			with sqlite3.connect("db/GDT_1.db") as conn:
				c = conn.cursor()
				c.execute("""INSERT INTO GreenDeck 
					(name,brand_name,regular_price_value,offer_price_value,currency,classification_l1,
					classification_l2,classification_l3,classification_l4) VALUES(?,?,?,?,?,?,?,?,?)
					""",(name,brand,reg_p_v,offer_p_v,curr,cl1,cl2,cl3,cl4))
				conn.commit()

				msg="Sucess "
		except:
			conn.rollback()
			msg = "Error in operation"

		finally:
			return render_template("result.html",msg=msg)

@app.route('/list')
def list():
	conn = sqlite3.connect("db/GDT_1.db")
	conn.row_factory = sqlite3.Row
	c = conn.cursor()
	c.execute("SELECT * FROM GreenDeck")
	rows = c.fetchall()
	return render_template("list.html",rows=rows)


@app.route('/delete_item')
def delete_this():
	return render_template('del_sub.html')

@app.route('/delete',methods=["POST"])
def delete():
	try:
		name = request.form['Name']
		#msg = name
		conn = sqlite3.connect("db/GDT_1.db")
		#conn.row_factory = sqlite3.Row
		c = conn.cursor()
		#name=name
		c.execute("DELETE FROM GreenDeck WHERE Name=?",(name,))
		conn.commit()
		msg = "success"
	except:	
		conn.rollback()
		msg="Error"
	finally:
		return render_template("result.html",msg=msg)

if __name__=='__main__':
	app.run(host='0.0.0.0')d