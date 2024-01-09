import tkinter as tk
import random

# Create fish class
class Fish:
    def __init__(self, canvas, size, color):
        self.canvas = canvas
        # ... (initialize fish attributes)

    def move(self):
        # ... (update fish position)
        self.canvas.move(self.id, self.x, self.y)

# Create the fish tank GUI
window = tk.Tk()
canvas = tk.Canvas(window, width=600, height=400, bg="lightblue")
canvas.pack()

# Create some fish
fish_list = []
for _ in range(5):
    fish = Fish(canvas, random.randint(20, 50), random.choice(["red", "orange", "yellow"]))
    fish_list.append(fish)

# Animate the fish
def animate():
    for fish in fish_list:
        fish.move()
    window.after(50, animate)  # Call this function again after 50 milliseconds

animate()  # Start the animation
window.mainloop()