import info
import design
import db
import pw_generator
import sqlite3

from tabulate import tabulate

def main():
    design.print_big_text("Developed by Deniz Varıcı")
    user_input = ""
    mydb = db.DatabaseManager("Db.db")
    mydb.create_table() #create table if not exists
    user_input_list = ["quit", "exit", "help", "info", "list", "delete", "add", "update", "get", "hidden-list", "clear", "destroy"]
    try:
        while user_input != "quit" and user_input != "exit":
            user_input = input(">> ")
            if user_input == "help" or user_input == "info":
                print(info.help_info)
            elif user_input == "list":
                password_list = mydb.get_password_list()
                if password_list:
                    # for data in password_list:
                    #     print(data)
                    table_headers = ["Platform\n___","Password\n___"]
                    print(tabulate(password_list,table_headers, tablefmt="fancy_grid"))
                else:
                    print("No record found")
            elif user_input == "delete":
                print("Enter Platform Name : ")
                platform_name = input(">> ")
                if mydb.delete_data(platform_name):
                    print("Deleted Successfully!")
                else:
                    print("Error! Platform name not found!")
            elif user_input == "add":
                print("Enter Platform Name : ")
                platform_name = input(">> ")
                print("Enter password(leave blank if you want random password) : ")
                password = input(">> ")
                try:
                    if password == "":
                        print("How many characters do you want for random password?(Leave blank if you want default(10 characters))")
                        char_count = input(">> ")
                        if char_count == "":
                            random_pass = pw_generator.generate_random_pw()
                        else:
                            char_count = int(char_count)
                            random_pass = pw_generator.generate_random_pw(char_count)
                        mydb.add_new_data(platform_name, random_pass)
                        print("Successfully added! type 'list' to show your password list")
                    else:
                        mydb.add_new_data(platform_name, password)
                        print("Successfully added! type list to show your password list")
                except sqlite3.IntegrityError:
                    print(f"{platform_name} already exists. Use a different name or update your password by update command")
            elif user_input == "update":
                print("Enter Platform Name : ")
                platform_name = input(">> ")
                print("Enter password(leave blank if you want random password) : ")
                password = input(">> ")
                if mydb.update_data(platform_name, password):
                    print("Successfully Updated!")
                else:
                    print("Error! You may entered wrong platform name check your platform name by 'list' command and try to 'update' again.")
            elif user_input == "get":
                print("Enter Platform Name : ")
                platform_name = input(">> ")
                pwforoneplatform = mydb.get_password_for_one_platform(platform_name)
                if pwforoneplatform is None:
                    print("Platform doesn't exists! Try again or see all passwords by typing 'list' command or type 'hidden-list' to see only platform names")
                else:
                    print(pwforoneplatform)
            elif user_input == "hidden-list":
                platform_list = mydb.get_platform_list()
                if platform_list:
                    # for platform in platform_list:
                    #     print(platform)
                    table_headers = ["Platform"]
                    print(tabulate(platform_list,table_headers, tablefmt="simple"))
                else:
                    print("No record found")
            elif user_input == "clear":
                design.clear_console()
            elif user_input == "destroy":
                user_accept = input("Are you sure you want to delete all your password data?(Y/n)")
                if user_accept == "Y" or user_accept == "y":
                    mydb.delete_all_datas()
                    print("All password data is deleted.")
            elif user_input_list.__contains__(user_input) == False:
                print("Command not recognized. Type help or info to get list of commands.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        mydb.close()

if __name__ == "__main__":
    main()
