import sys
import csv
import psycopg2
from tabulate import tabulate
from psycopg2.extras import RealDictCursor, execute_batch

# Это наша конфигурация для датабазы
from config_artf import DB_CONFIG

# Приколясы
from effects import loading_effect, clear_screen, clear_load, typewrite, screen_holder

# ------------- Это кароче наша менюшка и она рекурсирует если выбрать то чего там нет

def basic_menu():
    clear_screen()
    print("===-- Welcome to the artifact-book! --===")
    print("1. Add & Update artifacts!")
    print("2. Query artifacts!")
    print("3. Delete artifacts!")
    print("4. Import csv file!")
    print("5. Exit...")

    user_input = input("Your option: ")

    if user_input in ["1", "2", "3", "4", "5"]:
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
        
def main():
    # Тут он автоматом коммитится и закрывается как только функция заканчивается
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                while True:
                    menu_choice = basic_menu()
                    
                    match menu_choice:

                        case "1":
                            # добавляем и обновляем данные с консоли
                            print("===-- You are in artifact 'ADDER & UPDATER'! --===\n")
                            console_name = input("State the name: ").strip()
                            console_buff = input("State the buff: ").strip()   
                            if console_name and console_buff:
                                cur.execute("CALL upsert_artifact(%s::text, %s::text)", (console_name, console_buff))
                                conn.commit()
                            screen_holder("Upserting new artifact")
                            
                        case "2":
                            # посмотрим на таблицу кароче
                            print("===-- You are in artifact 'QUERYING'! --===\n")
                            query_choice = input("Do you wanna query by pattern or amount? (pattern/amount): ")
                                
                            if query_choice == 'pattern':
                                pattern = input("Your pattern: ")
                                cur.execute("SELECT * FROM search_artifacts(%s)", (pattern,))
                            elif query_choice == 'amount':
                                amount = input("Amount of results: ")
                                offset = input("How much to skip: ")
                                cur.execute("SELECT * FROM get_artifacts(%s, %s)", (int(amount), int(offset)))
                            
                            data = cur.fetchall()
                            print(tabulate(data, headers="keys", tablefmt="grid") + '\n')
                            screen_holder()

                        case "3":
                            # удаляем жалкие контакты, никто не спасется
                            print("===-- You are in artifact 'DELETION'! --===\n")
                            delete_pattern = input("Write your delete pattern: ")
                            cur.execute('CALL delete_artifact(%s)', (delete_pattern,))
                            conn.commit()
                            screen_holder('Deleting artifacts')
                
                        case "4":
                            # импорт всего с нашего кома сепаратет валюс  файла   
                            print("===-- You are in artifact 'BULKING'! --===\n")                        
                            csv_data = csv_converter('data.csv')
                            names = [row[0] for row in csv_data]
                            buffs = [row[1] for row in csv_data]

                            cur.execute("CALL bulk_upsert_artifacts(%s, %s)", (names, buffs))
                            conn.commit()
                            
                            screen_holder("Importing everything from csv")

                        case "5":
                            # кидала
                            print('Bye!')
                            sys.exit()
    except Exception as e:
        print(f"Error occured - {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
