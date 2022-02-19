from src.domain.person import Person
from src.repo.personRepository import PersonRepository
from src.exception.exception import PersonServiceException
import random
import re


class PersonService:
    def __init__(self, person_repository, generate=False):
        self._person_repository = person_repository
        if generate:
            self._person_repository = PersonRepository(self.generate_person())

    @property
    def persons(self):
        return self._person_repository.persons

    @staticmethod
    def generate_person():
        """
        Function for generating persons
        """
        persons = []
        names = Person.list_of_names()
        for i in range(0, 20):
            name = random.choice(names)
            names.remove(name)
            person_id = random.randint(1000, 9999)
            while person_id in [x.person_id for x in persons]:
                person_id = random.randint(1000, 9999)
            phone_number = "07"
            for digit in range(0, 8):
                phone_number = phone_number + str(random.randint(0, 9))
            persons.append(Person(person_id, name, phone_number))
        return persons

    def add_person(self, person_id, name, phone_number):
        """
        Function for adding a person to the class
        """
        person = Person(person_id, name, phone_number)
        if self._person_repository.find_person_by_id(person_id):
            raise PersonServiceException("Person with the ID " + str(person_id) + " already exists!\n")
        if self._person_repository.find_person_by_phone_number(phone_number):
            raise PersonServiceException("Person with the phone number " + str(phone_number) + " already exists!\n")
        self._person_repository.add_person(person)

    def remove_person(self, person_id):
        """
        Function for removing a person from the class
        """
        person = self._person_repository.find_person_by_id(person_id)
        if not person:
            raise PersonServiceException("There are no person with the ID " + str(person_id) + "!\n")
        self._person_repository.remove_person(person)

    def update_person(self, person_id, name, phone_number):
        """
        Function for updating a person in the class
        """
        person = self._person_repository.find_person_by_id(person_id)
        if not person:
            raise PersonServiceException("There are no person with the ID " + str(person_id) + "!\n")
        self._person_repository.update_person(person_id, name, phone_number)

    def search_person_by_name(self, name):
        """
        Function for searching to a person by its name
        """
        return [person for person in self._person_repository.persons if re.search(name, person.name, re.IGNORECASE)]

    def search_person_by_phone_number(self, phone_number):
        """
        Function for searching for a person by its phone number
        """
        return [person for person in self._person_repository.persons if
                re.search(phone_number, person.phone_number, re.IGNORECASE)]
