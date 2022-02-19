from src.domain.activity import Activity
from src.repo.activityRepository import ActivityRepository
from src.repo.personRepository import PersonRepository
from src.exception.exception import ActivityServiceException
from src.ui import ui
from src.ui.ui import UI
import random
import datetime
import re


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
        """
        start = datetime.datetime.strptime('25/11/2021 1:00 PM', '%d/%m/%Y %I:%M %p')
        end = datetime.datetime.strptime('30/12/2021 1:00 PM', '%d/%m/%Y %I:%M %p')
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = random.randrange(int_delta)
        return start + datetime.timedelta(seconds=random_second)

    def generate_activities(self):
        """
        Function for generating activities
        """
        descriptions = Activity.list_of_descriptions()
        activities = []
        for i in range(30):
            activity_id = random.randint(1000, 9999)
            while activity_id in [x.activity_id for x in activities]:
                activity_id = random.randint(1000, 9999)
            person_id = []
            for j in range(random.randint(0, 10)):
                pid = random.choice(self._person_service.persons).person_id
                person_id.append(pid)
            description = random.choice(descriptions)
            # descriptions.remove(description)
            random_date_time = self.random_date()
            day = random_date_time.day
            month = random_date_time.month
            year = random_date_time.year
            hour = random_date_time.hour
            minute = random_date_time.minute
            # minute = random.choice([00, 15, 30, 45])
            date = datetime.date(year, month, day)
            # date = date.strftime("%d/%m/%Y")
            time = datetime.time(hour, minute)
            activities.append(Activity(activity_id, person_id, date, time, description))
        return activities

    def add_activity(self, activity_id, person_id, date, time, description):
        """
        Function for adding an activity to the class
        """
        activity = Activity(activity_id, person_id, date, time, description)
        if self._activity_repository is not None:
            if self._activity_repository.find_activity_by_id(activity_id):
                raise ActivityServiceException("Activity with the ID " + str(activity_id) + " already exists!\n")
        if self._activity_repository.find_activity_by_date(date):
            if self._activity_repository.find_activity_by_time(date, time):
                raise ActivityServiceException(
                    "You cannot perform two or more activities at the same time (hypothetically)!\n")
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
        """
        activity = self._activity_repository.find_activity_by_id(activity_id)
        if not activity:
            raise ActivityServiceException("There are no activity with the ID " + str(activity_id) + "!\n")
        self._activity_repository.remove_activity(activity)

    def update_activity(self, activity_id, person_id, date, time, description):
        """
        Function for updating an activity in the class
        """
        activity = self._activity_repository.find_activity_by_id(activity_id)
        if not activity:
            raise ActivityServiceException("There are no activity with the ID " + str(activity_id) + "!\n")
        self._activity_repository.update_activity(activity_id, person_id, date, time, description)

    @staticmethod
    def split_command_param(user_input):
        """
        Function for splitting an input
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
            if length < 3:
                for i in range(length, 3):
                    new_date.append(0)
            return int(new_date[0]), int(new_date[1]), int(new_date[2])
        except Exception as ve:
            ui.print_exception(ve)

    @staticmethod
    def split_date_2(date):
        """
        Function for splitting a date
        """
        date = date.strip()
        new_date = []
        try:
            tokens = date.split('-')
            length = len(tokens)
            index = 0
            while index < length:
                new_date.append(tokens[index])
                index += 1
            return int(new_date[2]), int(new_date[1]), int(new_date[0])
        except Exception as ve:
            ui.print_exception(ve)

    @staticmethod
    def split_time(time):
        """
        Function for splitting time
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
            ui.print_exception(ve)

    def search_activity_by_date(self, date):
        """
        Function for searching for an activity by it date
        """
        date = str(date)
        date = date.replace("/0000", "")
        date = date.replace("00/", "")
        date = date.replace("00", "")
        """for activity in self._activity_repository.activities:
            print(str(activity.date.strftime("%d/%m/%Y")))"""
        return [activity for activity in self._activity_repository.activities if
                re.search(str(date), str(activity.date.strftime("%d/%m/%Y")), re.IGNORECASE)]

    def search_activity_by_time(self, time):
        """
        Function for searching for an activity by its time
        """
        time = str(time)
        time = time.replace(":00", "")
        return [activity for activity in self._activity_repository.activities if
                re.search(str(time), str(activity.time), re.IGNORECASE)]

    def search_activity_by_description(self, description):
        """
        Function for searching for an activity by its description
        """
        return [activity for activity in self._activity_repository.activities
                if re.search(description, activity.description, re.IGNORECASE)]

    def search_activity_by_person(self, person_id):
        """
        Function for searching for an activity by the persons participating
        """
        return [activity for activity in self._activity_repository.activities
                if re.search(str(person_id), str(activity.person_id), re.IGNORECASE)]

    def create_statistic_activities_by_date(self, date):
        """
        Function for creating a statistics for a given date
        """
        activity_list = self.search_activity_by_date(date)
        activity_list_time = sorted((str(activity.time) for activity in activity_list))
        activity_list_sorted = []
        for i in activity_list_time:
            for activity in activity_list:
                if str(i) == str(activity.time):
                    activity_list_sorted.append(activity)
        return activity_list_sorted

    # TODO: verify find_activity_by_date: you changed return aux[0] into return aux
    def number_of_activities_in_a_day(self, date):
        """
        Function for counting the activities on a specific day
        """
        list_of_activities = self._activity_repository.find_activity_by_date(date)
        count = 0
        for i in list_of_activities:
            count += 1
        return count

    def create_statistic_activities_by_free_time(self):
        """
        Function for creating a statistics for the busiest days
        """
        activity_list = self.activities
        # activity_list_date = sorted((str(self.number_of_activities_in_a_day(activity.date)) for activity
        # in activity_list))
        now = datetime.datetime.now()
        day = now.day
        month = now.month
        year = now.year
        now = datetime.date(year, month, day)
        list_of_date = []
        list_ = []
        for i in activity_list:
            date = i.date
            day, month, year = self.split_date_2(str(date))
            new_date = datetime.date(year, month, day)
            new_date = new_date.strftime("%d/%m/%Y")
            if str(date) >= str(now):
                if i.date not in list_of_date:
                    list_of_date.append([str(new_date), self.number_of_activities_in_a_day(i.date)])
        for i in range(0, len(list_of_date)):
            for j in range(i + 1, len(list_of_date)):
                if list_of_date[i][1] < list_of_date[j][1]:
                    aux = list_of_date[i]
                    list_of_date[j] = list_of_date[i]
                    list_of_date[i] = aux
        for i in range(0, len(list_of_date)):
            for j in range(0, len(list_of_date)):
                for k in range(j + 1, len(list_of_date)):
                    if list_of_date[j][1] == list_of_date[k][1] == list_of_date[i][1]:
                        if list_of_date[j][0] > list_of_date[k][0]:
                            aux = list_of_date[j]
                            list_of_date[k] = list_of_date[j]
                            list_of_date[j] = aux

        return list_of_date

    def create_statistic_activities_by_person(self, person_id):
        """
        Function for creating a statistics for activities with a given person
        """
        activity_list = self.search_activity_by_person(person_id)
        activity_list_date_time = sorted((str(datetime.datetime.combine(activity.date, activity.time)) for activity
                                          in activity_list))
        activity_list_sorted = []
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")

        for i in activity_list_date_time:
            if str(i) > str(now):
                for activity in activity_list:
                    if str(i) == str(datetime.datetime.combine(activity.date, activity.time)):
                        activity_list_sorted.append(activity)

        return activity_list_sorted
