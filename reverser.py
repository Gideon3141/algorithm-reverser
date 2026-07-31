import tkinter as tk

def reverse_algorithm():
    alg = entry.get().strip().split()
    alg.reverse()
    
    reversed_moves = []
    for move in alg:
        if move.endswith("'"):
            reversed_moves.append(move[:-1])
        elif move.endswith("2"):
            reversed_moves.append(move)
        else:
            reversed_moves.append(move + "'")
            
    result_label.config(text="Reversed: " + " ".join(reversed_moves))

root = tk.Tk()
root.title("Alg Reverser")
root.geometry("350x150")
  empty_icon = tk.PhotoImage()
    root.iconphoto(False, empty_icon)

tk.Label(root, text="Enter Algorithm:").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Reverse", command=reverse_algorithm).pack(pady=5)
result_label = tk.Label(root, text="Reversed: ", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()
