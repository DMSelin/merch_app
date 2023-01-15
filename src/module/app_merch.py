import tkinter as tk 

mainwindow = tk.Tk()
mainwindow.title('merch app')
mainwindow.geometry('500x600')
mainwindow.resizable(width=False, height=False)

frame_menu = tk.Frame(mainwindow, width=200, height=300, bg='#E0FFFF')
frame_menu.grid(row=0, column=0)

frame_choice = tk.Frame(mainwindow, width=300, height=300, bg='#FFEBCD')
frame_choice.grid(row=0, column=1)

frame_changes = tk.Frame(mainwindow, width=500, height=300, bg='#DCDCDC')
frame_changes.grid(row=1, column=0, columnspan=2)

l_routs = tk.Label(frame_menu, text='Маршруты').pack(expand=1)
l_report = tk.Label(frame_menu, text='Отчет').pack(expand=1)
l_positions = tk.Label(frame_menu,text='Позиции').pack()



mainwindow.mainloop()