from src.Service.Service import Service


class UI:
    def __init__(self, service=None):
        if service is None:
            service = Service()
        self._service = service

    @staticmethod
    def print_menu():
        """
        Print the menu
        :return:
        """
        print("Please select one of the following options:")
        print("1.Add a person")
        print("2.Remove a person")
        print("3.Update a person")
        print("4.List persons")
        print("5.Add an activity")
        print("6.Remove an activity")
        print("7.Update an activity")
        print("8.List activities")
        print("9.Exit the application")
        print()

    def create_menu(self):

        while True:
            UI.print_menu()
            option = int(input('>'))
            if option == 1:
                self.ui_add_person()
            elif option == 2:
                self.ui_remove_person()
            elif option == 3:
                self.ui_update_person()
            elif option == 4:
                self.list_persons(self._service.persons)
            elif option == 5:
                print('5')
            elif option == 6:
                print('6')
            elif option == 7:
                print('7')
            elif option == 8:
                print('8')
            elif option == 9:
                print("You exited the application.")
                return 0
            else:
                print('Invalid number. Please select one of the five options!')

    @staticmethod
    def list_persons(persons):
        print('\n')
        print("There are " + str(len(persons)) + " persons in total in the Activity Planner")
        for i in persons:
            print(i)
        print('\n')

    def ui_add_person(self):
        print("Please add a person:")
        person_id = input("ID of the person (4 digits): ")
        try:
            person_id = int(person_id)
        except Exception as ve:
            print(ve)
        name = input("Name of the person: ")
        phone_number = str(input("Phone number of the person: "))
        try:
            self._service.add_person(person_id, name, phone_number)
            print("Person added successfully!\n")
        except Exception as e:
            print(e)

    def ui_remove_person(self):
        print("Please select a person to remove:")
        person_id = input("ID of the person:")
        try:
            person_id = int(person_id)
        except Exception as ve:
            print(ve)
        if person_id < 1000 or person_id > 9999:
            print("Invalid person ID")
            return
        try:
            self._service.remove_person(person_id)
            print("Person removed successfully!\n")
        except Exception as ve:
            print(ve)

    def ui_update_person(self):
        print("Please select a person to update:")
        person_id = input("ID of the person:")
        try:
            person_id = int(person_id)
        except Exception as ve:
            print(ve)
        if person_id < 1000 or person_id > 9999:
            print("Invalid person ID")
            return
        name = input("Name of the person: ")
        phone_number = str(input("Phone number of the person: "))
        if len(phone_number) != 10 or not phone_number.isdigit():
            print("Invalid phone number")
            return
        try:
            self._service.update_person(person_id, name, phone_number)
            print("Person updated successfully!\n")
        except Exception as ve:
            print(ve)
