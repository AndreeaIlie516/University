from src.domain.activity import Activity
from src.repo.activityRepository import ActivityRepository
from src.repo.personRepository import PersonRepository
from src.exception.exception import ActivityServiceException
import random
import datetime


class ActivityService:
    def __init__(self, person_repository, activity_repository, person_service, generate=False):
        self._person_repository = PersonRepository()
        self._person_service = person_service
        self._activity_repository = activity_repository
        if generate:
            self._activity_repository = ActivityRepository(self.generate_activities())

    @property
    def activities(self):
        return self._activity_repository.activities

    @staticmethod
    def random_date():
        """
        Function for generating a random date
        :return:
        """
        start = datetime.datetime.strptime('12/11/2021 1:00 PM', '%d/%m/%Y %I:%M %p')
        end = datetime.datetime.strptime('31/12/2021 1:00 PM', '%d/%m/%Y %I:%M %p')
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = random.randrange(int_delta)
        return start + datetime.timedelta(seconds=random_second)

    def generate_activities(self):
        """
        Function for generating activities
        :return:
        """
        descriptions = Activity.list_of_descriptions()
        activities = []
        for i in range(18):
            activity_id = random.randint(1000, 9999)
            while activity_id in [x.activity_id for x in activities]:
                activity_id = random.randint(1000, 9999)
            person_id = []
            for j in range(random.randint(0, 10)):
                pid = random.choice(self._person_service.persons).person_id
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
            # date = date.strftime("%d/%m/%Y")
            time = datetime.time(hour, minute)
            activities.append(Activity(activity_id, person_id, date, time, description))
        return activities

    def add_activity(self, activity_id, person_id, date, time, description):
        """
        Function for adding an activity to the class
        :param activity_id:
        :param person_id:
        :param date:
        :param time:
        :param description:
        :return:
        """
        activity = Activity(activity_id, person_id, date, time, description)
        if self._activity_repository is not None:
            if self._activity_repository.find_activity_by_id(activity_id):
                raise ActivityServiceException("Activity with the ID " + str(activity_id) + " already exists!\n")
        if self._activity_repository.find_activity_by_date(date):
            if self._activity_repository.find_activity_by_time(date, time):
                raise ActivityServiceException("You cannot perform two or more activities at the same time (hypothetically)!\n")
        """for i in person_id:
            if self._person_repository.find_person_by_id(i) is None:
                raise ValueError("The are no person with the ID " + str(i) + " in the list!\n")
        """
        if person_id:
            exists = 0
            id = 0
            for i in person_id:
                id1 = i
                for j in self._person_service.persons:
                    if int(i) == int(j.person_id):
                        exists = 1
                        id1 = 0
                if id1 == i:
                    id = i
            if exists == 0:
                raise ActivityServiceException("The are no person with the ID " + str(id) + " in the list!\n")

        """for i in range(len(person_id)):
            activity_list = self._activity_repository.find_activity_by_persons(person_id[i])
            for j in activity_list:
                activ = self._activity_repository.find_activity_by_id(j)
                if activ.date == date:
                    if activ.time == time:
                        raise ValueError("Person with the ID " + str(person_id[i]) + "cannot perform two activities "
                                                                                     "simultaneously" )"""
        self._activity_repository.add_activity(activity)

    def remove_activity(self, activity_id):
        """
        Function for removing an activity from the class
        :param activity_id:
        :return:
        """
        activity = self._activity_repository.find_activity_by_id(activity_id)
        if not activity:
            raise ActivityServiceException("There are no activity with the ID " + str(activity_id) + "!\n")
        self._activity_repository.remove_activity(activity)

    def update_activity(self, activity_id, person_id, date, time, description):
        """
        Function for updating an activity in the class
        :param activity_id:
        :param person_id:
        :param date:
        :param time:
        :param description:
        :return:
        """
        activity = self._activity_repository.find_activity_by_id(activity_id)
        if not activity:
            raise ActivityServiceException("There are no activity with the ID " + str(activity_id) + "!\n")
        self._activity_repository.update_activity(activity_id, person_id, date, time, description)

    @staticmethod
    def split_command_param(user_input):
        """
        Function for splitting an input
        :param user_input:
        :return:
        """
        list_of_persons = []
        user_input = user_input.strip()
        tokens = user_input.split()
        length = len(tokens)
        index = 0
        while index < length:
            list_of_persons.append(int(tokens[index]))
            index += 1
        return list_of_persons

    @staticmethod
    def split_date(date):
        """
        Function for splitting a date
        :param date:
        :return:
        """
        date = date.strip()
        new_date = []
        try:
            tokens = date.split('/')
            length = len(tokens)
            index = 0
            while index < length:
                new_date.append(tokens[index])
                index += 1
            return int(new_date[0]), int(new_date[1]), int(new_date[2])
        except Exception as ve:
            print(ve)

    @staticmethod
    def split_time(time):
        """
        Function for splitting time
        :param time:
        :return:
        """
        time = time.strip()
        new_time = []
        try:
            tokens = time.split(':')
            length = len(tokens)
            index = 0
            while index < length:
                new_time.append(tokens[index])
                index += 1
            if length < 3:
                for i in range(length, 3):
                    new_time.append(0)
            return int(new_time[0]), int(new_time[1]), int(new_time[2])
        except Exception as ve:
            print(ve)
