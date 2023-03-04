import tkinter as tk
from item import Item

class Interface_App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mystore")
        self.geometry("600x500")
        self.configure(bg="#3d405b") # altera a cor de fundo da janela
        self.items = []
        self.total_price = 0.0
        self.elementos_janela()

    # Cria os elementos da janela
    def elementos_janela(self):
        self.item_label = tk.Label(self, text="Produto:", bg="#3d405b", fg="white")
        self.item_label.pack()
        self.item_entry = tk.Entry(self)
        self.item_entry.pack()

        self.price_label = tk.Label(self, text="Preço:", bg="#3d405b", fg="white")
        self.price_label.pack()
        self.price_entry = tk.Entry(self)
        self.price_entry.pack()

        self.quantity_label = tk.Label(self, text="Quantidade:", bg="#3d405b", fg="white")
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(self)
        self.quantity_entry.pack()

        #Espaço adicionado abaixo do campo de quantidade
        self.space_label = tk.Label(self, text="", bg="#3d405b")
        self.space_label.pack()
     
        #Utiliza a geometria grid para alinhar os botões
        self.button_frame = tk.Frame(self, bg="#3d405b")
        self.button_frame.pack()

        self.add_button = tk.Button(self.button_frame, text="Adicionar", command=self.add_item, bg="#e07a5f", fg="white")
        self.add_button.grid(row=0, column=0, padx=10)

        self.reset_button = tk.Button(self.button_frame, text="Limpar", command=self.reset, bg="#f2cc8f", fg="white")
        self.reset_button.grid(row=0, column=1, padx=10)

        self.quit_button = tk.Button(self.button_frame, text="Sair", command=self.quit, bg="#4d4e4f", fg="white")
        self.quit_button.grid(row=0, column=2, padx=10)

        self.total_label = tk.Label(self, text=f"Valor Total: R${self.total_price:.2f}", bg="#3d405b", fg="white")
        self.total_label.pack(padx=10)

        self.item_listbox = tk.Listbox(self, width=30)
        self.item_listbox.pack(pady=10)

    def add_item(self):
        item_name = self.item_entry.get()
        item_price = float(self.price_entry.get().replace(",", "."))
        item_quantity = int(self.quantity_entry.get())

        item = Item(item_name, item_price, item_quantity)
        self.items.append(item)

        self.item_listbox.insert(tk.END, f"{item_name} - R${item_price:.2f} - {item_quantity}")
        self.total_price += item.calculate_total()
        self.total_label.config(text=f"Valor Total: R${self.total_price:.2f}")

        self.item_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

    def reset(self):
        self.items = []
        self.total_price = 0.0
        self.item_listbox.delete(0, tk.END)
        self.total_label.config(text=f"Valor Total: R${self.total_price:.2f}")



        # Utiliza a geometria grid para alinhar os botões
        self.button_frame = tk.Frame(self, bg="#3d405b")
        self.button_frame.pack()

        self.add_button = tk.Button(self.button_frame, text="Adicionar", command=self.add_item, bg="#e07a5f", fg="white")
        self.add_button.grid(row=0, column=0, padx=10)

        self.reset_button = tk.Button(self.button_frame, text="Limpar", command=self.reset, bg="#f2cc8f", fg="white")
        self.reset_button.grid(row=0, column=1, padx=10)

        self.quit_button = tk.Button(self.button_frame, text="Sair", command=self.quit, bg="#4d4e4f", fg="white")
        self.quit_button.grid(row=0, column=2, padx=10)

        self.total_label = tk.Label(self, text=f"Valor Total: R${self.total_price:.2f}", bg="#3d405b", fg="white")
        self.total_label.pack(padx=10)

        self.item_listbox = tk.Listbox(self, width=30)
        self.item_listbox.pack(pady=10)

    def add_item(self):
        item_name = self.item_entry.get()
        item_price = float(self.price_entry.get().replace(",", "."))
        item_quantity = int(self.quantity_entry.get())

        item = Item(item_name, item_price, item_quantity)
        self.items.append(item)

        self.item_listbox.insert(tk.END, f"{item_quantity}x {item_name} = R${item_price:.2f}")
        self.total_price += item.calcula_total()
        self.total_label.config(text=f"Valor Total: R${self.total_price:.2f}")

        self.item_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

    def reset(self):
        self.items = []
        self.total_price = 0.0
        self.item_listbox.delete(0, tk.END)
        self.total_label.config(text=f"Valor Total: R${self.total_price:.2f}")

