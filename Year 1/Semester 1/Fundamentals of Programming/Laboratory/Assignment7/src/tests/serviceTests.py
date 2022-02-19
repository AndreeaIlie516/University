import unittest

from src.domain.person import Person
from src.domain.activity import Activity
from src.repo.activityRepository import ActivityRepository
from src.repo.personRepository import PersonRepository
from src.service.activityService import ActivityService
from src.service.personService import PersonService
import datetime


class PersonServiceTest(unittest.TestCase):

    def test_add_person(self):
        """
        Test function for adding a person to the class
        """
        person_repo = PersonRepository()
        person_service = PersonService(person_repo)
        person1 = Person(1452, "Lars Ulrich", "0756845612")
        person2 = Person(1246, "Robb Flynn", "0745236548")

        person_service.add_person(1452, "Lars Ulrich", "0756845612")
        person_list = list(person_service.persons)
        self.assertEqual(person_list, [person1])

        person_service.add_person(1246, "Robb Flynn", "0745236548")
        person_list = list(person_service.persons)
        self.assertEqual(person_list, [person1, person2])

    def test_remove_person(self):
        """
        Test function for removing a person from the class
        """
        person_repo = PersonRepository()
        person_service = PersonService(person_repo)
        person1 = Person(1234, "James Hetfield", "0786352410")
        person2 = Person(4256, "Dave Mustaine", "0784564213")
        person3 = Person(1452, "Lars Ulrich", "0756845612")

        person_service.add_person(1234, "James Hetfield", "0786352410")
        person_service.add_person(4256, "Dave Mustaine", "0784564213")
        person_service.add_person(1452, "Lars Ulrich", "0756845612")

        person_service.remove_person(4256)
        person_list = list(person_service.persons)
        self.assertEqual(person_list, [person1, person3])

        person_service.remove_person(1452)
        person_list = list(person_service.persons)
        self.assertEqual(person_list, [person1])

        person_service.remove_person(1234)
        person_list = list(person_service.persons)
        self.assertEqual(person_list, [])

    def test_update_person(self):
        """
        Test function for updating a person in the class
        """
        person_repo = PersonRepository()
        person_service = PersonService(person_repo)
        person1 = Person(1234, "James Hetfield", "0786352410")
        person2 = Person(1452, "Dave Mustaine", "0784564213")
        person3 = Person(1452, "Lars Ulrich", "0756845612")

        person_service.add_person(1234, "James Hetfield", "0786352410")
        person_service.add_person(1452, "Dave Mustaine", "0784564213")

        person_service.update_person(1452, "Lars Ulrich", "0756845612")
        person_list = list(person_service.persons)
        self.assertEqual(person_list, [person1, person3])

    def test_search_person_by_name(self):
        """
        Test function for searching for a person by its name
        """
        person_repo = PersonRepository()
        person_service = PersonService(person_repo)
        person1 = Person(1234, "James Hetfield", "0786352410")
        person2 = Person(4256, "Dave Mustaine", "0784564213")
        person3 = Person(1452, "Lars Ulrich", "0756845612")

        person_service.add_person(1234, "James Hetfield", "0786352410")
        person_service.add_person(4256, "Dave Mustaine", "0784564213")
        person_service.add_person(1452, "Lars Ulrich", "0756845612")

        person = person_service.search_person_by_name("James Hetfield")
        self.assertNotEqual(person, None)

    def test_search_person_by_phone_number(self):
        """
        Test function for searching for a person by its phone number
        """
        person_repo = PersonRepository()
        person_service = PersonService(person_repo)
        person1 = Person(1234, "James Hetfield", "0786352410")
        person2 = Person(4256, "Dave Mustaine", "0784564213")
        person3 = Person(1452, "Lars Ulrich", "0756845612")

        person_service.add_person(1234, "James Hetfield", "0786352410")
        person_service.add_person(4256, "Dave Mustaine", "0784564213")
        person_service.add_person(1452, "Lars Ulrich", "0756845612")

        person = person_service.search_person_by_phone_number("078635")
        self.assertNotEqual(person, None)


class ActivityServiceTest(unittest.TestCase):

    def test_add_activity(self):
        """
        Test function for adding an activity to the class
        """
        person_repo = PersonRepository()
        activity_repo = ActivityRepository()
        person_service = PersonService(person_repo)

        person_service.add_person(1234, "James Hetfield", "0786352410")
        person_service.add_person(4256, "Dave Mustaine", "0784564213")
        person_service.add_person(1452, "Lars Ulrich", "0756845612")
        activity_service = ActivityService(person_repo, activity_repo, person_service)
        activity1 = Activity(3246, [1234, 4256], datetime.date(2021, 7, 30), datetime.time(15, 30), "FP homework")
        activity2 = Activity(5485, [1452], datetime.date(2021, 10, 14), datetime.time(11, 30), "Reading")

        activity_service.add_activity(3246, [1234, 4256], datetime.date(2021, 7, 30), datetime.time(15, 30),
                                      "FP homework")
        activity_list = list(activity_service.activities)
        self.assertEqual(activity_list, [activity1])

        activity_service.add_activity(5485, [1452], datetime.date(2021, 10, 14), datetime.time(11, 30), "Reading")
        activity_list = list(activity_service.activities)
        self.assertEqual(activity_list, [activity1, activity2])

    def test_remove_activity(self):
        """
        Test function for removing an activity from the class
        """
        person_repo = PersonRepository()
        activity_repo = ActivityRepository()
        person_service = PersonService(person_repo)
        person_service.add_person(1234, "James Hetfield", "0786352410")
        person_service.add_person(4256, "Dave Mustaine", "0784564213")
        person_service.add_person(1452, "Lars Ulrich", "0756845612")
        activity_service = ActivityService(person_repo, activity_repo, person_service)
        activity1 = Activity(3246, [1234, 4256], datetime.date(2021, 7, 30), datetime.time(15, 30), "FP homework")
        activity2 = Activity(5485, [1452], datetime.date(2021, 10, 14), datetime.time(11, 30), "Reading")

        activity_service.add_activity(3246, [1234, 4256], datetime.date(2021, 7, 30), datetime.time(15, 30),
                                      "FP homework")
        activity_service.add_activity(5485, [1452], datetime.date(2021, 10, 14), datetime.time(11, 30), "Reading")

        activity_service.remove_activity(3246)
        activity_list = list(activity_service.activities)
        self.assertEqual(activity_list, [activity2])

        activity_service.remove_activity(5485)
        activity_list = list(activity_service.activities)
        self.assertEqual(activity_list, [])

    def test_update_activity(self):
        """
        Test function for updating an activity in the class
        """
        person_repo = PersonRepository()
        activity_repo = ActivityRepository()
        person_service = PersonService(person_repo)
        person_service.add_person(1234, "James Hetfield", "0786352410")
        person_service.add_person(4256, "Dave Mustaine", "0784564213")
        person_service.add_person(1452, "Lars Ulrich", "0756845612")
        activity_service = ActivityService(person_repo, activity_repo, person_service)
        activity1 = Activity(3246, [1234, 4256], datetime.date(2021, 7, 30), datetime.time(15, 30), "FP homework")
        activity2 = Activity(5485, [1452], datetime.date(2021, 10, 14), datetime.time(11, 30), "Reading")
        activity3 = Activity(5485, [4256], datetime.date(2021, 11, 20), datetime.time(14, 00), "Swimming")

        activity_service.add_activity(3246, [1234, 4256], datetime.date(2021, 7, 30), datetime.time(15, 30),
                                      "FP homework")
        activity_service.add_activity(5485, [1452], datetime.date(2021, 10, 14), datetime.time(11, 30), "Reading")

        activity_service.update_activity(5485, [1234, 7845, 1452], datetime.date(2021, 11, 20), datetime.time(14, 00),
                                         "Swimming")
        activity_list = list(activity_service.activities)
        self.assertEqual(activity_list, [activity1, activity3])

    def test_search_activity_by_date(self):
        """
        Test function for searching for an activity by its date
        """
        person_repo = PersonRepository()
        activity_repo = ActivityRepository()
        person_service = PersonService(person_repo)
        person_service.add_person(1234, "James Hetfield", "0786352410")
        person_service.add_person(4256, "Dave Mustaine", "0784564213")
        person_service.add_person(1452, "Lars Ulrich", "0756845612")
        activity_service = ActivityService(person_repo, activity_repo, person_service)
        activity1 = Activity(3246, [1234, 4256], datetime.date(2021, 7, 30), datetime.time(15, 30), "FP homework")
        activity2 = Activity(5485, [1452], datetime.date(2021, 10, 14), datetime.time(11, 30), "Reading")

        activity_service.add_activity(3246, [1234, 4256], datetime.date(2021, 7, 30), datetime.time(15, 30),
                                      "FP homework")
        activity_service.add_activity(5485, [1452], datetime.date(2021, 10, 14), datetime.time(11, 30), "Reading")

        activity = activity_service.search_activity_by_date("30/07/2021")
        self.assertNotEqual(activity, None)

    def test_search_activity_by_time(self):
        """
        Test function for searching for an activity by its time
        """
        person_repo = PersonRepository()
        activity_repo = ActivityRepository()
        person_service = PersonService(person_repo)
        person_service.add_person(1234, "James Hetfield", "0786352410")
        person_service.add_person(4256, "Dave Mustaine", "0784564213")
        person_service.add_person(1452, "Lars Ulrich", "0756845612")
        activity_service = ActivityService(person_repo, activity_repo, person_service)
        activity1 = Activity(3246, [1234, 4256], datetime.date(2021, 7, 30), datetime.time(15, 30), "FP homework")
        activity2 = Activity(5485, [1452], datetime.date(2021, 10, 14), datetime.time(11, 30), "Reading")

        activity_service.add_activity(3246, [1234, 4256], datetime.date(2021, 7, 30), datetime.time(15, 30),
                                      "FP homework")
        activity_service.add_activity(5485, [1452], datetime.date(2021, 10, 14), datetime.time(11, 30), "Reading")

        activity = activity_service.search_activity_by_time("11:30")
        self.assertNotEqual(activity, None)

    def test_search_activity_by_description(self):
        """
        Test function for searching for an activity by its description
        """
        person_repo = PersonRepository()
        activity_repo = ActivityRepository()
        person_service = PersonService(person_repo)
        person_service.add_person(1234, "James Hetfield", "0786352410")
        person_service.add_person(4256, "Dave Mustaine", "0784564213")
        person_service.add_person(1452, "Lars Ulrich", "0756845612")
        activity_service = ActivityService(person_repo, activity_repo, person_service)
        activity1 = Activity(3246, [1234, 4256], datetime.date(2021, 7, 30), datetime.time(15, 30), "FP homework")
        activity2 = Activity(5485, [1452], datetime.date(2021, 10, 14), datetime.time(11, 30), "Reading")

        activity_service.add_activity(3246, [1234, 4256], datetime.date(2021, 7, 30), datetime.time(15, 30),
                                      "FP homework")
        activity_service.add_activity(5485, [1452], datetime.date(2021, 10, 14), datetime.time(11, 30), "Reading")

        activity = activity_service.search_activity_by_time("Read")
        self.assertNotEqual(activity, None)

    def test_search_activity_by_person(self):
        """
        Test function for searching for an activity by the person participating
        """
        person_repo = PersonRepository()
        activity_repo = ActivityRepository()
        person_service = PersonService(person_repo)
        person_service.add_person(1234, "James Hetfield", "0786352410")
        person_service.add_person(4256, "Dave Mustaine", "0784564213")
        person_service.add_person(1452, "Lars Ulrich", "0756845612")
        activity_service = ActivityService(person_repo, activity_repo, person_service)
        activity1 = Activity(3246, [1234, 4256], datetime.date(2021, 7, 30), datetime.time(15, 30), "FP homework")
        activity2 = Activity(5485, [1452], datetime.date(2021, 10, 14), datetime.time(11, 30), "Reading")

        activity_service.add_activity(3246, [1234, 4256], datetime.date(2021, 7, 30), datetime.time(15, 30),
                                      "FP homework")

        activity_service.add_activity(5485, [1452], datetime.date(2021, 10, 14), datetime.time(11, 30), "Reading")

        activity = activity_service.search_activity_by_time(1234)
        self.assertNotEqual(activity, None)

    def test_create_statistic_activities_by_date(self):
        """
        Test function for creating a statistics for a given date
        """
        person_repo = PersonRepository()
        activity_repo = ActivityRepository()
        person_service = PersonService(person_repo)
        person_service.add_person(1234, "James Hetfield", "0786352410")
        person_service.add_person(4256, "Dave Mustaine", "0784564213")
        person_service.add_person(1452, "Lars Ulrich", "0756845612")
        activity_service = ActivityService(person_repo, activity_repo, person_service)
        activity1 = Activity(3246, [1234, 4256], datetime.date(2021, 7, 30), datetime.time(15, 30), "FP homework")
        activity2 = Activity(5485, [1452], datetime.date(2021, 7, 30), datetime.time(11, 30), "Reading")

        activity_service.add_activity(3246, [1234, 4256], datetime.date(2021, 7, 30), datetime.time(15, 30),
                                      "FP homework")
        activity_service.add_activity(5485, [1452], datetime.date(2021, 7, 30), datetime.time(11, 30), "Reading")

        list_activities_by_date = activity_service.create_statistic_activities_by_date("30/07/2021")
        self.assertEqual(list_activities_by_date, [activity2, activity1])



class AllServiceTest:
    """
    All domain test class
    """

    def __init__(self):
        person_service_test = PersonServiceTest()
        self._person_service_test = person_service_test
        activity_service_test = ActivityServiceTest()
        self._activity_service_test = activity_service_test

    def all_tests(self):
        """
        Function for all test functions
        """
        self._person_service_test.test_add_person()
        self._person_service_test.test_remove_person()
        self._person_service_test.test_remove_person()
        self._person_service_test.test_search_person_by_name()
        self._person_service_test.test_search_person_by_phone_number()
        self._activity_service_test.test_add_activity()
        self._activity_service_test.test_remove_activity()
        self._activity_service_test.test_update_activity()
        self._activity_service_test.test_search_activity_by_date()
        self._activity_service_test.test_search_activity_by_time()
        self._activity_service_test.test_search_activity_by_description()
        self._activity_service_test.test_search_activity_by_person()
        self._activity_service_test.test_create_statistic_activities_by_date()
