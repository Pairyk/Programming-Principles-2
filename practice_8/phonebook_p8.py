import sys
import csv
import psycopg2
from tabulate import tabulate
from psycopg2.extras import RealDictCursor, execute_batch

# Это не библиотека, просто функций для постгре 
import queries

# Это наша конфигурация для датабазы
from config import DB_CONFIG

# Приколясы
from effects import loading_effect, clear_screen, clear_load, typewrite, screen_holder

# ------------- Это кароче наша менюшка и она рекурсирует если выбрать то чего там нет

def basic_menu():
    clear_screen()
    print("===-- Welcome to the phonebook! --===")
    print("1. Add contacts!")
    print("2. Update contacts!")
    print("3. Query contacts!")
    print("4. Delete contacts!")
    print("5. Import csv file!")
    print("6. Exit...")

    user_input = input("Your option: ")

    if user_input in ["1", "2", "3", "4", "5", "6"]:
        print("Preparing the function", end="")
        clear_load()
        return user_input
    else:
        print("No such function", end="")
        clear_load()
        return basic_menu()

# ------------ Это наш конвертор с кома сепаратет валюс в дикшионери

def csv_converter(file_csv):
    contacts = []
    with open(file_csv) as file:
        reader = csv.reader(file)
        _ = next(reader)

        for row in reader:
            if row:
                contacts.append(tuple(row))
    return contacts
        
# ------------ Здесь мы с добавляем значения через терминал

def console_input():
    print("===-- You are in contact 'ADDER'! --===\n")
    console_name = input("State the name: ").strip()
    console_number = input("State the number: ").strip()    
    return console_name, console_number
    
# ------------ Здесь наша обновление контактов идет

def console_update():
    print("===-- You are in contact 'UPDATER'! --===\n")
    update_type_choice = input("Do you  wanna update by name or number? (name/number):").lower().strip()
    match update_type_choice:
        case 'name': 
            update_choice = "by_name"
            changer_value = input("Choose the name to update number: ").strip()
            updated_value = input("What is the new number: ").strip()
        case 'number':
            update_choice = "by_number"
            changer_value = input("Choose the number to update name: ").strip()
            updated_value = input("What is the new name: ").strip()
        case _:
            clear_load("No such choice")
            console_update()

    return update_choice, changer_value, updated_value

# ------------ основная часть получения инфы находится в main

def console_querying():
    print("===-- You are in contact 'QUERYING'! --===\n")
    query_choice = input("Do you wanna query by 'name', 'number' or just 'all'? (name/number/all): ")
    match query_choice:
        case "name" | "number" | "all":
            return query_choice
        case _:
            clear_load("No such function")
            console_querying()

# ------------ удаление всего живого(номеров)

def console_contact_killer():
    print("===-- YOU ARE IN 'CONTACT KILLER', CHOOSE YOUR PRAY! --===\n")
    delete_choice = input("Delete by 'name', 'number' OR 'ALL OF THEM'?! (name/number/all): ").lower()
    match delete_choice:
        case "name":
            delete_type = 'name'
            delete_pattern = input("Choose the name of the contact to delete it: ")
        case "number":
            delete_type = 'number'
            delete_pattern = input("Choose the number of the contact to delete it: ")
        case "all":
            delete_type = 'all'
            delete_pattern = input("Just press any key, bro. I will handle the rest")
        case _:
            loading_effect("No such function")
            console_contact_killer()
        
    return delete_choice, delete_pattern



def main():
    # Тут он автоматом коммитится и закрывается как только функция заканчивается
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                while True:
                    menu_choice = basic_menu()
                    
                    match menu_choice:

                        case "1":
                            # добавляем данные с консоли
                            new_name, new_number = console_input()
                            if new_name and new_number:
                                cur.execute(queries.insert_contact, (new_name, new_number))
                            screen_holder("Adding new contact")

                        case "2":
                            # абнавляем данные с консоли
                            update_choice, changer_value, updated_value = console_update()
                            if update_choice == "by_name":
                                cur.execute(queries.updating_contacts_by_number, (updated_value, changer_value))
                            else:
                                cur.execute(queries.updating_contacts_by_name, (updated_value, changer_value))
                            screen_holder("Updating contacts")
                            
                        case "3":
                            # посмотрим на таблицу кароче
                            query_type = console_querying()
                            if query_type == "name":
                                pattern = input("Choose the symbol that should be in name: ")
                                formated_pattern = '%' + pattern + '%'
                                cur.execute(queries.get_contacts_by_name, (formated_pattern,))
                            elif query_type == "number":
                                pattern = input("Choose the symbol that should be in number: ")
                                formated_pattern = '%' + pattern + '%'
                                cur.execute(queries.get_contacts_by_number, (formated_pattern,))
                            else:
                                cur.execute(queries.get_all_contacts)
                                loading_effect("Getting all information")
                            
                            data = cur.fetchall()
                            print(tabulate(data, headers="keys", tablefmt="grid") + '\n')

                            screen_holder()

                        case "4":
                            # удаляем жалкие контакты, никто не спасется
                            delete_type, delete_pattern = console_contact_killer()
                            if delete_type == "name":
                                cur.execute(queries.deleting_contacts_by_name, (delete_pattern,))
                            elif delete_type == "number":
                                cur.execute(queries.deleting_contacts_by_number, (delete_pattern,))
                            else:
                                cur.execute(queries.deleting_contacts_all, (delete_pattern,))
                            screen_holder('Deleting contact')
                
                        case "5":
                            # импорт всего с нашего кома сепаратет валюс  файла                           
                            csv_contacts = csv_converter('contacts.csv')
                            execute_batch(cur, queries.insert_contact, csv_contacts)
                            
                            screen_holder("Importing everything from csv")

                        case "6":
                            # кидала
                            print('Bye!')
                            sys.exit()
    except Exception as e:
        print(f"Error occured - {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
