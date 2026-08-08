# Resistor Color Code Calculator
# Python Mini Project
import tkinter as tk

# -------- DATA --------
colors = {
    "Black": 0, "Brown": 1, "Red": 2, "Orange": 3,
    "Yellow": 4, "Green": 5, "Blue": 6, "Violet": 7,
    "Grey": 8, "White": 9
}

multipliers = {
    "Black": 1, "Brown": 10, "Red": 100,
    "Orange": 1000, "Yellow": 10000,
    "Green": 100000, "Blue": 1000000
}

tolerance = {
    "Gold": 5, "Silver": 10
}

color_codes = {
    "Black": "#000000", "Brown": "#8B4513", "Red": "#FF0000",
    "Orange": "#FFA500", "Yellow": "#FFFF00", "Green": "#008000",
    "Blue": "#0000FF", "Violet": "#EE82EE", "Grey": "#808080",
    "White": "#FFFFFF", "Gold": "#FFD700", "Silver": "#C0C0C0"
}

# -------- FUNCTION --------
def calculate():
    try:                                               #Prevent program crash
        b1 = colors[band1.get()]
        b2 = colors[band2.get()]
        mult = multipliers[band3.get()]
        tol = tolerance[band4.get()]

        value = (b1 * 10 + b2) * mult

        # Formatting
        if value >= 1000000:
            value_str = str(value / 1000000) + " MΩ"
        elif value >= 1000:
            value_str = str(value / 1000) + " kΩ"
        else:
            value_str = str(value) + " Ω"

        result_label.config(text=value_str + " ±" + str(tol) + "%")   #Display Result

        # Update colors
        canvas.itemconfig(r1, fill=color_codes[band1.get()])  #Changes color of bands visually
        canvas.itemconfig(r2, fill=color_codes[band2.get()])
        canvas.itemconfig(r3, fill=color_codes[band3.get()])
        canvas.itemconfig(r4, fill=color_codes[band4.get()])

    except:
        result_label.config(text="Error") #error handling

# -------- GUI --------
root = tk.Tk()       # Create a  main window
root.title("Resistor Calculator")
root.geometry("700x350")

# Dropdown variables 
band1 = tk.StringVar(value="Red")              #Variable Creation and store selected variables
band2 = tk.StringVar(value="Violet")
band3 = tk.StringVar(value="Yellow")
band4 = tk.StringVar(value="Gold")

# -------- INPUT --------
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Band 1").grid(row=0, column=0)
tk.OptionMenu(frame, band1, *colors.keys(), command=lambda x: calculate()).grid(row=1, column=0)

tk.Label(frame, text="Band 2").grid(row=0, column=1)
tk.OptionMenu(frame, band2, *colors.keys(), command=lambda x: calculate()).grid(row=1, column=1)

tk.Label(frame, text="Multiplier").grid(row=0, column=2)
tk.OptionMenu(frame, band3, *multipliers.keys(), command=lambda x: calculate()).grid(row=1, column=2)

tk.Label(frame, text="Tolerance").grid(row=0, column=3)
tk.OptionMenu(frame, band4, *tolerance.keys(), command=lambda x: calculate()).grid(row=1, column=3)

# -------- CANVAS --------
canvas = tk.Canvas(root, width=300, height=120) #Creating Resistor
canvas.pack()

canvas.create_rectangle(50, 40, 250, 80, fill="#D2B48C")

r1 = canvas.create_rectangle(70, 40, 85, 80)
r2 = canvas.create_rectangle(100, 40, 115, 80)
r3 = canvas.create_rectangle(130, 40, 145, 80)
r4 = canvas.create_rectangle(180, 40, 195, 80)

# -------- RESULT --------
result_label = tk.Label(root, text="Result", font=("Arial", 18)) #Show calclated resistance
result_label.pack(pady=10)

# Initial call
calculate()

root.mainloop()  # keeps window open