from flask import *
from database import stadium_collection
from bson.objectid import ObjectId

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("homepage.html") 

@app.route("/san-bong")
def all_stadium():
    all_stadium = stadium_collection.find()
    return render_template('detail_district.html', all_stadium = all_stadium)

@app.route("/san-bong/<stadium_district>")
def detail_district(stadium_district):
    detail_district = stadium_collection.find({"stadium_district": stadium_district})
    return render_template('detail_district.html', detail_district = detail_district)
    
@app.route("/san-bong/<stadium_district>/<id>")
def detail_stadium(stadium_district,id):
    detail_stadium = stadium_collection.find_one({"_id": ObjectId(id)})
    return render_template("detail_stadium.html", detail_stadium = detail_stadium)

@app.route("/dat-san", methods = ["GET","POST"])
def booking_form():
    if request.method == "GET":
        return render_template("booking_form.html")
    elif request.method == "POST":
        form = request.form
        customer_name = form['name']
        customer_phone = form['phone']
        customer_email = form['email']
        return redirect("detail_stadium.html")
    
@app.route("/dang-nhap", methods = ["GET","POST"])
def login():
    # if not session["logged"]: #chua dang nhap
        if request.method == "GET":
            return render_template("login.html")
        elif request.method == "POST":
            form = request.form
            username = form["username"]
            password = form["password"]
            # if username == "adminc4e" and password == "adminc4e":
                # session["logged"] = True
            return redirect("/")
    #         else:
    #             return redirect("/login")
    # else: #dang nhap roi
    #     return redirect("/all-service")

@app.route("/dang-ki", methods = ["GET","POST"])
def register():
    # if not session["logged"]: #chua dang nhap
        if request.method == "GET":
            return render_template("register.html")
        elif request.method == "POST":
            form = request.form
            username = form["username"]
            password = form["password"]  
            return redirect("/all-service")
    

if __name__ == '__main__':
    app.run(debug=True)
    

