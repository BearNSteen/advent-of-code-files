import time
import tkinter as tk

class Timer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Timer")

        # Create a label to display the current time
        self.time_label = tk.Label(self.root, text="Current time: ")
        self.time_label.pack()

        # Create a label to display the remaining time on the timer
        self.timer_label = tk.Label(self.root, text="Timer: ")
        self.timer_label.pack()

        # Create an entry field for the user to input the timer duration
        self.timer_entry = tk.Entry(self.root)
        self.timer_entry.pack()

        # Create a button for the user to start the timer
        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack()

        # Create a button for the user to stop the timer
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_timer)
        self.stop_button.pack()

        # Set the initial timer duration to 0
        self.timer_duration = 0

        # Start the clock
        self.update_clock()

        # Start the mainloop
        self.root.mainloop()

    def start_timer(self):
        # Get the timer duration from the entry field
        self.timer_duration = int(self.timer_entry.get())

        # Start the timer and set the start_time
        self.start_time = time.time()

        # Update the timer label
        self.update_clock()

    def stop_timer(self):
        # Stop the timer
        self.end_time = time.time()

        # Calculate the elapsed time
        self.elapsed_time = self.end_time - self.start_time

    def update_clock(self):
        # Get the current time
        current_time = time.time()

        # Calculate the remaining time on the timer
        remaining_time = self.timer_duration - (current_time - self.start_time)

        # Format the remaining time
        remaining_time_formatted = "{0:02d}:{1:02d}".format(int(remaining_time // 60), int(remaining_time % 60))

        # Update the time and timer labels
        self.time_label.config(text="Current time: " + time.strftime("%H:%M:%S"))
        self.timer_label.config(text="Timer: " + remaining_time_formatted)

        # Schedule the next clock update
        self.root.after(100, self.update_clock)

if __name__ == "__main__":
    timer = Timer()