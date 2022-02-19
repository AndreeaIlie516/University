class PersonRepository:
    def __init__(self, person_list=None):
        if person_list is None:
            person_list = []
        self._person_list = person_list

    @property
    def persons(self):
        return self._person_list

    @staticmethod
    def filter(iterable, accept):
        new_list = type(iterable)()
        for x in iterable:
            if accept(x):
                new_list.append(x)
        return new_list

    def find_person_by_id(self, person_id):
        aux = self.filter(self._person_list, lambda x: x.person_id == person_id)
        if len(aux) == 0:
            return None
        else:
            return aux[0]

    def find_person_by_name(self, name):
        aux = self.filter(self._person_list, lambda x: x.name == name)
        if len(aux) == 0:
            return None
        else:
            return aux[0]

    def find_person_by_phone_number(self, phone_number):
        aux = self.filter(self._person_list, lambda x: x.phone_number == phone_number)
        if len(aux) == 0:
            return None
        else:
            return aux[0]

    def add_person(self, person):
        self._person_list.append(person)

    def remove_person(self, person):
        self._person_list.remove(person)

    def update_person(self, person_id, name, phone_number):
        person = self.find_person_by_id(person_id)
        person.name = name
        person.phone_number = phone_number


