import tkinter as tk

root = tk.Tk()

root.geometry("800x600")
root.title("Name to SQL Query Converter")

label = tk.Label(root, text="Hello World!", font=('Arial', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=10, font=('Arial', 16))
textbox.pack(padx=10)

button = tk.Button(root, text="Click Me!", font=('Arial', 18))
button.pack(padx=10, pady=10)

root.mainloop()

lines = []
while True:
    line = input()
    if line:
        lines.append("(DEFAULT, "+line+"),")
    else:
        break
text = '\n'.join(lines)
def remove(string):
    return string.replace(" ", "")
print(remove(text))