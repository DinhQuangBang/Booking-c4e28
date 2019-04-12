from flask import *
import smtplib
from database import form_collection, stadium_collection
from def_function import *
app = Flask(__name__)


@app.route('/booking_form', methods=["GET", "POST"])
def booking():
    if request.method == "GET":
        
        return render_template('booking_form.html')
    elif request.method == "POST":
        form = request.form
        customer_name = form["customer_name"]
        customer_phone = form["customer_phone"]
        customer_email = form["customer_email"]
        stadium_district = form["stadium_district"]
        stadium_name = form["stadium_name"]
        book_date = form["book_date"]
        book_time = form["book_time"]
        stadium_price = form["stadium_price"]
        find_stadium_district = stadium_collection.find_one({"stadium_district": stadium_district})
        stadium_email = find_stadium_district("stadium_email")
        new_form = {
            "customer_name": customer_name,
            "customer_phone": customer_phone,
            "customer_email": customer_email,
            "stadium_district": stadium_district,
            "stadium_name": stadium_name,
            "book_date": book_date,
            "book_time": book_time,
            "stadium_price": stadium_price
        }
        form_collection.insert_one(new_form)
        send_mail(customer_name, customer_phone, customer_email, stadium_district, stadium_name,stadium_email, book_date, book_time)
        
        return redirect('/booking_form/confirmation_booking')

@app.route('/booking_form/confirmation_booking')
def confirmation_booking():
    return render_template('confirmation_booking.html')


if __name__ == '__main__':
  app.run(debug=True)
 