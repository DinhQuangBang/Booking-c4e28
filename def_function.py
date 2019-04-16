customer_name = "Linh"
customer_phone = "01665160194"
customer_email = "khanhlinh24294@gmail.com"
stadium_district = "Hai Ba Trung"
stadium_name = "san bong"
book_date = "11/04/2019"
book_time = "6:00 - 7:30"
stadium_email = "khanhlinh24294@gmail.com"


def send_mail(customer_name,customer_phone,customer_email,stadium_district,stadium_name, book_date, book_time, stadium_email):
    import smtplib
    s = smtplib.SMTP('smtp.gmail.com', 587)
    mail_address = "hainam110993@gmail.com"
    mail_password = "hainam12"
    confirmation_subject = "Xác nhận đăng kí đặt sân {0} vào lúc {1} ngày {2}".format(stadium_name, book_time, book_date)
    confirmation_message = """Subject: {0}
    Trang web: datsan.vn xác nhận quý khách: {1} đã đăng kí đặt hẹn sân {2} vào lúc {3} ngày {4}. 
    Nhân viên của sân {2} sẽ sớm liên hệ cho quý khách.""".format(confirmation_subject, customer_name, stadium_name, book_time, book_date)
    notification_subject = "Đăng kí đặt sân của khách {0} vào lúc {1} ngày {2}".format(customer_name, book_time, book_date)
    notification_message = """Subject: {0}
    
    Khách hàng: {1} đã đăng kí đặt sân {2} vào lúc {3} ngày {4} qua trang web datsan.vn.
    Vui lòng gọi điện lại cho khách hàng theo số điện thoại: {5} để xác nhận lại.""".format(notification_subject, customer_name, stadium_name, book_time, book_date, customer_phone)

    s.starttls()
    s.login(mail_address, mail_password)
    s.sendmail(mail_address, customer_email, confirmation_message.encode("utf8"))
    s.sendmail(mail_address, stadium_email, notification_message.encode("utf8"))
    s.quit()

# send_mail(customer_name,customer_phone,customer_email,
# stadium_district,
# stadium_name,
# book_date,
# book_time,
# stadium_email,
# )
