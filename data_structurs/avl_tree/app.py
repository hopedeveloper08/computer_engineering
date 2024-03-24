import tkinter as tk
from avl import AVL
from queue import Queue
import tkinter.messagebox as messagebox


class App:
    def __init__(self):
        self.tree = AVL()
        self.initialize_tree()
        
        self.master = tk.Tk()
        self.master.geometry('1800x900')
        self.master.title("AVL tree")

        self.create_menu()
        self.canvas = tk.Canvas(self.master, width=2000, height=900)
        self.canvas.pack()

    def run(self):
        self.display_tree()
        self.master.mainloop()

    def initialize_tree(self):
        tree = [15, 21, 17, 12, 1, 45, 46, 21, 2, 17, 13, 9, 74, 48]
        # tree = []
        for v in tree:
            self.tree.insert(v)

    def display_tree(self):
        self.canvas.delete('all')

        if self.tree.root is None:
            return

        print("preorder: ", end='')
        self.tree.preorder()
        print("inorder: ", end='')
        self.tree.inorder()
        print("postorder: ", end='')
        self.tree.postorder()

        q = Queue()
        h = AVL.get_height(self.tree.root)
        q.put((self.tree.root, h, 1900 // 2, 50))
        MAX_HEIGHT = AVL.get_height(self.tree.root)

        while not q.empty():
            parent, h, x, y = q.get()

            self.canvas.create_oval(x - 30, y - 30, x + 30, y + 30, outline='black')

            if parent.left:
                left_x = x - 1800 // (2 ** (MAX_HEIGHT - h + 2))
                left_y = y + 150
                q.put((parent.left, h - 1, int(left_x), left_y))
                self.canvas.create_line(x, y, int(left_x), left_y, fill='black')

            if parent.right:
                right_x = x + 1800 // (2 ** (MAX_HEIGHT - h + 2))
                right_y = y + 150
                q.put((parent.right, h - 1, int(right_x), right_y))
                self.canvas.create_line(x, y, int(right_x), right_y, fill='black')

            self.canvas.create_oval(x - 28, y - 28, x + 28, y + 28, outline='light blue', fill='light blue')
            text = str(parent.data)
            self.canvas.create_text(x, y, text=text, fill='black', font=('Consolas', 16))

    def create_menu(self):
        menu_frame = tk.Frame(self.master)
        menu_frame.pack(pady=25)

        self.input_label = tk.Label(menu_frame, text='Enter value:')
        self.input_label.grid(row=0, column=0, pady=10, padx=10)

        self.input_entry = tk.Entry(menu_frame, width=30)
        self.input_entry.grid(row=0, column=1, pady=10)

        self.insert_button = tk.Button(menu_frame, width=20, text='Insert', command=self.insert_value, bg='green')
        self.insert_button.grid(row=1, column=0, padx=10)

        self.search_button = tk.Button(menu_frame, width=20, text='Search', command=self.search_value, bg="gold")
        self.search_button.grid(row=1, column=1, padx=10)

        self.delete_button = tk.Button(menu_frame, width=20, text='Delete', command=self.delete_value, bg='red')
        self.delete_button.grid(row=1, column=3, padx=10)

    def insert_value(self):
        value = self.input_entry.get()
        if value.isdigit():
            self.tree.insert(int(value))
            self.display_tree()

    def search_value(self):
        value = self.input_entry.get()
        if value.isdigit():
            result = self.tree.search(int(value))
            if result:
                messagebox.showinfo(title="found..." , message=f'{value} found in the AVL tree...')
            else:
                messagebox.showerror(title="not found!" , message=f'{value} not found in the AVL tree!!!')

    def delete_value(self):
        value = self.input_entry.get()
        if value.isdigit():
            self.tree.delete(int(value))
            self.display_tree()


if __name__ == '__main__':
    App().run()
