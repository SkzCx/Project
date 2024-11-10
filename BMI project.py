import tkinter as tk

def show_output(): 
    weight = int(weight_input.get())
    height = int(height_input.get())

    output = ((weight / height)**2)*100     

    outputBMI_label.configure(text=f'{output:0.2f}')

def show_output1():
    weight = int(weight_input.get())
    height = int(height_input.get())

    output = ((weight / height)**2)*100

    if output < 18.50:
     result_text = f'BMI: {output:0.2f} - น้ำหนักน้อย / ผอม'
    elif 18.50 <= output <= 22.50 :
        result_text = f'BMI: {output:0.2f} - ปกติ (สุขภาพดี)'
    elif 23 <= output <= 24.90 :
        result_text = f'BMI: {output:0.2f} - ท้วม / โรคอ้วนระดับ 1'
    elif 25 <= output <= 29.90 :
        result_text = f'BMI: {output:0.2f} - ท้วม / โรคอ้วนระดับ 2'
    elif output >  30 :
        result_text = f'BMI: {output:0.2f} - อ้วนมาก / โรคอ้วนระดับ 3'

    outputtitle_label.configure(text=result_text)


project = tk.Tk()
project.title('โปรเเกรมคํานวณ BMI')
project.minsize(width=250, height=200)


title_label=tk.Label(master=project, text='คํานวณ BMI')
title_label.pack()


weight_input=tk.Label(master=project, text='กรุณากรอกนํ้าหนัก (กิโลกรัม)')
weight_input.pack()
weight_input=tk.Entry(master=project)
weight_input.pack()


height_input=tk.Label(master=project, text='กรุณากรอกส่วนสูง (เซนติเมตร)')
height_input.pack()
height_input=tk.Entry(master=project)
height_input.pack()


ok_button=tk.Button(master=project, text='คํานวณBMI', command=lambda:[show_output(), show_output1()])
ok_button.pack()


outputBMI_label=tk.Label(master=project)
outputBMI_label.pack() 

outputtitle_label=tk.Label(master=project)
outputtitle_label.pack()


project.mainloop()