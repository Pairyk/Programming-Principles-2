create_phonebook_table = """
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    user_name TEXT NOT NULL,
    phone_number VARCHAR(20),
    added_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
"""

insert_contact = """
INSERT INTO phonebook (user_name, phone_number)
VALUES (%s, %s)
RETURNING id;
"""

contacts_list = [
    ("Abay", "+77019976111"),
    ("Daulet", "+77011243522"),
    ("Ali", "+77010053453"),
    ("Alinur", "+77010012374")
]

get_all_contacts = "SELECT * FROM phonebook ORDER BY id ASC;"
get_contacts_by_name = "SELECT * FROM phonebook ORDER BY user_name ASC;"
get_contacts_by_number = "SELECT * FROM phonebook ORDER BY phone_number ASC;"

updating_contacts_name = """
UPDATE phonebook
SET user_name = %s
WHERE phone_number = %s;
"""

updating_contacts_number = """
UPDATE phonebook
SET phone_number = %s
WHERE user_name = %s;
"""

deleting_contacts = "DELETE FROM phonebook"

deleting_contacts_by_name = "DELETE FROM phonebook WHERE user_name = %s"
deleting_contacts_by_number = "DELETE FROM phonebook WHERE phone_number = %s"
deleting_contacts_by_id = "DELETE FROM phonebook WHERE id = %s"