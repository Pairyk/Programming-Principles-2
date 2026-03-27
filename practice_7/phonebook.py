from os import getenv
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor, execute_batch
import csv

# Это не библиотека, просто функций для постгре 
import queries

load_dotenv()

def db_connection():
    # Крч помогает создать связь и еще берет все из дот-енва
    return psycopg2.connect(
        dbname=getenv("DB_NAME"),
        user=getenv("DB_USER"),
        password=getenv("DB_PASS"),
        host=getenv("DB_HOST"),
        port=getenv("DB_PORT"),
    )


def csv_converter(file_csv):
    contacts = []
    with open(file_csv) as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            if row:
                contacts.append(tuple(row))
    return contacts
        

def console_input():
    choice = input("Do you wanna enter data by console? (y/n):")
    if choice.lower() == 'y':
        console_name = input("State the name: ").strip()
        console_number = input("State the number: ").strip()    
    return console_name, console_number
    

def console_update_name():
    changer = input("Choose the number to update name: ").strip()
    upd_name = input("What is the new name: ").strip()
    return changer, upd_name


def console_update_number():
    changer = input("Choose the name to update number: ").strip()
    upd_number = input("What is the new number: ").strip()
    return changer, upd_number
    


def main():
    # Тут он автоматом коммитится и закрывается как только функция заканчивается
    try:
        with db_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                # Execute это базовая функция для вызова функций постгре
                # cur.execute(queries.create_phonebook_table)

                # Тут мы добавляем одно значение
                # cur.execute(queries.insert_contact, ("Dauren", "+77777777777"))

                # Тоже самое что и инсерт просто работает на листе и сразу все парсит
                # execute_batch(cur, queries.insert_contact , queries.contacts_list)
                
                # Тут мы просто принтим всю дату, сперва нунжно ее заретурнить главное
                # cur.execute(queries.get_all_contacts)
                # all_contacts = cur.fetchall()
                # for row in all_contacts:
                #     print(f"ID - {row['id']}, Name - {row['user_name']}, Number - {row['phone_number']}")

                # Обнавляем значение просто так
                # cur.execute(queries.updating_contacts, ('+81224651232', 'Alice'))

                # Просто удаляем бедного Боба (уже всех)
                # cur.execute(queries.deleting_contacts, ('7'))

#------------------------------------------------------------------------------------------------------------

                # contacts = csv_converter('contacts.csv')
                # execute_batch(cur, queries.insert_contact, contacts)

                # new_name, new_number = console_input()
                # if new_name and new_number:
                #     cur.execute(queries.insert_contact, (new_name, new_number))

                # update_choice = input("Do you wanna update value through console? (y/n): ").lower()
                # if update_choice == "y":
                #     what_to_update = input("Do you wanna update name or number? (name/number): ").lower()
                #     if what_to_update == "name":
                #         changer, new_value = console_update_name()
                #         cur.execute(queries.updating_contacts_name, (new_value, changer))
                #     elif what_to_update == "number":
                #         changer, new_value == console_update_number()
                #         cur.execute(queries.updating_contacts_number, (new_value, changer))

                # query_choice = input("Do you wanna query data? (y/n): ").lower()
                # if query_choice == 'y':
                #     query_type = input("Query by name or number or id? (name/number/id): ").lower()
                #     if query_type == "name":
                #         cur.execute(queries.get_contacts_by_name)
                #     elif query_type == "number":
                #         cur.execute(queries.get_contacts_by_number)
                #     elif query_type == "id":
                #         cur.execute(queries.get_all_contacts)

                #     data = cur.fetchall()
                #     for raw in data:
                #         print(f"id - {raw['id']}, name - {raw['user_name']}, number - {raw['phone_number']}")
                    
                # query_choice = input("Do you wanna delete data? (y/n): ").lower()
                # if query_choice == 'y':
                #     query_type = input("Delete by name or number or id? (name/number/id): ").lower()
                #     delete_value = input("Type details to delete: ")
                #     if query_type == "name":
                #         cur.execute(queries.deleting_contacts_by_name, (delete_value,))
                #     elif query_type == "number":
                #         cur.execute(queries.deleting_contacts_by_number, (delete_value,))
                #     elif query_type == "id":
                #         cur.execute(queries.deleting_contacts_by_id, (delete_value,))

                print("\nDone!")

    except Exception as e:
        print(f"Error occured - {e}")


if __name__ == "__main__":
    main()
