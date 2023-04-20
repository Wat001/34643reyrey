import re
import time
import threading
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver

def search_names(delay, url, text_to_search, ignore_text, name_listbox, stop_event):
    driver = webdriver.Chrome()
    driver.get(url)

    found_names = set()

    while not stop_event.is_set():
        page_source = driver.page_source
        matches = re.findall(text_to_search, page_source, re.IGNORECASE)
        for match in matches:
            if not re.search(ignore_text, match) and match not in found_names:
                found_names.add(match)
                name_listbox.insert(tk.END, match)
        time.sleep(delay)

    driver.quit()

def start_search():
    # Get the inputs from the user
    url = url_entry.get()
    text_to_search = r"\b" + re.escape(text_entry.get().lower()) + r"\w*\b"
    ignore_text = "(D|d)emir"
    time_delay = float(time_entry.get())

    # Disable the search button and enable the stop button
    search_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)

    # Create a stop event to signal the search thread to stop
    stop_event = threading.Event()

    # Create a thread to run the search function
    search_thread = threading.Thread(target=search_names, args=(time_delay, url, text_to_search, ignore_text, name_listbox, stop_event))
    search_thread.start()

def stop_search():
    # Enable the search button and disable the stop button
    search_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

    # Set the stop event to signal the search thread to stop
    stop_event.set()

# Create the main window
root = tk.Tk()
root.title("Name Searcher")

# Set the font size for all widgets
FONT_SIZE = 12
root.option_add("*Font", f"TkDefaultFont {FONT_SIZE}")

# Configure the padding for all widgets
PADX = 10
PADY = 5

# Configure the background color for all widgets
BG_COLOR = "#1d1f21"
FG_COLOR = "#c5c8c6"
ACTIVE_BG_COLOR = "#373b41"
ACTIVE_FG_COLOR = "#ffffff"
root.configure(bg=BG_COLOR)

# Create a custom style for the Entry widgets
ENTRY_STYLE = {
    "bd": 2,
    "relief": tk.FLAT,
    "highlightthickness": 1,
    "highlightcolor": ACTIVE_BG_COLOR,
    "highlightbackground": ACTIVE_BG_COLOR,
    "insertbackground": FG_COLOR,
    "fg": FG_COLOR,
    "bg": BG_COLOR,
    "font": f"TkDefaultFont {FONT_SIZE}",
}

# Create the widgets for the URL input
url_label = tk.Label(root, text="Enter URL:", bg=BG_COLOR, fg=FG_COLOR)
url_label.pack(padx=PADX, pady=PADY)
url_entry = tk.Entry(root, width=50, **ENTRY_STYLE)
url_entry.pack(padx=PADX, pady=PADY)

# Create the widgets for the text input
text_label = tk.Label(root, text="Enter text to search for:", bg=BG_COLOR, fg=FG_COLOR)
text_label.pack(padx=PADX, pady=PADY)
text_entry = tk.Entry(root, width=50, **ENTRY_STYLE)
text_entry.pack(padx=PADX, pady=PADY)

# Create the widgets for the time delay input
time_label = tk.Label(root, text="Enter time delay (seconds):", bg=BG_COLOR, fg=FG_COLOR)
time_label.pack(padx=PADX, pady=PADY)
time_entry = tk.Entry(root, width=50, **ENTRY_STYLE)
time_entry.pack(padx=PADX, pady=PADY)
search_button = tk.Button(root, text="Search", command=start_search, bg=BG_COLOR, fg=FG_COLOR, activebackground=ACTIVE_BG_COLOR, activeforeground=ACTIVE_FG_COLOR)
search_button.pack(padx=PADX, pady=PADY)
stop_button = tk.Button(root, text="Stop", command=stop_search, bg=BG_COLOR, fg=FG_COLOR, activebackground=ACTIVE_BG_COLOR, activeforeground=ACTIVE_FG_COLOR, state=tk.DISABLED)
stop_button.pack(padx=PADX, pady=PADY)
name_listbox = tk.Listbox(root, width=50, height=10, bg=BG_COLOR, fg=FG_COLOR, selectbackground=ACTIVE_BG_COLOR, selectforeground=ACTIVE_FG_COLOR)
name_listbox.pack(padx=PADX, pady=PADY)
root.mainloop()
