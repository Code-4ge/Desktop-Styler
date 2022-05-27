from tkinter import *
from settings import *
import datetime

desk = Tk()
desk.title("Desktop Styler")
desk.overrideredirect(1)
desk.iconbitmap("Styler_logo.ico")
desk.wm_attributes("-transparentcolor", "white")
desk.geometry("%dx%d+-8+20" %(desk.winfo_screenwidth(), desk.winfo_screenheight()))
desk.config(bg="white")

day_list = ["SUN", "MON", "TUE", "WED", "THR", "FRI","SAT"]
quote = ["\" Don't Stop Until You're Proud \"\n- Anna Colibri"]

def time_date():
    get_time = datetime.datetime.now()
    day_now = day_list[(int(get_time.day) % 7)-1]
    dayShow.config(text=day_now)
    date_now = get_time.strftime("%B %d, %Y")
    dateShow.config(text=date_now)
    time_now = get_time.strftime("%I:%M %p")
    TimeShow.config(text=time_now)
    TimeShow.after(1000,time_date)


line = Canvas(desk, width=100, height=150, bg="white", highlightthickness=0)
line.create_line(100, 0, 0, 150, fill=TEXT_COLOR, width=2)
line.pack()
line.place(x=589, y=100)


dayShow = Label(desk, font=('"{}" 55' .format(DAY_FONT)), bg="white", fg=TEXT_COLOR)
dayShow.pack(anchor="center")
dayShow.place(x=490, y=125)

points=[30, 0, 200, 0, 200, 45, 0, 45]
polygon = Canvas(desk, width=200, height=45, bg="white", highlightthickness=0)
polygon.create_polygon(points, fill=TEXT_COLOR)
polygon.pack()
polygon.place(x=680, y=115)

TimeShow = Label(desk, font=('"{}" 25' .format(TIME_FONT)), bg=TEXT_COLOR, fg="white")
TimeShow.pack(anchor="center", pady=10)
TimeShow.place(x=715, y=115)

dateShow = Label(desk, font=('"{}" 20' .format(DATE_FONT)), bg="white", fg=TEXT_COLOR)
dateShow.pack(anchor="center")
dateShow.place(x=660, y=175)

quoteShow = Label(desk, text=quote[0], font=('"{}" 10' .format(QUOTE_FONT)), bg="white", fg=TEXT_COLOR, justify=LEFT)
quoteShow.pack()
quoteShow.place(x=635, y=220)

time_date()

desk.mainloop()