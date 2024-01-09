from tkinter import *
from tkinter import messagebox

def animate_logo(x, y, step=5):
    canvas.move(logo, step, 0)                                       # Move the logo on the canvas horizontally by the specified 'step' amount
    if canvas.coords(logo)[0] > window.winfo_width():                # Check if the x-coordinate of the logo's current position is beyond the window's width
        canvas.coords(logo, -400, 100)                               # If so, reset the logo's position to the left of the window
    window.after(20, animate_logo, x + step, y)                      # Schedule the next iteration of the animate_logo function after 20 milliseconds

def on_email_entry_click(event):
    if email_entry.get() == "example@gmail.com":                     # Check if the current text in the email entry is the default value "example@gmail.com"
        email_entry.delete(0, END)                                   # If it is, delete the entire text in the entry widget
        email_entry.config(fg='black')                               # Change the text color (foreground) to black


def on_email_entry_focus_out(event):
    if not email_entry.get():                                         # Check if the email entry is empty after the user has clicked outside (lost focus)
        email_entry.insert(0, "example@gmail.com")                    # If the entry is empty, insert the default value "example@gmail.com" at the beginning (index 0)
        email_entry.config(fg='grey')


def close_window():                                              #closes window automatically      
    window.destroy()

# to save details of first form
        
def save():
    firstname = firstname_entry.get()
    lastname = lastname_entry.get()
    email = email_entry.get()
    
    if len(firstname) == 0 or len(lastname) == 0:                       #if user has not entered any value and submit the form then this shows error
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title="Confirm details", message=f"These are the details entered: \nEmail: {email} "
                                                      " \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{firstname} | {lastname} | {email}\n")
                firstname_entry.delete(0, END)                      #to clear the entry once submitted form
                lastname_entry.delete(0, END)
                show_other_form()                                  #to popup another window 



# to save details of second form

def save_other_details():
    destination = destination_entry.get()
    prize = prize_entry.get()
    pickup_location = pickup_entry.get()
    if len(destination) == 0 or len(prize) == 0 or len(pickup_location) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title="Confirm details", message=f"Destination: {destination}\nPrize: {prize}\nPickup_location: {pickup_location}\n"
                                                                 "Thanks for your submission. When the deal is low, we will notify you.")
        if is_ok:
            with open("data_other.txt", "a") as data_file:
                data_file.write(f"final:-{destination} | cost:-{prize} | initial:-{pickup_location}\n")
                destination_entry.delete(0, END)
                prize_entry.delete(0, END)
                pickup_entry.delete(0, END)
                close_window()                                           #called close window function here


# declared as a global variable to access these variable anywhere
destination_entry = None
prize_entry = None
pickup_entry=None

# function of 2nd form to take destination and prize
def show_other_form():
    for widget in window.winfo_children():
        widget.destroy()                          #to destroy the previous window

    window.title("Flight Deal Checker")
    window.config(padx=50, pady=50, bg="#AED6F1")

    global prize_entry                                  #accessed global variable using global keyword
    prize_label = Label(window, text="What is your lowest amount:", bg="#AED6F1")
    prize_label.grid(row=2, column=0)

    global destination_entry
    destination_label = Label(window, text="Enter your destination", bg="#AED6F1")
    destination_label.grid(row=1, column=0)
    
    global pickup_entry
    pickup_label = Label(window, text="Enter your pickup location:", bg="#AED6F1")
    pickup_label.grid(row=3, column=0)

    destination_entry = Entry(window, width=35)
    destination_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=10)
    destination_entry.focus()

    prize_entry = Entry(window, width=35)
    prize_entry.grid(row=2, column=1, padx=5, pady=10)
    
    pickup_entry = Entry(window, width=35)
    pickup_entry.grid(row=3, column=1, padx=5, pady=10)


    add_button = Button(window, text="submit", width=30, bg="#003366", fg="white", command=save_other_details)
    add_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)


# main window

window = Tk()
window.title("Flight Deal Checker")
window.config(padx=50, pady=50, bg="#AED6F1")

# to create canvas and image
canvas = Canvas(height=200, width=200, bg="#AED6F1", highlightthickness=0)
logo_img = PhotoImage(file="aeroplane.png")
logo_img = logo_img.subsample(3, 3)
logo = canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=2)

# creating label
firstname_label = Label(text="Enter your FirstName:", bg="#AED6F1")
firstname_label.grid(row=1, column=0)

lastname_label = Label(text="Enter your LastName:", bg="#AED6F1")
lastname_label.grid(row=2, column=0)

email_label = Label(text="Email/Username:", bg="#AED6F1")
email_label.grid(row=3, column=0)

# creating entries
firstname_entry = Entry(width=35)
firstname_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=10)
firstname_entry.focus()

email_entry = Entry(width=35, fg='grey')             # Set initial text color to grey
email_entry.insert(0, "example@gmail.com")           #Insert the default value "example@gmail.com" into the email entry at the beginning (index 0).
email_entry.bind('<FocusIn>', on_email_entry_click)      #This means that when the email entry receives focus (user clicks inside it), the on_email_entry_click function will be called.
email_entry.bind('<FocusOut>', on_email_entry_focus_out)
email_entry.grid(row=3, column=1, columnspan=2, padx=5, pady=10)

lastname_entry = Entry(width=35)
lastname_entry.grid(row=2, column=1, padx=5, pady=10)

add_button = Button(text="submit", width=30, bg="#003366", fg="white", command=save)
add_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

# calling animation function here
animate_logo(100, 100)
window.mainloop()