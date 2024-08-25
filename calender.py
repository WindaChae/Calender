import calendar
import tkinter as tk
from tkinter import ttk

# Fungsi untuk menampilkan kalender bulan tertentu
def show_calendar(year, month):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    calendar_text = cal.formatmonth(year, month)
    
    # Menampilkan kalender di dalam label Tkinter
    lbl_calendar.config(text=calendar_text)

# Fungsi untuk menangani event tombol klik
def on_show():
    try:
        year = int(entry_year.get())
        month = int(entry_month.get())
        show_calendar(year, month)
    except ValueError:
        lbl_calendar.config(text="Masukkan tahun dan bulan yang valid.")

# Membuat jendela aplikasi
window = tk.Tk()
window.title("Kalender")

# Input untuk tahun
ttk.Label(window, text="Tahun:").grid(row=0, column=0, padx=10, pady=10)
entry_year = ttk.Entry(window)
entry_year.grid(row=0, column=1, padx=10, pady=10)

# Input untuk bulan
ttk.Label(window, text="Bulan:").grid(row=1, column=0, padx=10, pady=10)
entry_month = ttk.Entry(window)
entry_month.grid(row=1, column=1, padx=10, pady=10)

# Tombol untuk menampilkan kalender
btn_show = ttk.Button(window, text="Tampilkan Kalender", command=on_show)
btn_show.grid(row=2, columnspan=2, pady=10)

# Label untuk menampilkan kalender
lbl_calendar = tk.Label(window, text="", font=("Courier", 10), justify=tk.LEFT)
lbl_calendar.grid(row=3, columnspan=2, padx=10, pady=10)

# Menjalankan aplikasi
window.mainloop()
