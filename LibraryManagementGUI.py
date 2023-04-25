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
import tkinter as tk



class LibraryManagementGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Library Management System')
        self.root.geometry('400x200')

        # Create Admin frame for adding books
        self.admin_frame = tk.Frame(self.root, width=200, height=200)

        # Create Customer frame for searching books
        self.customer_frame = tk.Frame(self.root, width=200, height=200)

        # Create buttons to choose between Admin and Customer sides
        self.admin_button = tk.Button(self.root, text='Admin', command=self.show_admin)
        self.admin_button.pack(side='left', padx=10, pady=10)
        self.customer_button = tk.Button(self.root, text='Customer', command=self.show_customer)
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

        # Hide the Admin and Customer frames initially
        self.admin_frame.pack_forget()
        self.customer_frame.pack_forget()

        # Set admin_logged_in to False by default
        self.admin_logged_in = False
    def show_admin(self):
        if self.admin_logged_in:
            # Show the Admin frame with input fields for adding books
            self.admin_frame.pack(side='right')
            self.customer_frame.pack_forget()

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

    def show_customer(self):
        # Show the Customer frame and hide the Admin frame
        self.customer_frame.pack(side='right')
        self.admin_frame.pack_forget()

    def add_book(self):
        book_side = self.book_side.get()
        book_line = self.book_line.get()
        book_title = self.book_title.get()

        # Write book information to file
        with open('book_data.txt', 'a') as f:
            f.write(f"{book_side},{book_line},{book_title}\n")

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

    def delete_book(self):
        if self.admin_logged_in:
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



if __name__ == '__main__':
    gui = LibraryManagementGUI()
    gui.root.mainloop()