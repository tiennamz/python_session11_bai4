product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7
    }
]

while True:
    choice = input('''
===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====
1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho
2. Bán sản phẩm cho khách hàng
3. Nhập thêm hàng vào kho
4. Xem báo cáo doanh thu
5. Thoát chương trình

Mời bạn nhập lựa chọn: '''
    ).strip()
    
    if choice.isdigit():
        choice = int(choice)
    else:
        print("Hãy nhập 1 số dương 1-5")
        continue
    
    match choice:
        case 1:
            if not product_list:
                print("Danh sách sản phẩm hiện đang trống.")
                continue
            print("Danh sách sản phẩm hiện tại:")
            for index, product in enumerate(product_list,start=1):
                if product.get("quantity") == 0:
                    status = "Hết hàng"
                elif product.get("quantity") <=5:
                    status = "Sắp hết hàng"
                else:
                    status = "Còn hàng"
                    
                print(f"{index}. Mã SP: {product.get("product_id")} | Tên: {product.get("product_name")} | Giá: {product.get("price")} | Tồn kho: {product.get("quantity")} | Đã bán: {product.get("sold")} | Trạng thái: {status}")

        case 2:
            id_input = input("Nhập mã sản phẩm khách muốn mua:").strip().upper()
            is_found = False
            
            for product in product_list:
                if id_input == product.get("product_id"):
                    is_found = True
                    
                    quantity_input = input("Nhập số lượng khách mua: ")
                    if not quantity_input.isdigit() or int(quantity_input) <= 0:
                        print("Số lượng mua không hợp lệ")
                    else:
                        quantity_input = int(quantity_input)
                        if quantity_input > product.get("quantity"):
                            print("Số lượng trong kho không đủ để bán")
                        else:
                            product["quantity"] -= quantity_input
                            product["sold"] += quantity_input
                            
                            print(f"Bạn đã mua {quantity_input} {product.get("product_name")}. Tổng tiền: {quantity_input * product.get("price")}")
                    break
                
            if not is_found:
                print("Không tìm thấy mã sản phẩm")
    
        case 3:
            id_input = input("Nhập mã sản phẩm khách muốn thêm:").strip().upper()
            is_found = False   
                      
            for product in product_list:
                if id_input == product.get("product_id"):
                    is_found = True
                    
                    quantity_input = input("Nhập số lượng nhập thêm: ")
                    if not quantity_input.isdigit() or int(quantity_input) <= 0:
                        print("Nhập kho không hợp lệ")
                    else:
                        quantity_input = int(quantity_input)
                        product["quantity"] += quantity_input
                        print(f"Bạn đã nhập {quantity_input} {product.get("product_name")}.")
                    break
                
            if not is_found:
                print("Không tìm thấy mã sản phẩm")
                
        case 4:
            is_selled = False
            for product in product_list:
                if product.get("sold") > 0:
                    is_selled = True
                    break
            if not is_selled:
                print("Chưa có doanh thu phát sinh.")
                continue
            total_revenue = 0
            max_revenue = 0
            product_max = ""
            print("===== BÁO CÁO DOANH THU CỬA HÀNG YODY =====")
            for index, product in enumerate(product_list,start=1):
                revenue = product.get('sold') * product.get('price')
                if revenue > max_revenue:
                    max_revenue = revenue
                    product_max = product.get("product_name")
                total_revenue += revenue
                print(f"{index}. {product.get("product_name")} | Đã bán: {product.get("sold")} | Doanh thu: {product.get('sold') * product.get('price')}")
            print(f"Tổng doanh thu: {total_revenue}")
            print(f"Sản phẩm bán chạy nhất: {product_max}")
            
        case 5:
            print("Thoát chương trình.Sau đó dừng chương trình.")
            break
        
        case _:
            print("Lỗi cú pháp, vui lòng nhập lại!!!")
            
'''
- Input
    lựa chọn menu
    id sản phẩm 
    số lg
- output
    dữ liệu đã chuẩn hóa
    thông báo thành công hc lỗi
- các hàm cần dùng: remove, get, strip, upper, isdigit, 
- Pseudocode 
- in menu
- nhận lựa chọn 
- 1: hiện ra bảng
- 2: nhập id, ktra id có tồn tại k, có cho mua, không thì báo lỗi
- 3: nhập id, ktra id có tồn tại k, có cho nhập, không thì báo lỗi
- 4: duyệt list xem có cái nào chưa đc mua k, nếu k thì duyệt chạy để lấy doanh thu cùng với max
- 5: thoát
'''
