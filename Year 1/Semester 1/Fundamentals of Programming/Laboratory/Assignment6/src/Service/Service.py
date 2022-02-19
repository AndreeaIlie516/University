from src.domain.domain import Person, Activity
from src.repository.person_repository import PersonRepository
import random
import datetime


class Service:
    def __init__(self, person_repository=None, activity_repository=None):
        self._person_repository = person_repository
        self._activity_repository = activity_repository
        if person_repository is None:
            self._person_repository = PersonRepository(self.generate_person())

    @property
    def persons(self):
        return self._person_repository.persons

    @property
    def activities(self):
        return self._activity_repository.activities

    @staticmethod
    def generate_person():
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

    @staticmethod
    def random_date():
        start = datetime.datetime.strptime('12/11/2021 1:00 PM', '%d/%m/%Y %I:%M %p')
        end = datetime.datetime.strptime('31/12/2021 1:00 PM', '%d/%m/%Y %I:%M %p')
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = random.randrange(int_delta)
        return start + datetime.timedelta(seconds=random_second)

    def generate_activities(self):
        descriptions = Activity.list_of_descriptions()
        activities = []
        for i in range(1, 20):
            activity_id = i
            person_id = []
            for j in range(random.randint(1, 10)):
                pid = random.choice(self._person_repository.persons).id
                person_id.append(pid)
            description = random.choice(descriptions)
            descriptions.remove(description)
            random_date_time = self.random_date()
            day = random_date_time.day
            month = random_date_time.month
            year = random_date_time.year
            hour = random_date_time.hour
            minute = random_date_time.minute
            date = datetime.date(year, month, day)
            time = datetime.time(hour, minute)
            activities.append(Activity(activity_id, person_id, date, time, description))
        return activities

    def add_person(self, person_id, name, phone_number):
        person = Person(person_id, name, phone_number)
        if self._person_repository.find_person_by_id(person_id):
            raise ValueError("Person with the ID " + str(person_id) + " already exists!\n")
        if self._person_repository.find_person_by_name(name):
            raise ValueError("Person with the name " + str(name) + " already exists!\n")
        if self._person_repository.find_person_by_phone_number(phone_number):
            raise ValueError("Person with the phone number " + str(phone_number) + " already exists!\n")
        self._person_repository.add_person(person)

    def remove_person(self, person_id):
        person = self._person_repository.find_person_by_id(person_id)
        if not person:
            raise ValueError("There are no student with the ID " + str(person_id) + "!\n")
        self._person_repository.remove_person(person)

    def update_person(self, person_id, name, phone_number):
        person = self._person_repository.find_person_by_id(person_id)
        if not person:
            raise ValueError("There are no student with the ID " + str(person_id) + "!\n")
        self._person_repository.update_person(person_id, name, phone_number)
