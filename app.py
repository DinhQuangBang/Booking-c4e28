from flask import *
from database import stadium_collection, user_collection, form_collection, partnership_collection
from bson.objectid import ObjectId
from def_function import *

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

@app.route("/dang-ky-dat-san/<id>", methods = ["GET","POST"])
def booking_form(id):
    noti = str("")
    detail_stadium = stadium_collection.find_one({"_id": ObjectId(id)})
    if request.method == "GET":
        return render_template("booking_form.html", detail_stadium = detail_stadium)
    elif request.method == "POST":
        form = request.form
        customer_name = form["name"]
        customer_phone = form["phone"]
        customer_email = form["email"]
        book_date = form["date"]
        book_time = form["time"]
        if book_time == "16:00-17:30":
            price = "600.000vnđ"
        elif book_time == "17:30-19:00" or book_time == "19:00-20:30":
            price = "800.000vnđ"
        elif book_time == '20:30-22:00':
            price = "400.000vnđ"
        else: 
            price = "300.000vnđ"

        if book_date == "":
            noti = "Bạn chưa chọn Ngày"
            return render_template("booking_form.html", noti = noti, detail_stadium = detail_stadium)
        elif book_time == "0":
            noti = "Bạn chưa chọn Thời Gian"
            return render_template("booking_form.html", noti = noti, detail_stadium = detail_stadium)
        elif customer_name == "":
            noti = "Bạn chưa nhập Tên"
            return render_template("booking_form.html", noti = noti, detail_stadium = detail_stadium)
        elif customer_phone == "":
            noti = "Bạn chưa nhập Số Điện Thoại"
            return render_template("booking_form.html", noti = noti, detail_stadium = detail_stadium)
        elif customer_email == "":
            noti = "Bạn chưa nhập Email"
            return render_template("booking_form.html", noti = noti, detail_stadium = detail_stadium)
        else:
            new_form = {
                "stadium_name": detail_stadium["stadium_name"],
                "stadium_address": detail_stadium["stadium_address"],
                "customer_name": customer_name,
                "customer_phone": customer_phone,
                "customer_email": customer_email,
                "book_date": book_date,
                "book_time": book_time,
                "stadium_price": price,
            }
            form_collection.insert_one(new_form)
            # send_mail(customer_name, customer_phone, customer_email, stadium_name, stadium_address, book_date, book_time)

            return redirect("/dat-lich-thanh-cong")

@app.route('/dat-lich-thanh-cong')
def confirmation_booking():
    return render_template('confirmation_booking.html')

@app.route('/dang-ky-hop-tac', methods = ["GET","POST"])
def partnership_register():
    if request.method == "GET":
        return render_template("partnership.html")
    elif request.method == "POST":
        form = request.form
        partner_name = form["partner_name"]
        partner_phone = form["partner_phone"]
        partner_email = form["partner_email"]
        partner_address = form["partner_address"]
        partner_note = form["partner_note"]
        new_form = {
            "partner_name": partner_name,
            "partner_email": partner_email,
            "partner_phone": partner_phone,
            "partner_address": partner_address,
            "partner_note": partner_note
        }
        partnership_collection.insert_one(new_form)
        send_mail_partnership(partner_name, partner_phone, partner_email, partner_address, partner_note)
        return redirect('/dang-ky-thanh-cong')

@app.route('/dang-ky-thanh-cong')
def confirmation_registration():
    return render_template('confirmation_registration.html')
    
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
