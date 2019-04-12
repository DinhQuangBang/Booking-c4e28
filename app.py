from flask import *
from database import stadium_collection, user_collection
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
    noti = str("")
    user_information = user_collection.find()
    for user_informations in user_information:
        if request.method == "GET":
            return render_template("login.html")
        elif request.method == "POST":
            form = request.form
            phone = form["phone"]
            password = form["password"]
            if phone == user_informations["phone"]: 
                user_detail = user_collection.find_one({"phone":phone})
                if password == user_detail["password"]:
                    return redirect("/")
                else:
                    noti = "Sai Mật Khẩu"
                    return render_template("login.html", noti = noti)
            elif phone != user_informations["phone"]:
                noti = "Số Điện Thoại không tồn tại"
                return render_template("login.html", noti = noti)
                
            
@app.route("/dang-ki", methods = ["GET","POST"])
def register():
    noti = str("")
    user_information = user_collection.find()
    for user_informations in user_information:
        if request.method == "GET":
            return render_template("register.html")
        elif request.method == "POST":
            form = request.form
            name = form["name"]
            phone = form["phone"]
            email = form["email"]
            password = form["password"] 
            re_passwork = form["repassword"]
            if phone == user_informations["phone"]: 
                noti = "Số Điện Thoại đã được đăng kí"
                return render_template("register.html", noti = noti)
            elif email == user_informations["email"]:
                noti = "Email đã được đăng kí"
                return render_template("register.html", noti = noti)
            elif password != re_passwork:
                noti = "Mật khẩu không trùng nhau" 
                return render_template("register.html", noti = noti)
            else:
                new_user = {
                    'name': name,
                    'phone': phone,
                    'email': email,
                    'password': password,
                }
                user_collection.insert_one(new_user)
                return redirect("/dang-nhap")


if __name__ == '__main__':
    app.run(debug=True)
    


    

