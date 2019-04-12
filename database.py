from pymongo import MongoClient
mongo_uri = "mongodb+srv://admin:admin@booking-z36ui.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri)
form_database = client.submitted_form
form_collection = form_database["form"]
stadium_database = client.stadium_database
stadium_collection = stadium_database["stadium_detail"]

user_database = client.user_database
user_collection = user_database["user_information"]

detail = [
    {
        'stadium_district':	'Hai Bà Trưng',
        'stadium_name': 'Sân bóng ĐH Bách Khoa',
        'stadium_address': 'Lê Thanh Nghị, Bách Khoa', 	
        'stadium_phone': '0438680186',
        'stadium_email': 'hainam11993@gmail.com',
        'stadium_image': 'https://lh3.googleusercontent.com/wYazdvtYYMkj8oBs9X9mnDKhxpuu2Gp7flyJwJN6bPrdqXCM4t02dGiO-Js0pvhxceQM2R4DgM4kxMXRhm3VuYOxUKxNpSiMzYmNWi8TxH2f5k54UU9gv9-L2O_j1Ew9fdsK1vpFTwqIb-oZ_cmxq479Xi4d3J_xGZgrbC44Eh9q3a1S1co-DcjUgvk2GaXxaZmtDRniVmggnhi_1j09z7_UG6QlV3hSbB4TwmFEKYJ3krgroHrnTbLtX_EmQkMkVLiL29DXhOsPh2R7GNvnu-L9YlX5gx0Z9lx7P11X-P3-KhIiHllsT543UkzBxst9Y0YanBhBhNL4ob6kP6IvOy-dQ3K9fBkXb4PM3WfgWg_L4bBIhlJdpGOu4_KwrEqXQey9UPmopiziRgar0jLjOaJMpxOJN7O_pMX8bJdZ2-VExpet0XdnhuEwEZQBnj25UuX0F5k-Fgjdsp1b22gdEFDP2FDsCG1btjX9epHywm4wcKu8QdqSN0vSDPmizYYQbWspUjbgDUWvJNL5rk0kvZ5h09l67efAou3cz3mCZwJALItnEH0_48AkB_Tp0ruHTFGApkIg5EIKUtxkog9pptqtuLaLXTu6fELSsdym4WoQs-VD8iE-uRg7ubAesQb_mj0B7GDCRHmJ_iZf3ELhU2KfI1CKxhg=w960-h720-no',
        'stadium_description': '''Sân bóng cỏ nhân tạo Bách Khoa khá chuyên nghiệp với khán đài bao quanh. Sân bao gồm 4 sân 7 đạt kích thước tiêu chuẩn của FIFA, hệ thống chiếu sáng tốt, mặt sân đẹp. Ban tổ chức sân giảm 30% đối với những đội bóng là học sinh – sinh viên, đặc biệt với sinh viên Bách Khoa là 50%. Có đầy đủ dịch vụ thuê đồ và nước uống. Bên cạnh đó còn rất nhiều dịch vụ khác:
Dịch vụ cho thuê và bán trang phục cầu thủ, giày thể thao
Dịch vụ gửi xe máy, ô tô khép kín
Dịch vụ y tế
Khu vệ sinh, thay đồ''',
    },
    {
        'stadium_district':	'Hai Bà Trưng',
        'stadium_name': 'Sân bóng Hai Bà Trưng',
        'stadium_address': 'Ngõ 104 Nguyễn An Ninh, Trương Định', 	
        'stadium_phone': '0964434433',
        'stadium_email': 'hainam11993@gmail.com',
        'stadium_image': 'https://lh3.googleusercontent.com/OEMfYQNx7g46tKi9L2XsYDh2d0PYhkQYugm48oypQL0mSL82jecfrFQdwqo_VSEGQxF9m9G3qaqGb17TfTD0d6iTu4mjo4epjE2dDotjGa6Zhl3YdopwtUQAxScUHP96x-FjAbBfoC6sYGcbsEga_UsHDoDQbTUmylJYen7qblCSokpVnKZVEbQThW43tre2m5ZiNuBASmPbdHl_-s-JhZhjVrRxtzsozMt4nShQHJLhZn3HOI7I_RiGeXqhQ117bETPvnfkeAXjT1en7RbFDOSpQl7SYhwJ6aSjbS7pS8PSbHtkTJgo7drxD8jc_ixFSc0xMvKx1jTbcIGaOiDDeNo-llkF1HyaqFXca6tBE8VUiygR_GjFwj72qRW7_G93-wd-rmgotC15heHMJMWrUCXc7HUHVeXuu5ngO4XAa26h0T8Nn92XyOyLWksN4HQmXcFNNyzfMhpRk_PpkF102z0YZ7lnRCaKbJ6tl2uMbaB9UlkrWsa-v_jOxnyvSurWWhnIyxpMDSYOBB9WmSx72B3qeMiurNfGXp5mhHSKpNQPoIRQWC4IhT6Tvml0Zv0RS6eT8tKDT0BwKzVNNx5j3dPlE7iI1FrbpDUb2OHkq59bbD3VPlTsFeBKDProV04FG-TBU--vbXHRTmNcotH02xXZeStUz6Q=w870-h515-no',
        'stadium_description': '''Sân bóng Hai Bà Trưng là sân cỏ nhân tạo với diện tích rộng. Chất lượng sân đảm bảo, sạch sẽ, mang lại những buổi đá bóng thú vị và hấp dẫn nhất. Giá thuê sân hợp lí, có nhiều loại sân cho quý khách chọn lựa.''',
    },
    {
        'stadium_district':	'Hai Bà Trưng',
        'stadium_name': 'Sân bóng Thanh Nhàn',
        'stadium_address': 'Đối diện 187 Thanh Nhàn', 	
        'stadium_phone': '0984420372',
        'stadium_email': 'hainam11993@gmail.com',
        'stadium_image': 'https://lh3.googleusercontent.com/p7QE0qc9gaKK2iVvU1vyylutEjoTOOdky2TNGVVCpIeLaldYv8z7FjHb6vOi3morVFiK6TrY1k3ix8iguGjgYPeVgJ8OIdiu3KWVI_eK-9IN-HOS-3UXjb_Cscw7VOCJrRZsaAZEzZK84y3HU25jV36keNWZKJdsaNKf76ghilLX8Z26SMvkCagVAYfK-6uW-D4FQWDl1HCiQcWnhS0kpyRTt1uKyZ1Asz8Nz75RONIPQwMczsGaPmV3aWmkjspEGvZr1x5sPenOgWA5Fpu51B5SrjLMaCeXWuXyaP8lT2rl7qOmHQjH7Bl2LSWQ74po3QXUur1DXjgPG1MO56wk14FuGcJXrXBudiyBupeHfO7EGEspxLFshCXOB5sh0s5lQX3_Z8ocmy7GZi_wLWDEGaOv5X2hmk0Rk_9y5420zZHGiNqUjTnsNAET2ZmqjbhYgTEodTreu63TbqqSE7IxUNehCmvt-I3S5MEBN8gKxjoBhawExM4G2BR9lrB1nuLETgCmT9mgvUOkFi5fR7odrrxtrn4zRYH-Jww2Ai-DDtvoZMKVo-bmDuPq1yz7cJheL6f-qJlXTXkQtOZm0K71agCKzjWDF69EgWuax8uX83CWxKRzmF6W18-980XN_6dyBXaYU0f6kTv7RAlBSSE9QvFntlu7OOQ=w870-h515-no',
        'stadium_description': '''Sân bóng nằm trong khuôn viên công viên Tuổi Trẻ, với 3 sân mặt cỏ, diện tích sân, hệ thống chiếu sáng khá tốt. 
Số lượng sân 7 người: 5 sân
Dịch vụ cung cấp:
Cho thuê và bán quần áo thể thao
Cho thuê và bán giầy thể thao
Dịch vụ ăn uống''',
    },
    {
        'stadium_district':	'Cầu Giấy',
        'stadium_name': 'Sân bóng ĐH sư phạm Hà Nội',
        'stadium_address': '136 Xuân Thủy', 	
        'stadium_phone': '0985112451',
        'stadium_email': 'hainam11993@gmail.com',
        'stadium_image': 'https://lh3.googleusercontent.com/6U4WM4t69kf3faegVJzHjPH-IBcPgzfK8kL-4VsTGl44JOfv6oveOCvqoDDDDGrNmQVPASPVpS8HGDC4ZvE4VhhEEDxFTX5Ir2b8ewFN0b42sO-1IYizUIqCYC-GdDxuK5ZNaso7MCE8EC4b967VRtUyIUdQNYFlfLgqZUIswCURFo-sgTzdeSni7MMveXGYBY0ksTvY4xe4wsClL88mbd100qQYRf1g_7hIOVV-PtqhTl2Mxn9mJ63c9Hjfuu99VvbRd1CAVdlT0Gr32mkP6xj-NExBM5njrurFcQmG5D5xHy-aRBQiHj7KaNs-TYLUAjZiKTOYknPBQlDcAvdOBB-QT7t4ptlFf_nRqs3Ore5RjSxOz2yzNIFph3BZRaNTeg5o4ont_g7taKt6uxl_r0A9wYrAV4uFkrkPHLLADLXthacQcmfSrpP0ZSfAcpdK2yZHdIpNcvVJNojqXxhIilFHE7S1-rrGWT5CY_u1xATFRbFYy2t3SxhvbEI6EEkf6zyQuTSaQrUCEbAEU8PuBc_NA9PRixL562Biz-LdW2F2DBWxa0tg4xCZijfVFUprhiOY9ZxrQ_LKS4BiLPfn6wXMIDvZAC6CL_EWno5ctuuyNeW6Fuy3MrRvOZmKnG7dfYe9unPGlDEr_ZAfELjRm_K5CeVWcaQ=w1250-h937-no',
        'stadium_description': '''Sân bóng trường ĐH sư phạm đã đi vào hoạt động sân kích thước chuẩn, lưới quây xung quanh, hệ thống chiếu sáng 
Cập nhập hiện trạng sân Đh Sư phạm Hà Nội: đèn đã xong, mấy ae đá test bảo sáng quá. Nhà trồng được sao phải nghĩ. Các anh chỉ việc đá tốt, còn chất lượng sân là việc của em. Nhanh tay đặt sân kẻo muộn.''',
    },
    {
        'stadium_district':	'Cầu Giấy',
        'stadium_name': 'Sân Bóng Duy Tân',
        'stadium_address': 'Ngõ 19 Duy Tân (Quận Cầu Giấy, Hà Nội', 	
        'stadium_phone': '0967587588',
        'stadium_email': 'hainam11993@gmail.com',
        'stadium_image': 'https://lh3.googleusercontent.com/cdVPEnSdGzp-NCu_d-KzwN3my4_FSMtm6MEYveByJ_x6tf0iX1veLU4zz5mjF16sxXz0iVia8ENSybQ-Em7FGwOn5S5xYihep3ysEY8b8y6OIIMw3yGT0xXl_RkZd02VShn4vPypc5njuok_jysA6ZJTtCiPAUKi5UyXmgrXoVIm9Zwa-gdm7-WalrQMNOZg8cuCGoINXUWLHmTZrMIxylvJ9glSr3hxWs8NxqN9nsHr-13oPGtBazASBTGzc7MMdajsP-JP9rctGK0nCAkDO-op2F9eaPv_-V4cIzLwDlx5kC49ayQy6nCLGVfTv1C2ROmthXsCbow0TnU98TgBmJKvaKqeeCcgI27Q16VRtUgv4Ms8Vrbqo7SXZIvjWWIapyVO2Os4wi8nG4iTYFTqDnc8mC5EFSG-rm-XUXxcsGB38PW8Ecz0ckl4ByjO4IVMHGsIQgw7UPg-wDcPXksrciHJ6icxKoeeptUlAAuAC5BNjGfWyhKnsfdTPvSDQwJKHYu5rKKUsc6WSMdkIrV8ZK2Npo6nQTuLYLbWKu9hdwdmVSKwTA44DMtXkCkwqG9hGxzTStvsG0jfHr4n9TvZ7HJhLChcMR1KlfBZaUUgSQfigJEwFFbV0b6aCWUNL7sv0Hjm0D0aqweAyVeoZpU-fJWMicunCtg=w960-h720-no',
        'stadium_description': '''Dịch vụ cung cấp:
Cho thuê và bán quần áo thể thao
Cho thuê và bán giầy thể thao
Dịch vụ ăn uống''',
    },
    {
        'stadium_district':	'Thanh Xuân',
        'stadium_name': 'Sân bóng Viettel 1',
        'stadium_address': 'Số 19 ngách 206 ngõ 155 Trường Chinh, Phương Liệt', 	
        'stadium_phone': '0936656669',
        'stadium_email': 'hainam11993@gmail.com',
        'stadium_image': 'https://lh3.googleusercontent.com/C95GB3eeeFaebLGnQ5bP6lt2mmNwMj1WM9VOI6sGmJcw5SHInY1w33bMM-7XioHFkqBjRjq9Rk069stjrRd0Hih6k35G3i0N6R__2h7y7Hm0KShQQbPO805j1IXklW96mR1-7Cc2jmztawD8oewXG7kzgT8z8xsH1U9VpnJA5sOqqRA5ZWi-PhIsCe3eV2Uec_BFtS8R1QfYBnHF3fqz3avvy5W9NM2NsztumOmUiQAIuu7akEMqEUwRoEjz89BAZ5Rc5gz62cOtQHm4Qhz_uppJIqzxWDGyxvbWXxIkUBFbddSfm4MXtj0w656Mz_GbJfKCW80mEvJZSfNsd-iUZuYPbDAu_-S_oTkcp9_3ojoJtSXclBXm3uXKm6ntdLwvmL5FiCAZiNsG58jQvgJxgo6JDnh_EROVnREusmlqTxJNPeVEQJiyeR5N-mLrvdeWOQo65_lIhZl03nFp0ippGEcJEqNUA6jFORlyYCtppGLQRIQEqf_OJNa_4gvyar_CngaZwGb-n5MckZELasrduxDRKa9vgSdl0OZppIJZMgNnHRrA1i2MUKp-LKcukZwFUrZyUGFr3ft-mbhH3d2VIjgXAIVxFox9bKgOdz6trl46qTuPWPpyj9t4yqDkbV4u8xpZU5Je9O7gKTLrKCOUSEQ1LDf1abk=w960-h717-no',
        'stadium_description': '''Sân bóng Viettel Số 19 ngách 206 ngõ 155 Trường Chinh, Phương Liệt, được xây dựng đạt tiêu chuẩn quốc gia sân cỏ nhân tạo. 
Dịch vụ sân đa dạng, chu đáo, an ninh tốt.Giá cả bình dân, hợp lý. Nhân viên sân nhanh nhẹn, nhiệt tình.''',
    },
    {
        'stadium_district':	'Thanh Xuân',
        'stadium_name': 'Sân bóng Viettel 2',
        'stadium_address': 'Ngõ 155, Ngách 155/206 Trường Chinh - Cầu Phương Liệt', 	
        'stadium_phone': '0936656669',
        'stadium_email': 'hainam11993@gmail.com',
        'stadium_image': 'https://lh3.googleusercontent.com/Zb8Ge4f-5olPapnVUUL8-KA4gUx1veH7qYo-pzuVtZ7Vy03SHDOpF5eJHeol_8YsPP25O2Gme4NioH2Cm4bW5jRqyrkR14vagrNtzKVxvp9JNWOuIi5UiYJIKTJ7wnmITs15b7jLk38AIqESfy9NXuMLQP0fcSk0SE_GkbBLL3REu74pddD8zgN8Q_WLPgZBKmip7pOz537FN7aieiBJF7Xmv9CArkpgNBtsqXe4VPVCOhFUirmZ677SlVKZlYXfhq3mWGm9MLPcFZYMUp5qJUJDxNQ6Nzw36qIvPYGLcsD7nLdJ9Qc2a_LR6B4S5oz0jVPBcC5q9DnEsIpW9h4wG4cfn0CQY2-gQuLZo4AQd2zSbahVU-7bOStb91MUiyaeMA03rjMQ0jdagxFXAEXjuAIV9m6R_9Z7ZjTKJ3xiEGHj0_7_we8V0e1mdl2l_sGmileSiS0GfiG_JDibbd9m5Y5p4Mw7SNETMnWjkfPu9UgPaVd6e3NZKi3TzaXbhsUYzqxvpW7RLDVQNtCDcdkCnyF_l2gfXpeNztwgsBmf72BqLG1o5Ze3omWeTRYfCcNSVCLcMuyS4JCLVhLgvG5Ys6d3m9z8t_sKYeRU12Cm-0_2SRolLa9Nyocsd_i8VXlhMSynlxlhokgrfZu_VYhIop7mHdXOIUE=w529-h387-no',
        'stadium_description': '''Sân bóng là trung tâm thể thao quân đội gồm 2 sân khá, hệ thống chiếu sáng, măt cỏ, diện tích tốt. Sân nằm cuối ngách 155/206 Trường Chinh. Bên ngoài là 2 sân Viettel 1 và Viettel 2
THÔNG TIN CHI TIẾT
- Giới thiệu chung: Sân bóng Viettel 2, được xây dựng và hoàn thành vào năm 2009, bao gồm 12 sân cỏ nhân tạo ( diện tich sân 30m x 45m ), có thể hỗ trợ các loại sân 7,9,11 người.
- Đồ hỗ trợ bóng đá: Có cho thuê hầu hết các dụng cụ bóng đá cần thiết như : Giầy, bóng, lót chân…
- Đánh giá chung và một số hình ảnh về sân:
+ Ưu điểm: Canteen khá rộng có thể chứa được nhiều người, bãi để xe thoáng, đèn điện vào buổi tối rất sáng.
+ Hạn chế: Chất lượng mặt sân ở mức bình thường, lối đi vào khá khó đi đặc biệt là khi trời mưa.''',
    },
    {
        'stadium_district':	'Thanh Xuân',
        'stadium_name': 'Sân bóng cỏ nhân tạo VSA1',
        'stadium_address': '5d Lê Trọng Tấn', 	
        'stadium_phone': '0977641696',
        'stadium_email': 'hainam11993@gmail.com',
        'stadium_image': 'https://lh3.googleusercontent.com/xdEInE-VGuWAeJgHEm2TP-knB6wVkNXCbIa1zl8jyWWgOTfjDJo5_9GHS9p-kw7EVWfISlb-TYFvHOj1aCMMIVTz9SDamMKPWfcU_OBJm1L0BJ0pHHpXsd2GSqTd7LsUMhDl-_IoSdYaIX71vD12EB41-YqyqBkbfhl3BGibn-nzLe_PfaYyed7o8Gj91N9RWHeSOducB0wnhqBupZhAPYpVZ5TfZPeLvjFV7n4oDiCcDMdgXwRm0BHVUARqW8hkeaF3JJF7iQpTORbpZAv0-AvRMQLXTSWmSrvenCTsLRsDeTngsVEbZXoirl0MXV9kYncwfOyod077zvb0CmwUE-Vv_VtTQemv1CvY5R3cPizEhMcDvh9SVlSKe-bmktvyGl1NKR-4sE8uKsqYSbEyY4m2GwEuAGmsGZYo4oYnZusUPAZ5EK0kOf9ywKC1wMEgfvhg5iRPukC6NLQ4v_14Qq7gqB88OTVCe4HRfCWriMMiwGeenRR8onP-ycIIhCbjwXKbCp9KBko8m5uD5pnGVhc-pSw7apYd0_GIQAsnszIPE8M9WxEl73udFgxQR9Kx_LjBoua8J4D-Lx_hG-7WHIwlyjt3y0V_GpB6EIz3BtoLziff_YxB7OKzCm3g8xybLLM12a7PH8-UpKsqho9jCEWYYnJ1bUU=w1250-h937-no',
        'stadium_description': '''Cụm 6 sân 7 kích thước 32x52m (tổng diện tích sân bóng đá Cỏ nhân tạo là gần 10000 m2)
Cho thuê Sân đá bóng phục vụ tất cả các ngày trong tuần. Sân mới mở nên cỏ còn rất mới. Có bãi đậu xe oto . Rất mong anh em yêu đá bóng ủng hộ''',
    },
    {
        'stadium_district':	'Nam Từ Liêm',
        'stadium_name': 'Sân bóng Phạm Văn Đồng 3',
        'stadium_address': '232 Phạm Văn Đồng, Cạnh tòa nhà Bộ Công an', 	
        'stadium_phone': '0947200456',
        'stadium_email': 'hainam11993@gmail.com',
        'stadium_image': 'https://lh3.googleusercontent.com/zQN6uukZ5gVbD9R2KQrVWGWi0CcOv3XL9_RMrBnf4VFuN6uNP6xuRFcSeJPAtM_x68VE8TPoNJ2_3V-a5XnPP3HBd7gQrR2ev4-jlgen69eyFXMEk1BQY7GIuHgtVovLAyISa7Ch2HXw9ZklfM3e49c2ljAJeyG6F3yQiNPrgHxwN5pmxgC9rNEVlACsk4j2XqM7GqET104AI-mx5ZiGY2_wIv28vT7MQqhX-6rCLKCDtfj_dh22sh5OZY_BOeUihkT6rN9xmxznkdj54b_Zd0JjDYindbPhcD1zudNpMATkkkwTf3P5AG_o1wdPD3Z_9fCuGROZfWV4Y-LFxBPgxlMjdVqKJOJF5U2Z8EM129FFYA_TzfiFwLLhB4DpY1dazJ37tgJv7-n8hFCqqCNoXEPM-u19zpHhCRWRMmFG_btnF7MWIQFqAqpuGNh3zRqf2n83qMT55cHj_3NF45ZiSPfPK1N_1AdWC0xxhMDGBwgxmJ6BN96o-5oMt2DBk3-mT0l0d6uQyqGm81wrubWjcq86rV3C3RMghmDKgWWXUM7_97voInDAYlT0nhIHlf49I6J-I235d3XZ5OTDyijEwnb2MxJ8vfV3TyUWhvbL3nli48HlrrpT5sNwnRKggFohcOdmakByfDtq8m3ouu27Ov4klbTHJzQ=w1250-h937-no',
        'stadium_description': '''Sân 7-11 người mới khai trương
Sân mới ở cạnh tòa nhà Bộ Công an, kích thước tiêu chuẩn, điện cực sáng''',
    },
    {
        'stadium_district':	'Nam Từ Liêm',
        'stadium_name': 'Sân bóng Mỹ Đình 2',
        'stadium_address': 'P2 Lê Quang Đạo, Mỹ Đình', 	
        'stadium_phone': '0966116365',
        'stadium_email': 'hainam11993@gmail.com',
        'stadium_image': 'https://lh3.googleusercontent.com/cqnhY6prnQp9RcPqeHk2jUwLsgPuGS7XP6-ClJouZJPrOdYMAmVEzAD8MKehips-Eg5N6RWgMKl_mrsTvJ0_aiK_q8YMtEJRg6-v0lNV1LUyJrqhnQcqXpG9-SI1niO9-NYphuNNUO-t50MO95x3Aaf2V7m-k1fcRBySsLKJsf58cFeRVzwBGvG1_kyrWR81HlETxswIWaBJ-_rx-B3ejoNR3h1gVbattkNSF-osrJ0zlyHnuLCQb3MUCZMhOobwTL7o1_bSYWZij7lgSiOjHD1GGpcUnozbxrvU4UizhB9QZrGhkPmsB1D2xmIfyiJPMDytSXktQdEbG01suG-edfbwA48RgfcJwifknnzFSFfYftbRjaOd6MPH89yk4LPFsvBOEDi-Ltr0K7XFVPjzxiCm9ArEhTTSEcgbFFjHUpyOo9Ugb_zw358lJoL1IYnUh9mmmxjvLsvjwCNQtxqOyJkwif5XU_t55oGPRKKiEXJAZVBRF7jGYh9SyMqOXrDT2QiI_TtKWOzR5OF0WLnxNJbbQ72gi0tgo3Hw54n3RqHvFcLiJ0EtD5B4piHFMHTK1VLfm1ycgEO-UjRmCBFT6DAKmBnIUqx2B6u3LVFlhmhLPLqxad5UPJcoraBfttrbvn66Fw3NLMof-RhnLcKzYEIJXel84lE=w960-h722-no',
        'stadium_description': '''Sân bóng đá MỸ ĐÌNH 2 bao gồm 3 sân 7 với kích thước rộng tiêu chuẩn 25,8m x 48,5m ghép thành sân lớn. 
- Sân bóng đá MỸ ĐÌNH 2 được đầu tư hệ thống ánh sáng hoàn thiện và kiên cố, đảm bảo ánh sáng khi chơi vào buổi tối..''',
},
]
stadium_collection.insert_many(detail)
