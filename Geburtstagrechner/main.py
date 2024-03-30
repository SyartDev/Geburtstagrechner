import tkinter as tk
from datetime import datetime

def calculate_days_until_birthday():
    birthday_str = date_entry.get()

    # Konvertiere das Geburtsdatum in ein DateTime-Objekt
    birthday = datetime.strptime(birthday_str, "%Y-%m-%d")

    # Aktuelles Datum
    today = datetime.now()

    # Nächster Geburtstag für dieses Jahr
    next_birthday = datetime(today.year, birthday.month, birthday.day)

    # Berechne die Differenz zwischen Geburtstag und heute
    if today > next_birthday:
        # Wenn der Geburtstag dieses Jahr bereits vergangen ist, berechne den nächsten Geburtstag im nächsten Jahr
        next_birthday = datetime(today.year + 1, birthday.month, birthday.day)

    difference = next_birthday - today

    # Extrahiere nur die Tage aus der Differenz
    days_until_birthday = difference.days

    result_label.config(text=f"Hallo, dein nächster Geburtstag ist in {days_until_birthday} Tagen.")

# GUI erstellen
root = tk.Tk()
root.title("Geburtstagsrechner")
root.geometry("300x150")



# Label und Entry für das Geburtsdatum
date_label = tk.Label(root, text="Geburtsdatum (YYYY-MM-DD):")
date_label.pack()
date_entry = tk.Entry(root)
date_entry.pack()


# Button zum Berechnen der Tage bis zum nächsten Geburtstag
calculate_button = tk.Button(root, text="Berechnen", command=calculate_days_until_birthday)
calculate_button.pack()

# Label für das Ergebnis
result_label = tk.Label(root, text="")
result_label.pack()

# GUI starten
root.mainloop()

# GUI starten
root.mainloop()
