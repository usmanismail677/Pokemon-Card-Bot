import sqlite3
from tabulate import tabulate  # Install it using: pip install tabulate

# Connect to the database
conn = sqlite3.connect("ebay_pokemon_cards.db")
cursor = conn.cursor()

# Fetch records
cursor.execute("SELECT * FROM pokemon_cards LIMIT 10;")  # Adjust limit as needed
records = cursor.fetchall()

# Display table headers
headers = ["ID", "Title", "Price", "Link"]
table_data = tabulate(records, headers=headers, tablefmt="grid")  # Other formats: "pretty", "psql"

# Print to terminal
print(table_data)

# Save output to a file
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(table_data)

print("Output saved to output.txt")

conn.close()
