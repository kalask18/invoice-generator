import tkinter as tk
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime
from tkinter import messagebox
import os
import sys

def resource_path(filename):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.abspath("."), filename)

# Hover effect function for interactive buttons
def on_hover(e, widget, color):
    widget.config(bg=color)


root = tk.Tk()
root.title("Invoice Generator")
root.config(bg="#f4f6f9")

frame = tk.Frame(root, bg="#f4f6f9")
frame.pack(padx=40, pady=30) 

#
import datetime
from docxtpl import DocxTemplate


def generate_invoice():
    firstname = firstname_entry.get().strip()
    lastname = lastname_entry.get().strip()

    if not firstname:
        messagebox.showwarning("Missing Info", "Please enter both First Name.")
        return

    phone = phone_entry.get().strip()

    if not phone:
        messagebox.showwarning("Missing Info","Please enter a Phone Number.")
        return

    if not phone.isdigit() or len(phone) != 10:
        messagebox.showwarning("Invalid Phone Number","Please enter a valid 10-digit phone number.")
        return

    if not invoice_list:
        messagebox.showwarning("Empty Invoice", "Please add at least one product before generating.")
        return

    doc = DocxTemplate(resource_path("invoice_template.docx"))

    name = firstname + " " + lastname
    subtotal = round(sum(item[3] for item in invoice_list), 2)
    salestax = 0.1
    total = round(subtotal * (1 + salestax), 2)

    doc.render({
        "name": name,
        "phone": phone,
        "invoice_list": invoice_list,
        "subtotal": subtotal,
        "salestax": str(int(salestax * 100)) + "%",
        "total": total
    })

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
    file_name = name.replace(" ", "") + "_new_invoice_" + timestamp + ".docx"

    doc.save(file_name)

    messagebox.showinfo("Success", f"Invoice generated successfully:\n{file_name}")

    clear()

def clear():
    qty_entry.delete(0, tk.END)
    qty_entry.insert(0, '1')
    product_entry.delete(0,tk.END)
    unitprice_spinbox.delete(0,tk.END)
    unitprice_spinbox.insert(0, '0.0')
    
invoice_list = []

def add_item():
    if not product_entry.get().strip():
        messagebox.showwarning("Missing Info", "Please enter a Product Name.")
        return
        
    try:
        qty = int(qty_entry.get())
        unit_price = float(unitprice_spinbox.get())
    except ValueError:
        messagebox.showwarning("Invalid Input", "Quantity and Unit Price must be valid numbers.")
        return
        
    if qty <= 0:
        messagebox.showwarning("Invalid Input", "Quantity must be greater than 0.")
        return
    if unit_price <= 0:
        messagebox.showwarning("Invalid Input", "Unit Price must be greater than 0.")
        return

    product = product_entry.get()
    total = round(unit_price * qty,2)
    invoice_item = [qty, product, unit_price, total]
    preview.insert("", 0, values=invoice_item)   
    invoice_list.append(invoice_item)
    clear() 

def new_invoice():
    firstname_entry.delete(0,tk.END)
    lastname_entry.delete(0,tk.END)
    phone_entry.delete(0,tk.END)
    clear()
    preview.delete(*preview.get_children())
    invoice_list.clear()

# ==========================================
# DESIGN and LABELS
# ==========================================
font_bold = ("Segoe UI", 10, "bold")
font_norm = ("Segoe UI", 10)
bg_col = "#f4f6f9"

firstname_label = tk.Label(frame, text='First Name', bg=bg_col, font=font_bold)
firstname_label.grid(row=0, column=0, sticky="w", padx=10, pady=(0, 5))

lastname_label = tk.Label(frame, text='Last Name', bg=bg_col, font=font_bold)
lastname_label.grid(row=0, column=1, sticky="w", padx=10, pady=(0, 5))

firstname_entry = tk.Entry(frame, font=font_norm, width=25, relief="solid", bd=1)
firstname_entry.grid(row=1, column=0, sticky="ew", padx=10, pady=(0, 20))

lastname_entry = tk.Entry(frame, font=font_norm, width=25, relief="solid", bd=1)
lastname_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=(0, 20))

phone_label = tk.Label(frame, text='Phone', bg=bg_col, font=font_bold)
phone_label.grid(row=0, column=2, sticky="w", padx=10, pady=(0, 5))

phone_entry = tk.Entry(frame, font=font_norm, width=25, relief="solid", bd=1)
phone_entry.grid(row=1, column=2, sticky="ew", padx=10, pady=(0, 20))

qty_label = tk.Label(frame, text='Qty', bg=bg_col, font=font_bold)
qty_label.grid(row=2, column=0, sticky="w", padx=10, pady=(0, 5))

# Swapped to ttk.Spinbox to fix the terminal error
qty_entry = ttk.Spinbox(frame, from_=1, to=999999, font=font_norm)
qty_entry.insert(0,'1')
qty_entry.grid(row=3, column=0, sticky="ew", padx=10, pady=(0, 20))

product_label = tk.Label(frame, text='Product Name', bg=bg_col, font=font_bold)
product_label.grid(row=2, column=1, sticky="w", padx=10, pady=(0, 5))

product_entry = tk.Entry(frame, font=font_norm, relief="solid", bd=1)
product_entry.grid(row=3, column=1, sticky="ew", padx=10, pady=(0, 20))

unitprice_label = tk.Label(frame, text='Unit Price', bg=bg_col, font=font_bold)

unitprice_label.grid(row=2, column=2, sticky="w", padx=10, pady=(0, 5))

# Swapped to ttk.Spinbox to fix the terminal error
unitprice_spinbox = ttk.Spinbox(frame, from_=0.0, to=10000, increment=0.5, font=font_norm)
unitprice_spinbox.insert(0,'0.0')
unitprice_spinbox.grid(row=3, column=2, sticky="ew", padx=10, pady=(0, 20))

additem_button = tk.Button(frame, text='Add Item', command=add_item, bg="#28a745", fg="white", font=font_bold, cursor="hand2", relief="flat")
additem_button.grid(row=4, column=2, sticky="ew", padx=10, pady=(0, 20), ipady=4)
additem_button.bind("<Enter>", lambda e: on_hover(e, additem_button, "#218838"))
additem_button.bind("<Leave>", lambda e: on_hover(e, additem_button, "#28a745"))

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), background="#e9ecef")
style.configure("Treeview", font=("Segoe UI", 10), rowheight=30)

columns = ('qty', 'pro', 'price', 'total')
preview = ttk.Treeview(frame, column=columns, show='headings', height=6)
preview.heading('qty', text='Qty')
preview.heading('pro', text='Product Name')
preview.heading('price', text='Unit Price')
preview.heading('total', text='Total')

preview.column('qty', width=80, anchor='center')
preview.column('pro', width=300, anchor='w')
preview.column('price', width=120, anchor='e')
preview.column('total', width=120, anchor='e')
preview.grid(row=5, column=0, columnspan=3, sticky="nsew", padx=10, pady=(0, 20))

generate_button = tk.Button(frame, text='Generate Invoice', command=generate_invoice, bg="#007bff", fg="white", font=font_bold, cursor="hand2", relief="flat")
generate_button.grid(row=6, column=0, columnspan=3, sticky='news', padx=10, pady=(0, 10), ipady=6)
generate_button.bind("<Enter>", lambda e: on_hover(e, generate_button, "#0069d9"))
generate_button.bind("<Leave>", lambda e: on_hover(e, generate_button, "#007bff"))

new_button = tk.Button(frame, text='New Invoice', command=new_invoice, bg="#dc3545", fg="white", font=font_bold, cursor="hand2", relief="flat")
new_button.grid(row=7, column=0, columnspan=3, sticky='news', padx=10, pady=(0, 10), ipady=6)
new_button.bind("<Enter>", lambda e: on_hover(e, new_button, "#c82333"))
new_button.bind("<Leave>", lambda e: on_hover(e, new_button, "#dc3545"))

root.mainloop()