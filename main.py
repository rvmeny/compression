from tkinter import *
from LZ77 import LZ77_c, LZ77_dec

class LZ77App:
    def __init__(self, root):
        self.root = root
        self.root.title("LZ77 Compression")
        self.root.geometry("500x500+350+200")

        self.create_widgets()

    def create_widgets(self):
        Label(self.root, text="Введите текст для сжатия:").pack(pady=10)

        self.input_entry = Entry(self.root, width=50)
        self.input_entry.pack(pady=10)

        compress_button = Button(self.root, text="Сжать", command=self.compress_data)
        compress_button.pack(pady=5)

        clear_button = Button(self.root, text="Очистить", command=self.clear_data)
        clear_button.pack(pady=5)

        self.result_text = Text(self.root, height=10, width=50)
        self.result_text.pack(pady=10)

    def compress_data(self):
        input_data = self.input_entry.get()
        compressed_data = LZ77_c(input_data)
        self.display_results(input_data, compressed_data)

    def clear_data(self):
        self.result_text.delete("1.0", "end-1c")
        self.input_entry.delete(0, 'end')
        self.input_entry.focus()

    def display_results(self, input_data, result_data):
        self.result_text.delete("1.0", "end-1c")
        result_str = "Входные данные:\n{}\n\nРезультат: {}".format(input_data, result_data)
        self.result_text.insert("1.0", result_str)

if __name__ == "__main__":
    root = Tk()
    app = LZ77App(root)
    root.mainloop()
