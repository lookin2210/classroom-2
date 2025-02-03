items = {
    "หมูสับกิโล": 150,
    "เนื้ออกไก่": 105,
    "ไก่บ้าน(ตัว)": 120,
    "มาม่าต้มยำ": 6.50,
    "ข้าวสาร": 150,
    "น้ำตาล": 20,
    "ปลากะป๋องสามแม่ครัว": 10,
    "ซอสน้ำมัยหอย": 18,
    "ผงชูรส": 10.25,
    "ไข่แผงคละเบอร์": 120.25,
    "ชาเขียว": 21.50,
    "ขนมปังอบเนย": 19,
    "กาแฟ": 15.75,
    "Pepsi": 29.50,
    "ชาไทย": 11.50,
    "น้ำเปล่า": 15.15,
    "น้ำแข็ง": 10
}

total_money = 1000
print("รายการสินค้าพร้อมราคา:")
for idx, (item, price) in enumerate(items.items(), 1):
    print(f"{idx}. {item} - {price} บาท")
selected_items = []
while True:
    try:
        choice = int(input("\nกรุณาเลือกสินค้าจากรายการ (ใส่หมายเลขสินค้า) หรือใส่ 0 เพื่อเสร็จสิ้น: "))
        if choice == 0:
            break
        elif 1 <= choice <= len(items):
            item = list(items.keys())[choice - 1]
            quantity = int(input(f"คุณเลือกซื้อ {item} จำนวน: "))
            selected_items.append((item, quantity))
            print(f"คุณเลือกซื้อ: {item} จำนวน {quantity} ชิ้น")
        else:
            print("กรุณาเลือกหมายเลขสินค้าที่ถูกต้อง.")
    except ValueError:
        print("กรุณาใส่หมายเลขสินค้าเป็นตัวเลข.")
total_cost = sum(items[item] * quantity for item, quantity in selected_items)
change = total_money - total_cost
print("\n--- ผลลัพธ์ ---")
print("รายการสินค้าที่เลือกซื้อ:")
for item, quantity in selected_items:
    print(f"{item} จำนวน {quantity} ชิ้น - {items[item] * quantity} บาท")
   
print(f"\nรวมราคาสินค้าทั้งหมด: {total_cost} บาท")
print(f"เงินที่ใช้ไป: {total_cost} บาท")
print(f"เงินทอน: {change} บาท" if change >= 0 else "ยอดเงินไม่พอในการซื้อสินค้าทั้งหมด.")
