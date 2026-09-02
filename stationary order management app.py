import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

root = tk.Tk()
root.title("Stationery Order Management")
root.geometry("500x450")

canvas = tk.Canvas(root, width=500, height=450)
canvas.pack(fill="both", expand=True)

bg_image = tk.PhotoImage(width=500, height=450) 
for y in range(450):
    color = f"#{int(20 + y*0.1):02x}{int(40 + y*0.2):02x}{int(60 + y*0.3):02x}"
    bg_image.put(color, to=(0, y, 500, y + 1))


style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#1e293b", foreground="white", font=("Arial", 11)) 
style.configure("Header.TLabel", font=("Arial", 14, "bold"))
style.configure("TButton", font=("Arial", 10, "bold"), background="#0284c7", foreground="white")
style.map("TButton", background=[("active", "#0369a1")])

content_frame = tk.Frame(root, bg="#1e293b", bd=2, relief="groove")
canvas.create_window(250, 220, window=content_frame, width=440, height=380)

header = ttk.Label(content_frame, text="Stationery Order Desk", style="Header.TLabel")
header.pack(pady=10)

items_db = {"Notebook": 2.50, "Gel Pen": 1.20, "Marker Pack": 4.00, "Sticky Notes": 1.50}
qty_entries = {}

grid_frame = tk.Frame(content_frame, bg="#1e293b")
grid_frame.pack(pady=10)

for idx, (item_name, price) in enumerate(items_db.items()): 
    lbl_item = ttk.Label(grid_frame, text=f"{item_name} ($ {price:.2f}):")
    lbl_item.grid(row=idx, column=0, padx=15, pady=6, sticky="w")
    
    entry_qty = ttk.Entry(grid_frame, width=8, justify="center") 
    entry_qty.insert(0, "0")
    entry_qty.grid(row=idx, column=1, padx=15, pady=6)
    
    qty_entries[item_name] = entry_qty

currency_var = tk.StringVar(value="USD")

def calculate_total():
    total_usd = 0.0
    exchange_rate = 83.50  
    
    for item_name, entry in qty_entries.items():
        val = entry.get().strip()
        
        if not val.isdigit():
            messagebox.showerror("Input Error", f"Please enter a valid positive whole number for {item_name}.") 
            return
            
        total_usd += int(val) * items_db[item_name]

    curr = currency_var.get()
    final_amt = total_usd if curr == "USD" else (total_usd * exchange_rate) 
    symbol = "$" if curr == "USD" else "₹"
    
    lbl_result.config(text=f"Total Amount: {symbol} {final_amt:,.2f}")

selector_frame = tk.Frame(content_frame, bg="#1e293b")
selector_frame.pack(pady=5)

ttk.Label(selector_frame, text="Currency:").pack(side="left", padx=5)
r_usd = ttk.Radiobutton(selector_frame, text="USD ($)", variable=currency_var, value="USD", command=calculate_total)
r_inr = ttk.Radiobutton(selector_frame, text="INR (₹)", variable=currency_var, value="INR", command=calculate_total)
r_usd.pack(side="left", padx=5)
r_inr.pack(side="left", padx=5)

btn_calc = ttk.Button(content_frame, text="Calculate Total Order", command=calculate_total)
btn_calc.pack(pady=15)

lbl_result = ttk.Label(content_frame, text="Total Amount: $ 0.00", style="Header.TLabel")
lbl_result.pack(pady=5)

root.mainloop()