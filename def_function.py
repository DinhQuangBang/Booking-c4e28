import smtplib
def send_mail(customer_name,customer_phone,customer_email,stadium_district,stadium_name, book_date, book_time, stadium_email):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    mail_address = "hainam110993@gmail.com"
    mail_password = "hainam12"
    confirmation_subject = "Xác nhận đăng kí đặt sân {0} vào lúc {1} ngày {2}".format(stadium_name, book_time, book_date)
    confirmation_message = """Subject: {0}

    Trang web: sanphui.vn xác nhận quý khách: {1} đã đăng kí đặt hẹn sân {2} vào lúc {3} ngày {4}. 
    Nhân viên của sân {2} sẽ sớm liên hệ cho quý khách.""".format(confirmation_subject, customer_name, stadium_name, book_time, book_date)
    notification_subject = "Đăng kí đặt sân của khách {0} vào lúc {1} ngày {2}".format(customer_name, book_time, book_date)
    notification_message = """Subject: {0}

    Khách hàng: {1} đã đăng kí đặt sân {2} vào lúc {3} ngày {4} qua trang web sanphui.vn.
    Vui lòng gọi điện lại cho khách hàng theo số điện thoại: {5} để xác nhận lại.""".format(notification_subject, customer_name, stadium_name, book_time, book_date, customer_phone)
    s.starttls()
    s.login(mail_address, mail_password)
    s.sendmail(mail_address, customer_email, confirmation_message.encode("utf8"))
    s.sendmail(mail_address, stadium_email, notification_message.encode("utf8"))
    s.quit()
    
def send_mail_partnership(partner_name, partner_phone, partner_email, partner_address, partner_note):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    mail_address = "hainam110993@gmail.com"
    mail_password = "hainam12"
    partnership_subject = "Có người muốn hợp tác nè !!!"
    confirmation_message = """Subject: {0}

    Thông tin đối tác:
    Họ tên: {1}
    Số điện thoại: {2}
    Email: {3}
    Địa chỉ: {4}
    Ghi chú: {5}""".format(partnership_subject, partner_name, partner_phone, partner_email, partner_address, partner_note)
    s.starttls()
    s.login(mail_address, mail_password)
    s.sendmail(mail_address, partner_email, confirmation_message.encode("utf8"))
    s.quit()
