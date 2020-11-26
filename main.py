from _list import List

# The main program
def main():
    # Creates list
    to_do_list = List("To do list")

    # Loop for program
    while True:
        # Prints title
        print()  # Spacer
        print(to_do_list)

        # Prints list
        to_do_list.draw_list()


        # Choise for adding or removing 'to dos'
        choise = input("\nType '+' to add a to do, or type '-' to remove a to do: ")


        # Adding 'to do'
        if choise == "+":
            # Gives 'to do' a title
            title = input("Title for to do: ")
            # Gives 'to do' a description
            description = input("Description for to do: ")
            to_do_list.add_to_do(title, description)

        # Removing 'to do'
        elif choise == "-":
            # Checks input is an int
            try:
                # Choose the 'to do' to remove
                list_pos = int(input("Position of to do you want to remove: "))
            # Print if input is not an int
            except ValueError:
                print("\n\n\n\nInvalid position, please type an int.")  # x * \n so it's easier to read

            else:
                # Checks if the 'to do' is in the list
                if to_do_list.give_len_list() >= list_pos and list_pos > 0:
                    to_do_list.remove_to_do(list_pos)
                else:
                    # Prints this message if 'to do' is not in the list
                    print("\n\n\n\nInvalid position, please type an position in the list")  # x * \n so it's easier to read   


# Runs main if file is run as main program
if __name__ == "__main__":
    main()