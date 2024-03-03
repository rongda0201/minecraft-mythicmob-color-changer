import re
import tkinter as tk
from tkinter import scrolledtext

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb_color):
    return "#{:02x}{:02x}{:02x}".format(*rgb_color)

def adjust_color(input_str, r_change, g_change, b_change):
    pattern = r"c=#[0-9A-Fa-f]{6}"
    match = re.search(pattern, input_str)
    
    if match:
        color_hex = match.group(0)[3:]
        rgb_color = hex_to_rgb(color_hex)
        
        # Adjust the RGB values
        new_r = min(255, rgb_color[0] + r_change)
        new_g = max(0, rgb_color[1] + g_change)
        new_b = max(0, rgb_color[2] + b_change)
        
        new_color_hex = rgb_to_hex((new_r, new_g, new_b))
        result_str = input_str.replace(color_hex, new_color_hex[1:])  # Exclude the "#" in the replacement
        
        return result_str
    else:
        return "No color code found in the input."

def process_input():
    user_input = input_text.get("1.0", tk.END).splitlines()
    r_change = int(r_entry.get())
    g_change = int(g_entry.get())
    b_change = int(b_entry.get())

    result_text.delete(1.0, tk.END)
    
    for line in user_input:
        result = adjust_color(line, r_change, g_change, b_change)
        result_text.insert(tk.END, result + "\n")

# GUI setup
root = tk.Tk()
root.title("Mythicmob 粒子顏色批量調整")

# Input Frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="輸入粒子顏色代碼:").pack()
input_text = scrolledtext.ScrolledText(input_frame, width=100, height=10, wrap=tk.WORD)
input_text.pack(pady=10)

# Adjustments Frame
adjustments_frame = tk.Frame(root)
adjustments_frame.pack()

tk.Label(adjustments_frame, text="輸入 R 的變動值:").grid(row=0, column=0, padx=5)
r_entry = tk.Entry(adjustments_frame)
r_entry.grid(row=0, column=1, padx=5)

tk.Label(adjustments_frame, text="輸入 G 的變動值:").grid(row=1, column=0, padx=5)
g_entry = tk.Entry(adjustments_frame)
g_entry.grid(row=1, column=1, padx=5)

tk.Label(adjustments_frame, text="輸入 B 的變動值").grid(row=2, column=0, padx=5)
b_entry = tk.Entry(adjustments_frame)
b_entry.grid(row=2, column=1, padx=5)

# Process Button
process_button = tk.Button(root, text="轉換", command=process_input)
process_button.pack(pady=10)

# Result Frame
result_frame = tk.Frame(root)
result_frame.pack()

tk.Label(result_frame, text="轉換結果:").pack()
result_text = scrolledtext.ScrolledText(result_frame, width=100, height=10, wrap=tk.WORD)
result_text.pack(pady=10)

# Run the GUI
root.mainloop()
