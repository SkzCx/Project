import random
import tkinter as tk


eat = {
    "ข้าว": [
        "ข้าวผัดกระเพรา",
        "ข้าวผัดไข่",
        "ข้าวผัดหมู",
        "ข้าวผัดทะเล",
        "ข้าวผัดสับปะรด",
        "ข้าวหมูแดง",
        "ข้าวราดแกงเขียวหวาน",
        "ข้าวต้มปลา",
        "ข้าวยำ"
    ],
    "ก๋วยเตี๋ยว": [
        "ก๋วยเตี๋ยวเรือ",
        "ก๋วยเตี๋ยวผัดไทย",
        "ก๋วยเตี๋ยวต้มยำ",
        "ก๋วยเตี๋ยวหลอด",
        "ก๋วยเตี๋ยวเย็นตาโฟ",
        "ก๋วยเตี๋ยวชามใหญ่"
    ],
    "ผัด": [
        "ผัดกระเพรา",
        "ผัดผงกะหรี่",
        "ผัดเปรี้ยวหวาน",
        "ผัดพริกไทยดำ",
        "ผัดกะเพราไก่",
        "ผัดหมี่กรอบ"
    ],
    "เมนูไข่": [
        "ไข่เจียวหมูสับ",
        "ไข่ดาว",
        "ไข่พะโล้",
        "ไข่เค็ม",
        "ไข่ต้มยำ"
    ],
    "เมนูน้ำ": [
        "ต้มยำกุ้ง",
        "ต้มข่าไก่",
        "ต้มยำปลาน้ำใส",
        "แกงเขียวหวาน",
        "แกงเผ็ด",
        "ต้มยำทะเล"
    ],
    "อาหารทอด": [
        "ไก่ทอด",
        "หมูทอด",
        "ปลาทอด",
        "ปีกไก่ทอด",
        "ทอดมัน",
        "ปลาชุบแป้งทอด"
    ],
    "อาหารจานเดียว": [
        "ข้าวหมูทอดกระเทียม",
        "ข้าวสเต็ก",
        "ข้าวผัดกะเพราไก่",
        "ข้าวราดกะหรี่",
        "ข้าวหน้าไก่",
        "ข้าวหน้าหมูทอด"
    ]
}

def random_food():
    
    category = category_var.get()
    
    if category in eat:
        
        food_choice = random.choice(eat[category])
        output_label.config(text=f"เมนูที่สุ่มมา: {food_choice}")
    else:
        
        output_label.config(text="เลือกหมวดหมู่อาหารให้ถูกต้อง")


food = tk.Tk()
food.title('โปรแกรมสุ่มอาหาร')
food.minsize(width=400, height=300)


title_label = tk.Label(master=food, text='เลือกหมวดหมู่อาหาร:')
title_label.pack(pady=10)


category_var = tk.StringVar()
category_menu = tk.OptionMenu(food, category_var, *eat.keys())
category_menu.pack(pady=10)


ok_button = tk.Button(master=food, text='สุ่มเมนู', command=random_food)
ok_button.pack(pady=20)


output_label = tk.Label(master=food, text='', font=('Arial', 14))
output_label.pack(pady=20)

food.mainloop()
