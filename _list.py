from toDo import ToDo

class List:
    def __init__(self, title):
        # Title of list
        self.title = title

        # Total amount of 'to dos'
        self.totalt_to_do = 0

        # The list
        self._list = []


    # Prints the title of the list
    def __str__(self):
        return self.title
        

    # Prints out the 'to do' list
    def draw_list(self):
        for i in range(len(self._list)):
            pos = i + 1
            print(f"{pos}: {self._list[i]}\n")
        
        #Prints out the total amount of 'to dos'
        print(f"Number of things to do: {self.totalt_to_do}")


    # Returns total amount of 'to dos'
    def give_len_list(self):
        return self.totalt_to_do


    # Add a 'to do' to the list
    def add_to_do(self, title, description):
        self._list.append(ToDo(title, description))

        # Updates total 'to dos'
        self.totalt_to_do += 1


    # Removes a 'to do' from the list
    def remove_to_do(self, list_pos):
        list_pos -= 1
        self._list.pop(list_pos)

        # Updates total 'to dos'
        self.totalt_to_do -= 1