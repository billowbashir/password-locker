#!/usr/bin/env python3.6
import random
from credentials import Credentials
def create_credential(pname,uname,password):
    new_credential=Credentials(pname,uname,password)
    return new_credential # create new credential and return it
def sav_credential(credentials):
    credentials.save_credentials()
def del_credential(credentials):
    credentials.delete_credentials()
def find_credentials(platform_name):
    return Credentials.find_credentials_by_platform_name(platform_name)
def check_existing_credentials(platform_name):
    return Credentials.credentials_exists(platform_name)
def show_credentials():
    return Credentials.display_all_credentials()
def main():
    print("Hello Welcome to password locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : gp - generate a new password, dp - display saved passwords, fp -find a password, ex -exit password locker ")

        short_code = input().lower()

        if short_code == 'gp':
            print("New password")
            print("-"*10)

            print ("platform name ....")
            pname = input()

            print("username ...")
            uname = input()
            password=random.randint(1000,9999)
            print(f"your password is {password}")





            sav_credential(create_credential(pname,uname,password)) # create and save new credentials.
            print ('\n')
            print(f"New password for {pname} and account {uname} created")
            print ('\n')

        elif short_code == 'dp':

            if show_credentials():
                print("Here is a list of all your passwsords")
                print('\n')

                for credential in show_credentials():
                    print(f"{credential.platform_name} {credential.username} .....{credential.password}")

                    print('\n')
            else:
                    print('\n')
                    print("You dont seem to have any passwords saved yet")
                    print('\n')

        elif short_code == 'fp':

            print("Enter the platform the password is for")

            search_platform = input()
            if check_existing_credentials(search_platform):
                search_platform = find_credentials(search_platform)
                print(f"{search_platform.platform_name} {search_platform.username}")
                print('-' * 20)

                print(f"password.......{search_platform.password}")
            else:
                print("That password does not exist")

        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':

    main()
