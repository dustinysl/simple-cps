from tkinter import *
import time, threading

window = Tk()
window.title("CPS TEST 1")
window.geometry("1000x900")

count = 0
start_state = DISABLED
def onclick():
    global count
    count += 1
    print(count)

def start():
    click_button.config(state=ACTIVE)
    timer()

def timer():
    def run():
        global duration
        start_time = time.time()
        duration = 10
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time > duration:
                timer_label.config(text="Time's up!")
                stop()
                break
            timer_label.config(text=f"Time: {elapsed_time:.2f} sec")
            time.sleep(0.1)


    thread = threading.Thread(target=run, daemon=True)
    thread.start()

def stop():
    click_button.config(state=DISABLED)
    cps_result(count)

def cps_result(count):
    global duration, result
    result = count / duration
    result_label.config(text=f"Your CPS is: {result}")



frame = Frame(window)
frame.pack(pady=200)

click_button = Button(frame, text="Click Here", font=("Small Fonts", 20,'bold'), justify=CENTER, width=40, height=10, command= onclick, state=start_state)
click_button.grid(row=0, column=1)
start_button = Button(frame, text="START!", font=("Small Fonts", 15),anchor=CENTER,command=start)
start_button.grid(row=1, column=1)

timer_label = Label(frame, text="Timer: ", font=("Small Fonts", 10, 'bold'), justify=CENTER)
timer_label.grid(row=2,column=1) 

result_label = Label(frame, text=f"", font=("Small Fonts", 10, 'bold'), justify=CENTER)
result_label.grid(row=3, column=1)



window.mainloop()