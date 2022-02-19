class Person:
    def __init__(self, person_id, name, phone_number):
        if person_id < 1000 or person_id > 9999:
            raise ValueError("Invalid person ID")
        self._person_id = person_id
        self._name = name
        if len(phone_number) != 10 or not phone_number.isdigit():
            raise ValueError("Invalid phone number")
        self._phone_number = phone_number

    def __str__(self):
        return "ID: " + str(self._person_id) + ", Name: " + str(self._name) + ", Phone Number: " + str(
            self._phone_number)

    def __eq__(self, other):
        return self.person_id == other.person_id and self.name == other.name

    @property
    def person_id(self):
        return self._person_id

    @property
    def name(self):
        return self._name

    @property
    def phone_number(self):
        return self._phone_number

    @person_id.setter
    def person_id(self, x):
        if x < 1000 or x > 9999:
            raise ValueError("Invalid person ID")
        self._person_id = x

    @name.setter
    def name(self, x):
        self._name = x

    @phone_number.setter
    def phone_number(self, x):
        if len(x) != 10 or not x.isdigit():
            raise ValueError("Invalid phone number")
        self._phone_number = x

    @staticmethod
    def list_of_names():
        list_of_names = [
            "Jacob Fletcher",
            "Morgan McLean",
            "Lydia Boyle",
            "Courtney Norton",
            "Aidan Griffiths",
            "Louie Wheeler",
            "Sam Brady",
            "Paige Lamb",
            "Joseph Carter",
            "Erin Nelson",
            "Alexander Wong",
            "Isabelle Goddard",
            "Elise Faulkner",
            "Freddie Mitchell",
            "Katherine Allan",
            "Leon Matthews",
            "Elizabeth Herbert",
            "Sarah Mellor",
            "Hollie Farmer",
            "Jennifer Barton",
            "Henry Stevenson",
            "Aaliyah Simmons",
            "Michael Dickinson",
            "Louie Weston",
            "Daisy Clements",
            "Riley Garner",
            "Cameron Reed",
            "Jasmine Coleman",
            "Katherine Sanderson",
            "Daniel Hall"
        ]
        return list_of_names


class Activity:
    def __init__(self, activity_id, person_id, date, time, description):
        self._activity_id = activity_id
        self._person_id = person_id
        self._date = date
        self._time = time
        self._description = description

    def __str__(self):
        return "ID: " + str(self._activity_id) + ", Person ids: " + str(self._person_id) + ", Date: " + str(
            self._date) + ", Time: " + str(self._time) + ", Description: " + str(self._description)

    def __eq__(self, other):
        return self.activity_id == other.activity_id

    @property
    def activity_id(self):
        return self._activity_id

    @property
    def person_id(self):
        return self._person_id

    @property
    def date(self):
        return self._date

    @property
    def time(self):
        return self._time

    @property
    def description(self):
        return self._description

    @activity_id.setter
    def activity_id(self, x):
        self._activity_id = x

    @person_id.setter
    def person_id(self, x):
        self._person_id = x

    @date.setter
    def date(self, x):
        self._date = x

    @time.setter
    def time(self, x):
        self._time = x

    @description.setter
    def description(self, x):
        self._description = x

    @staticmethod
    def list_of_descriptions():
        list_of_descriptions = [
            "labdhsde"
        ]
        return list_of_descriptions
