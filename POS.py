import tkinter as tk
from PIL import Image, ImageTk


#IDEAS
# Maybe have a plus and minus arrow next to each checkout item so that you can easily add or take away from what's
# already there.


class Window(tk.Frame):

    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Zelda POS")
        self.pack(fill=tk.BOTH, expand=1)

        self.checkout_arr = []

        self.store_items = (
            ("Arrows (10)", 20),
            ("Bombchu (10)", 100),
            ("Bombs (5)", 25),
            ("Bottle - Blue Fire", 300),
            ("Bottle - Blue Potion", 100),
            ("Bottle - Bottled Bug", 50),
            ("Bottle - Fairy", 50),
            ("Bottle - Fish", 200),
            ("Bottle - Green Potion", 30),
            ("Bottle - Lon Lon Milk", 30),
            ("Bottle - Poe Soul", 30),
            ("Bottle - Red Potion", 30),
            ("Deku Nuts (5)", 15),
            ("Deku Seeds (30)", 30),
            ("Deku Stick", 10),
            ("Giant's Knife", 200),
            ("Shield - Deku", 40),
            ("Shield - Hylian", 80),
            ("Tunic - Goron", 300),
            ("Tunic - Zora", 300)
        )

        # Create a dictionary of the store items
        self.store_items_dict = {}
        for i in self.store_items:
            key = i[0]
            value = i[1]
            self.store_items_dict[key] = value


        # Item buttons
        self.img_a = tk.PhotoImage(file="graphics/" + self.store_items[0][0] + ".png")
        self.btn = [[0 for x in range(20)] for x in range(60)]
        grid_width = 5
        grid_height = 4
        self.button_img =[]
        for x in range(grid_width):
            for y in range(grid_height):
                id = x * grid_height + y
                # print(id)
                item_name = self.store_items[id][0]
                item_price = self.store_items[id][1]
                button_text = str(item_price) + " Rupees" + "\n\n\n\n" + item_name
                self.button_img.append(tk.PhotoImage(file="graphics/" + self.store_items[id][0] + ".png"))
                self.btn[x][y] = tk.Button(self, text=button_text, image=self.button_img[id], compound="center",
                                                command=lambda x1=x, y1=y: self.add_to_cart(x1, y1), bg="#d1d1e0",
                                                activebackground="#7676a2")
                self.btn[x][y].grid(column=x, row=y+1, sticky=tk.NSEW)

                # Assign button attributes
                self.btn[x][y].text = item_name
                self.btn[x][y].price = item_price



        # Label - item name label
        self.checkout_label_name = tk.Label(self, width=0, text="        Item name        ", anchor=tk.S)
        self.checkout_label_name.grid(column=grid_width, row=0, sticky=tk.NSEW, padx=5)

        # Label - item unit price label
        self.checkout_label_price = tk.Label(self, width=0, text="Unit price", anchor=tk.S)
        self.checkout_label_price.grid(column=grid_width+1, row=0, sticky=tk.NSEW, padx=5)

        # Label - item quantity label
        self.checkout_label_quantity = tk.Label(self, width=0, text="Quantity", anchor=tk.S)
        self.checkout_label_quantity.grid(column=grid_width+2, row=0, sticky=tk.NSEW, padx=5)

        # Label - item total label
        self.checkout_label_total = tk.Label(self, width=0, text="Total", anchor=tk.S)
        self.checkout_label_total.grid(column=grid_width+3, row=0, sticky=tk.NSEW, padx=5)

        # Label - item name
        self.checkout_items_name = tk.StringVar()
        self.checkout_0 = tk.Label(self, width=0, textvariable=self.checkout_items_name, bg="#bfd2ef", anchor=tk.NW)
        self.checkout_0.grid(column=grid_width, row=1, rowspan=grid_height, sticky=tk.NSEW)

        # Label - item unit price
        self.checkout_items_unit_price = tk.StringVar()
        self.checkout_1 = tk.Label(self, width=0, textvariable=self.checkout_items_unit_price, bg="#bfe4ff",
                                   anchor=tk.NW)
        self.checkout_1.grid(column=grid_width+1, row=1, rowspan=grid_height, sticky=tk.NSEW)

        # Label - item quantity
        self.checkout_items_quantity = tk.StringVar()
        self.checkout_2 = tk.Label(self, width=0, textvariable=self.checkout_items_quantity, bg="#bfd2ef", anchor=tk.NW)
        self.checkout_2.grid(column=grid_width+2, row=1, rowspan=grid_height, sticky=tk.NSEW)

        # Label - item total price
        self.checkout_items_price = tk.StringVar()
        self.checkout_3 = tk.Label(self, width=0, textvariable=self.checkout_items_price, bg="#bfe4ff", anchor=tk.NW)
        self.checkout_3.grid(column=grid_width+3, row=1, rowspan=grid_height, sticky=tk.NSEW)

        # Label - total price of all items
        self.total_price = 0
        self.checkout_items_total = tk.StringVar()
        self.checkout_items_total.set("Total: ₹0")
        self.checkout_4 = tk.Label(self, width=0, textvariable=self.checkout_items_total, bg="#e1e8f4", anchor=tk.NE)
        self.checkout_4.grid(column=grid_width, row=grid_height+1, columnspan=4, sticky=tk.NSEW)

        # Label - cash
        self.checkout_cash = tk.StringVar()
        self.checkout_cash.set("")
        self.checkout_5 = tk.Label(self, width=0, textvariable=self.checkout_cash, bg="#e1e8f4", anchor=tk.NE)
        self.checkout_5.grid(column=grid_width, row=grid_height+2, columnspan=4, sticky=tk.NSEW)

        # Label - change
        self.checkout_change = tk.StringVar()
        self.checkout_change.set("")
        self.checkout_6 = tk.Label(self, width=0, textvariable=self.checkout_change, bg="#e1e8f4", anchor=tk.NE)
        self.checkout_6.grid(column=grid_width, row=grid_height+3, columnspan=4, sticky=tk.NSEW)

        # Button - complete transaction
        self.btn_complete_transaction = tk.Button(self, text="Complete transaction",
                                                  command=lambda:self.complete_transaction(), bg="#d1d1e0",
                                                  activebackground="#7676a2")
        self.btn_complete_transaction.grid(column=grid_width, row=grid_height+4, columnspan=4, sticky=tk.NSEW)

        # Button - clear items
        self.btn_clear_items = tk.Button(self, text="Clear items", command=lambda: self.clear_items(), bg="#d1d1e0",
                                         activebackground="#7676a2")
        self.btn_clear_items.grid(column=grid_width+5, row=1, sticky=tk.NSEW)

        # Button - remove
        self.btn_remove_items = tk.Button(self, text="Remove last item", command=lambda: self.remove_last(),
                                          bg="#d1d1e0", activebackground="#7676a2")
        self.btn_remove_items.grid(column=grid_width+5, row=2, sticky=tk.NSEW)

        # Button - clear
        self.buffer = tk.Label(self, text="")
        self.buffer.grid(column=5, row=9, columnspan=3, sticky=tk.NSEW)

        # Digit pad
        self.cash = ""
        self.numbers = [0 for x in range(10)]
        for i in range(10):
            n = 9-i
            self.numbers[n] = tk.Button(self, text=str(n),  compound="center",
                                        command=lambda number=n: self.add_cash(number), bg="#d1d1e0",
                                        activebackground="#7676a2", anchor="center")
            self.numbers[n].grid(column=7-(i%3), row=grid_height+6+(i//3), sticky=tk.NSEW)

        # Button - clear
        self.btn_clear = tk.Button(self, text="Clear", command=lambda: self.clear_cash(), bg="#d1d1e0",
                                   activebackground="#7676a2")
        self.btn_clear.grid(column=5, row=13, columnspan=2, sticky=tk.NSEW)


    def complete_transaction(self):
        if self.cash != "":
            cash = int(self.cash)
            if self.total_price > cash: # Insufficient funds
                self.checkout_change.set("Insufficient funds")
            else:
                self.checkout_change.set("Change: ₹" + str(cash - self.total_price))

    def clear_items(self):
        # Reset variables and labels
        self.cash = ""
        self.checkout_cash.set("")
        self.checkout_change.set("")
        self.total_price = 0
        self.checkout_arr = []
        self.update_item_box()

        pass

    def add_cash(self, n):
        if not (n == 0 and self.cash == ""): # Don't allow the user to input zero as the first number
            self.cash += str(n) # Update the cash variable
            self.checkout_cash.set("Cash: ₹" + str(self.cash))  # Update the label
        pass

    def clear_cash(self):
        self.cash = ""
        self.checkout_cash.set("")

    def remove_last(self):
        if len(self.checkout_arr) > 0:
            self.checkout_arr.pop(-1)
            self.update_item_box()

    def add_to_cart(self, x, y):
        this_button = self.btn[x][y]
        name = this_button.text
        #price = this_button.price
        #self.btn[x][y].config(bg="red")

        self.checkout_arr.append(name)

        self.update_item_box()

    def update_item_box(self):
        # Build dictionary of item quantities

        item_quantities = {}
        for this_item in self.checkout_arr:
            if this_item in item_quantities:
                item_quantities[this_item] += 1
            else:
                item_quantities[this_item] = 1

        # Use dictionary to create text to place in the label area
        name_textbox = ""
        quantity_textbox = ""
        unit_price_textbox = ""
        price_textbox = ""
        self.total_price = 0
        for key in item_quantities:
            self.total_price += int(self.store_items_dict[key]) * item_quantities[key]
            if name_textbox == "": # If it's the first item, don't add a new line
                name_textbox = str(key)
                unit_price_textbox = "₹" + str(self.store_items_dict[key])
                quantity_textbox = "x" + str(item_quantities[key])
                price_textbox = "₹" + str(self.store_items_dict[key] * item_quantities[key])
            else:
                name_textbox = name_textbox + "\n" + key
                unit_price_textbox = unit_price_textbox + "\n" + "₹" + str(self.store_items_dict[key])
                quantity_textbox = quantity_textbox + "\n" + "x" + str(item_quantities[key])
                price_textbox = price_textbox + "\n" + "₹" + str(self.store_items_dict[key] * item_quantities[key])

        # Update text for labels
        self.checkout_items_name.set(name_textbox)
        self.checkout_items_unit_price.set(unit_price_textbox)
        self.checkout_items_quantity.set(quantity_textbox)
        self.checkout_items_price.set(price_textbox)
        if self.total_price > 0:
            self.checkout_items_total.set("Total: ₹" + str(self.total_price))
        else:
            self.checkout_items_total.set("")

root = tk.Tk()
root.geometry("900x600")
app = Window(root)
root.mainloop()