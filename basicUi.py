import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from threading import Thread



def start_processing():
    root_directory = directory_entry.get()
    if not os.path.isdir(root_directory):
        messagebox.showerror("Error", "Invalid directory path")
        return

    # extensions = (".jpg", ".jpeg")
    # csv_filename = "output.csv"

    progress_label.config(text="Processing started...")
    start_button.config(state=tk.DISABLED)
    
    # # Create a separate thread to run the traversal and hashing process
    # processing_thread = Thread(target=traverse_and_hash, args=(root_directory, extensions, csv_filename, progress_label))
    # processing_thread.start()

    # # Wait for the processing thread to finish
    # processing_thread.join()

    progress_label.config(text="Processing completed!")
    start_button.config(state=tk.NORMAL)


def browse_directory():
    directory_path = filedialog.askdirectory()
    if directory_path:
        directory_entry.delete(0, tk.END)
        directory_entry.insert(0, directory_path)

# Create the main application window
app = tk.Tk()
app.title("File Hashing Tool")


# Create and configure the directory entry and browse button
directory_label = ttk.Label(app, text="Root Directory:")
directory_label.grid(row=0, column=0, padx=5, pady=5)
directory_entry = ttk.Entry(app, width=40)
directory_entry.grid(row=0, column=1, padx=5, pady=5)
browse_button = ttk.Button(app, text="Browse", command=browse_directory)
browse_button.grid(row=0, column=2, padx=5, pady=5)

# Create and configure the start button
start_button = ttk.Button(app, text="Start Processing", command=start_processing)
start_button.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# # Create and configure the progress label
# progress_label = ttk.Label(app, text="")
# progress_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

app.mainloop()