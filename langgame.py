import tkinter as tk
from tkinter import ttk

vowels = ['a', 'e', 'i', 'o', 'u']

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 
              'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

def on_plain(event):
    plain = plainText.get('1.0', tk.END).strip('\n')
    outText.delete('1.0', tk.END)

    if combo.get() == "Encrypt":
        output = ""
        for idx, char in enumerate(plain):
            if char.isalpha():
                isUpper = char.isupper()
                char = char.lower()

                idx += 1
                if char in vowels:
                    lettArr = vowels
                else:
                    lettArr = consonants

                lettIdx = lettArr.index(char) + idx
                outChar = lettArr[lettIdx % len(lettArr)]

                if isUpper:
                    outChar = outChar.upper()
            else:
                outChar = char

            output = output + outChar
    elif combo.get() == "Palindrome":
        output = plain + plain[-2::-1].strip()
    else:
        output = ""

    outText.insert('1.0', chars = output)

def on_select(event):
    on_plain(event)

root = tk.Tk()
root.title("Language Games")

options = ["Encrypt", "Palindrome"]

combo = ttk.Combobox(root, values=options)
combo.set(options[0])
combo.bind("<<ComboboxSelected>>", on_select)
combo['state'] = 'readonly'
combo.bind("<<")
combo.pack(pady=10)

tk.Label(root, text="Plain Text").pack()

plainText = tk.Text(root, height=8)
plainText.pack(padx=10, pady=10, expand=True,fill=tk.BOTH)
plainText.bind("<KeyRelease>", on_plain)

tk.Label(root, text="Encrypted Text").pack()

outText = tk.Text(root, height=8)
outText.pack(padx=10, pady=10, expand=True,fill=tk.BOTH)

root.mainloop()
