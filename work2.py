province = ["กรุงเทพมหานคร", "กาฬสินธุ์", "กาญจนบุรี", "จันทบุรี", "ฉะเชิงเทรา", 
            "ชลบุรี", "พะเยา", "ชุมพร", "ชัยนาท", "ขอนแก่น", "ชัยภูมิ", 
            "ยโสธร", "นครพนม", "นครราชสีมา", "เชียงใหม่"]
province[province.index("กรุงเทพมหานคร")] = "Bangkok"
province[province.index("นครราชสีมา")] = "Korat"
province[province.index("ฉะเชิงเทรา")] = "Paet Row"
province[province.index("ชลบุรี")] = "Chon buri"
province[province.index("ชุมพร")] = "Chum porn"

print(province)
