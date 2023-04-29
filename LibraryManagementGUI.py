# ***************************************************************
# Name : ProgramNameTong
# Author: Than Tong
# Created : * Course: CIS 152 - Data Structure
# Version: 1.0
# OS: Windows 11
# IDE: Python
# Copyright : This is my own original work
# based onspecifications issued by our instructor
# Description :
#           Input: ADD HERE XXX
#           Ouput: ADD HERE XXX
# Academic Honesty: I attest that this is my original work.
# I have not used unauthorized source code, either modified or
# unmodified. I have not given other fellow student(s) access
# to my program.

# ***************************************************************
# Name : ProgramNameTong
# Author: Than Tong
# Created : * Course: CIS 152 - Data Structure
# Version: 1.0
# OS: Windows 11
# IDE: Python
# Copyright : This is my own original work
# based onspecifications issued by our instructor
# Description :
#           Input: ADD HERE XXX
#           Ouput: ADD HERE XXX
# Academic Honesty: I attest that this is my original work.
# I have not used unauthorized source code, either modified or
# unmodified. I have not given other fellow student(s) access
# to my program.
import os
import tkinter as tk

RENT_DATA_FILE = 'rent_data.txt'
BOOK_DATA_FILE = 'book_data.txt'

class book_data:
    def __init__(self, side, line, title):
        self.side = side
        self.line = line
        self.title = title

class LibraryManagementGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Library Management System')
        self.root.geometry('400x300')

        # Create Admin frame for adding books
        self.admin_frame = tk.Frame(self.root, width=200, height=200)
        self.init_admin_frame()

        # Create Customer frame for searching books
        self.customer_frame = tk.Frame(self.root, width=200, height=200)
        self.init_customer_frame()

        # Create buttons to choose between Admin and Customer sides
        self.admin_button = tk.Button(self.root, text='Admin', command=self.show_admin)
        self.admin_button.pack(side='left', padx=10, pady=10)
        self.customer_button = tk.Button(self.root, text='Customer',
                                         command=lambda: [self.show_customer(), self.rent_book()])
        self.customer_button.pack(side='right', padx=10, pady=10)

        # Create labels and input fields for Customer frame
        self.customer_title_label = tk.Label(self.customer_frame, text='Search Book')
        self.customer_title_label.pack()

        self.search_book_label = tk.Label(self.customer_frame, text='Book Title')
        self.search_book_label.pack()
        self.search_book_entry = tk.Entry(self.customer_frame)
        self.search_book_entry.pack()

        self.search_book_button = tk.Button(self.customer_frame, text='Search Book', command=self.search_book)
        self.search_book_button.pack(pady=10)

        self.search_results_label = tk.Label(self.customer_frame, text='Search results go here')
        self.search_results_label.pack()

        # Create a delete button for removing a book
        self.delete_book_button = tk.Button(self.admin_frame, text='Delete Book', command=self.delete_book)
        self.delete_book_button.pack(pady=10)

        self.rent_book_button = tk.Button(self.customer_frame, text='Rent Book', command=self.rent_book)
        self.rent_book_button.pack(pady=10)

        self.return_book_button = tk.Button(self.customer_frame, text='Rental Return', command=self.admin_rental_return)
        self.return_book_button.pack()

        # Hide the Admin and Customer frames initially
        self.admin_frame.pack_forget()
        self.customer_frame.pack_forget()

        # Set admin_logged_in to False by default
        self.admin_logged_in = False

    def quick_sort_by_title(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            left = [x for x in arr[1:] if x.title < pivot.title]
            right = [x for x in arr[1:] if x.title >= pivot.title]
            return self.quick_sort_by_title(left) + [pivot] + self.quick_sort_by_title(right)
    def update_most_recent(self):
        if os.path.exists(RENT_DATA_FILE):
            last_line = ''
            with open(RENT_DATA_FILE, 'r') as fin:
                for line in fin:
                    last_line = line.strip()
            if last_line:
                self.recent_rental_book_label.config(text=last_line)
                self.recent_rental_book_label.pack()
    def init_admin_frame(self):
        # Create labels and input fields for adding books
        self.add_book_label = tk.Label(self.admin_frame, text='Add Book')
        self.add_book_label.pack()

        self.book_side_label = tk.Label(self.admin_frame, text='Side')
        self.book_side_label.pack()
        self.book_side = tk.Entry(self.admin_frame)
        self.book_side.pack()

        self.book_line_label = tk.Label(self.admin_frame, text='Line')
        self.book_line_label.pack()
        self.book_line = tk.Entry(self.admin_frame)
        self.book_line.pack()

        self.book_title_label = tk.Label(self.admin_frame, text='Title')
        self.book_title_label.pack()
        self.book_title = tk.Entry(self.admin_frame)
        self.book_title.pack()

        self.add_book_button = tk.Button(self.admin_frame, text='Add Book', command=self.add_book)
        self.add_book_button.pack()

        self.btn_check_rental = tk.Button(self.admin_frame, text='Check Rental', command=self.check_rental)
        self.btn_check_rental.pack()

        # Create a label for the book title of the most recent rental
        self.recent_rental_label = tk.Label(self.admin_frame, text='Most Recent Rental:')
        self.recent_rental_label.pack()

        self.recent_rental_book_label = tk.Label(self.admin_frame, text='')
        self.update_most_recent()

        self.return_book_button = tk.Button(self.admin_frame, text='Rental Return', command=self.admin_rental_return)
        self.return_book_button.pack()

    def show_admin(self):
        if self.admin_logged_in:
            # Show the Admin frame with input fields for adding books
            self.update_most_recent()
            self.admin_frame.pack(side='right')
            self.customer_frame.pack_forget()

        else:
            # Show the password window and hide the Customer frame
            self.admin_frame.pack_forget()  # hide the Admin frame
            self.password_window = tk.Toplevel(self.root)
            self.password_label = tk.Label(self.password_window, text='Enter password:')
            self.password_label.pack()
            self.password_entry = tk.Entry(self.password_window, show='*')
            self.password_entry.pack()
            self.submit_button = tk.Button(self.password_window, text='Submit', command=self.check_password)
            self.submit_button.pack()

    def add_admin_login(self):
        if not hasattr(self, 'password_window'):
            self.password_window = tk.Toplevel(self.root)
            self.password_label = tk.Label(self.password_window, text='Enter password:')
            self.password_label.pack()
            self.password_entry = tk.Entry(self.password_window, show='*')
            self.password_entry.pack()
            self.submit_button = tk.Button(self.password_window, text='Submit', command=self.check_password)
            self.submit_button.pack()

    def check_password(self):
        password = self.password_entry.get()
        if password == '0000':
            self.password_window.destroy()
            self.admin_logged_in = True
            self.show_admin()
        else:
            self.password_label.config(text='Incorrect password, try again...')
            self.password_entry.delete(0, tk.END)  # Add this line to reset the entry field

    def init_customer_frame(self):
        return
        self.rent_date_label = tk.Label(self.customer_frame, text='Rent Date')
        self.rent_date_label.pack()
        self.rent_date_entry = tk.Entry(self.customer_frame)
        self.rent_date_entry.pack()

        self.return_date_label = tk.Label(self.customer_frame, text='Return Date')
        self.return_date_label.pack()
        self.return_date_entry = tk.Entry(self.customer_frame)
        self.return_date_entry.pack()

        self.name_label = tk.Label(self.customer_frame, text='Name')
        self.name_label.pack()
        self.name_entry = tk.Entry(self.customer_frame)
        self.name_entry.pack()

    def show_customer(self):
        # Show the Customer frame and hide the Admin frame
        self.customer_frame.pack(side='right')
        self.admin_frame.pack_forget()

    def check_rental(self):
        if not os.path.exists(RENT_DATA_FILE):
            self.display_popup('No data found')
            return

        rent_window = tk.Toplevel(self.root)
        rent_window.title('Rental Details')

        with open(RENT_DATA_FILE, 'r') as fin:
            for line in fin:
                book_title_label = tk.Label(rent_window, text=line)
                book_title_label.pack()

    def add_book(self):
        input_side = self.book_side.get()
        input_line = self.book_line.get()
        input_title = self.book_title.get()

        if not input_side or not input_line or not input_title:
            self.display_popup('Invalid input.')
            return

        book_list = []
        if os.path.exists(BOOK_DATA_FILE):
            with open(BOOK_DATA_FILE, 'r') as f:
                for line in f:
                    book_side, book_line, book_title = line.strip().split(',')
                    book_list.append(book_data(book_side, book_line, book_title))

        #Add new book to the list
        book_list.append(book_data(input_side, input_line, input_title))

        #Quick sort book list
        if len(book_list) > 1:
            book_list = self.quick_sort_by_title(book_list)

        with open(BOOK_DATA_FILE, 'w') as f:
            for book in book_list:
                f.write(f"{book.side},{book.line},{book.title}\n")

        # Clear input fields
        self.book_side.delete(0, tk.END)
        self.book_line.delete(0, tk.END)
        self.book_title.delete(0, tk.END)

        # Display success message
        print("Success message should appear now")
        success_label = tk.Label(self.admin_frame, text="You added a new book.", fg="green")
        success_label.pack()

    def search_book(self):
        # Get input field value
        search_book_title = self.search_book_entry.get()

        # Search for books with search_book_title
        search_results = []
        with open('book_data.txt', 'r') as f:
            for line in f:
                book_side, book_line, book_title = line.strip().split(',')
                if book_title == search_book_title:
                    search_results.append((book_title, book_line, book_side))

        # Display search results in the customer frame
        if search_results:
            search_results_str = '\n'.join(
                [f'Title: {title}, Line: {line}, Section: {side}' for title, line, side in search_results])
        else:
            search_results_str = 'No results found.'
        self.search_results_label.config(text=search_results_str)

    def admin_rental_return(self):
        rental_ret_window = tk.Toplevel(self.root)
        rental_ret_window.title("Return rental")
        name_label = tk.Label(rental_ret_window, text='Name')
        name_label.pack()
        name_input = tk.Entry(rental_ret_window)
        name_input.pack()

        title_label = tk.Label(rental_ret_window, text='Title')
        title_label.pack()
        title_input = tk.Entry(rental_ret_window)
        title_input.pack()

        btn_return = tk.Button(rental_ret_window, text='Return', command=lambda: self.return_rental(name_input.get(),
                                                                                                    title_input.get()))
        btn_return.pack()

        btn_close = tk.Button(rental_ret_window, text='Close', command=lambda: rental_ret_window.destroy())
        btn_close.pack()

    def return_rental(self, name, title):
        if not name or not title:
            self.display_popup('Invalid input!')
        else:
            found_rental = False
            with open(RENT_DATA_FILE, "r") as f:
                lines = [] #    f.readlines()
                for line in f:
                    lines.append(line)
                    book_title, rent_date, return_date, rent_name = line.strip().split(',')
                    if book_title == title and rent_name == name:
                        found_rental = True

            if found_rental:
                with open(RENT_DATA_FILE, "w") as f:
                    for line in lines:
                        book_title, rent_date, return_date, rent_name = line.strip().split(',')
                        if book_title != title and rent_name != name:
                            f.write(line)
                        else:
                            print("Rental returned: " + line)
                self.display_popup('Book returned!')
            else:
                print('Book not found! Name: ' + name + ' - title: ' + title)
                self.display_popup('Book not found!')

    def delete_book(self):
        if self.admin_logged_in:
            # Remove any previously created input fields for adding a book
            for widget in self.admin_frame.winfo_children():
                widget.destroy()

            # Show the Admin frame with input fields for deleting books
            self.admin_frame.pack(side='right')
            self.customer_frame.pack_forget()

            # Create labels and input fields for deleting books
            self.delete_book_label = tk.Label(self.admin_frame, text='Delete Book')
            self.delete_book_label.pack()

            self.delete_book_title_label = tk.Label(self.admin_frame, text='Title')
            self.delete_book_title_label.pack()
            self.delete_book_title_entry = tk.Entry(self.admin_frame)
            self.delete_book_title_entry.pack()

            self.delete_book_button = tk.Button(self.admin_frame, text='Delete Book', command=self.confirm_delete_book)
            self.delete_book_button.pack()

        else:
            # Show the password window and hide the Customer frame
            self.admin_frame.pack_forget()  # hide the Admin frame
            self.password_window = tk.Toplevel(self.root)
            self.password_label = tk.Label(self.password_window, text='Enter password:')
            self.password_label.pack()
            self.password_entry = tk.Entry(self.password_window, show='*')
            self.password_entry.pack()
            self.submit_button = tk.Button(self.password_window, text='Submit', command=self.check_password_for_delete)
            self.submit_button.pack()

    def check_password_for_delete(self):
        password = self.password_entry.get()
        if password == '0000':
            self.password_window.destroy()
            self.admin_logged_in = True
            self.delete_book()
        else:
            self.password_label.config(text='Incorrect password, try again...')
            self.password_entry.delete(0, tk.END)  # Add this line to reset the entry field

    def confirm_delete_book(self):
        book_title = self.delete_book_title_entry.get()
        with open('book_data.txt', 'r') as f:
            lines = f.readlines()
        with open('book_data.txt', 'w') as f:
            for line in lines:
                if line.strip().split(',')[2] != book_title:
                    f.write(line)
        self.delete_book_title_entry.delete(0, tk.END)
        self.delete_book_label.config(text='Book deleted successfully!')

    def rent_book(self):
        # Show the Rental Details window
        rent_window = tk.Toplevel(self.root)
        rent_window.title('Rental Details')

        # Create labels and input fields for the rental details
        book_title_label = tk.Label(rent_window, text='Book Title')
        book_title_label.pack()
        book_title_entry = tk.Entry(rent_window)
        book_title_entry.pack()

        rent_date_label = tk.Label(rent_window, text='Rent Date')
        rent_date_label.pack()
        rent_date_entry = tk.Entry(rent_window)
        rent_date_entry.pack()

        return_date_label = tk.Label(rent_window, text='Return Date')
        return_date_label.pack()
        return_date_entry = tk.Entry(rent_window)
        return_date_entry.pack()

        name_label = tk.Label(rent_window, text='Name')
        name_label.pack()
        name_entry = tk.Entry(rent_window)
        name_entry.pack()

        # Create a button to save the rental details
        save_button = tk.Button(rent_window, text='Save Rental',
                                command=lambda: [self.save_rental(book_title_entry.get(),
                                                                 rent_date_entry.get(),
                                                                 return_date_entry.get(),
                                                                 name_entry.get()), rent_window.destroy()])
        save_button.pack()

    def display_popup(self, text):
        popup_msg = tk.Toplevel(self.root)
        popup_msg.title('Error')
        popup_label = tk.Label(popup_msg, text=text)
        popup_label.pack()
        ok_button = tk.Button(popup_msg, text='OK',
                              command=lambda: popup_msg.destroy())
        ok_button.pack()
    def save_rental(self, book_title, rent_date, return_date, name):
        if not book_title or not rent_date or not return_date or not name:
            print('Invalid data')
            self.display_popup('Invalid data')
            return
        # Save the rental details in a database or file
        print('Rent Book:', book_title)
        print('Rent Date:', rent_date)
        print('Return Date:', return_date)
        print('Name:', name)
        with open(RENT_DATA_FILE, 'a') as f:
            f.write(f"{book_title},{rent_date},{return_date},{name}\n")


if __name__ == '__main__':
    gui = LibraryManagementGUI()
    gui.root.mainloop()
