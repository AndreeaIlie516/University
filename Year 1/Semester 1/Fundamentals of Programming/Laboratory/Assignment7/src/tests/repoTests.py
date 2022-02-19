from src.domain.person import Person
from src.domain.activity import Activity
from src.repo.activityRepository import ActivityRepository
from src.repo.personRepository import PersonRepository
import datetime
import unittest


class PersonRepoTest(unittest.TestCase):

    def test_find_person_by_id(self):
        """
        Test function for finding a person by its id
        """
        person_repo = PersonRepository()
        person1 = Person(1234, "James Hetfield", "0786352410")
        person2 = Person(4256, "Dave Mustaine", "0784564213")
        person3 = Person(1452, "Lars Ulrich", "0756845612")

        person_repo.add_person(person1)
        person_repo.add_person(person2)
        person_repo.add_person(person3)

        person = person_repo.find_person_by_id(1278)
        self.assertEqual(person, None)
        person = person_repo.find_person_by_id(1234)
        self.assertEqual(person, person1)

    def test_find_person_by_name(self):
        """
        Test function for finding a person by its name
        """
        person_repo = PersonRepository()
        person1 = Person(1234, "James Hetfield", "0786352410")
        person2 = Person(4256, "Dave Mustaine", "0784564213")
        person3 = Person(1452, "Lars Ulrich", "0756845612")

        person_repo.add_person(person1)
        person_repo.add_person(person2)
        person_repo.add_person(person3)

        person = person_repo.find_person_by_name("John")
        self.assertEqual(person, None)
        person = person_repo.find_person_by_name("James Hetfield")
        self.assertEqual(person, person1)

    def test_find_person_by_phone_number(self):
        """
        Test function for finding a person by its phone number
        """
        person_repo = PersonRepository()
        person1 = Person(1234, "James Hetfield", "0786352410")
        person2 = Person(4256, "Dave Mustaine", "0784564213")
        person3 = Person(1452, "Lars Ulrich", "0756845612")

        person_repo.add_person(person1)
        person_repo.add_person(person2)
        person_repo.add_person(person3)

        person = person_repo.find_person_by_phone_number("072465325")
        self.assertEqual(person, None)
        person = person_repo.find_person_by_phone_number("0786352410")
        self.assertEqual(person, person1)

    def test_add_person(self):
        """
        Test function for adding a person to the class
        """
        person_repo = PersonRepository()
        person1 = Person(1452, "Lars Ulrich", "0756845612")
        person2 = Person(1246, "Robb Flynn", "0745236548")

        person_repo.add_person(person1)
        person_list = list(person_repo.persons)
        self.assertEqual(person_list, [person1])

        person_repo.add_person(person2)
        person_list = list(person_repo.persons)
        self.assertEqual(person_list, [person1, person2])

    def test_remove_person(self):
        """
        Test function for removing a person from the class
        """
        person_repo = PersonRepository()
        person1 = Person(1234, "James Hetfield", "0786352410")
        person2 = Person(4256, "Dave Mustaine", "0784564213")
        person3 = Person(1452, "Lars Ulrich", "0756845612")

        person_repo.add_person(person1)
        person_repo.add_person(person2)
        person_repo.add_person(person3)

        person_repo.remove_person(person2)
        person_list = list(person_repo.persons)
        self.assertEqual(person_list, [person1, person3])

        person_repo.remove_person(person3)
        person_list = list(person_repo.persons)
        self.assertEqual(person_list, [person1])

        person_repo.remove_person(person1)
        person_list = list(person_repo.persons)
        self.assertEqual(person_list, [])

    def test_update_person(self):
        """
        Test function for updating a person in the class
        """
        person_repo = PersonRepository()
        person1 = Person(1234, "James Hetfield", "0786352410")
        person2 = Person(1452, "Dave Mustaine", "0784564213")
        person3 = Person(1452, "Lars Ulrich", "0756845612")

        person_repo.add_person(person1)
        person_repo.add_person(person2)

        person_repo.update_person(1452, "Lars Ulrich", "0756845612")
        person_list = list(person_repo.persons)
        self.assertEqual(person_list, [person1, person3])


class ActivityRepoTest(unittest.TestCase):

    def test_find_activity_by_id(self):
        """
        Test function for finding an activity by its id
        """
        activity_repo = ActivityRepository()
        activity1 = Activity(3246, [2743, 3281, 9483], datetime.date(2021, 7, 30), datetime.time(15, 30), "FP homework")
        activity2 = Activity(5485, [4785, 4123, 7856], datetime.date(2021, 10, 14), datetime.time(11, 30), "Reading")
        activity3 = Activity(4785, [1234, 7845, 1452], datetime.date(2021, 11, 20), datetime.time(14, 00), "Swimming")
        activity_repo.add_activity(activity1)
        activity_repo.add_activity(activity2)
        activity_repo.add_activity(activity3)
        activity = activity_repo.find_activity_by_id(1278)
        self.assertEqual(activity, None)
        activity = activity_repo.find_activity_by_id(3246)
        self.assertEqual(activity, activity1)

    def test_find_activity_by_time(self):
        """
        Test function for finding an activity by its time
        """
        activity_repo = ActivityRepository()
        activity1 = Activity(3246, [2743, 3281, 9483], datetime.date(2021, 7, 30), datetime.time(15, 30), "FP homework")
        activity2 = Activity(5485, [4785, 4123, 7856], datetime.date(2021, 10, 14), datetime.time(11, 30), "Reading")
        activity3 = Activity(4785, [1234, 7845, 1452], datetime.date(2021, 11, 20), datetime.time(14, 00), "Swimming")
        activity_repo.add_activity(activity1)
        activity_repo.add_activity(activity2)
        activity_repo.add_activity(activity3)
        activity = activity_repo.find_activity_by_time(datetime.date(2021, 7, 30), datetime.time(17, 30))
        self.assertEqual(activity, None)
        activity = activity_repo.find_activity_by_time(datetime.date(2021, 7, 30), datetime.time(15, 30))
        self.assertEqual(activity, activity1)
        activity = activity_repo.find_activity_by_time(datetime.date(2021, 7, 30), datetime.time(15, 50))
        self.assertEqual(activity, activity1)

    def test_find_activity_by_date(self):
        """
        Test function for finding an activity by its date
        """
        activity_repo = ActivityRepository()
        activity1 = Activity(3246, [2743, 3281, 9483], datetime.date(2021, 7, 30), datetime.time(15, 30), "FP homework")
        activity2 = Activity(5485, [4785, 4123, 7856], datetime.date(2021, 10, 14), datetime.time(11, 30), "Reading")
        activity3 = Activity(4785, [1234, 7845, 1452], datetime.date(2021, 11, 20), datetime.time(14, 00), "Swimming")
        activity_repo.add_activity(activity1)
        activity_repo.add_activity(activity2)
        activity_repo.add_activity(activity3)
        activity = activity_repo.find_activity_by_date(datetime.date(2021, 12, 30))
        self.assertEqual(activity, None)
        activity = activity_repo.find_activity_by_date(datetime.date(2021, 7, 30))
        self.assertNotEqual(activity, None)

    def test_find_activity_by_persons(self):
        """
        Test function for finding an activity by the persons participating
        """
        activity_repo = ActivityRepository()
        activity1 = Activity(3246, [2743, 3281, 9483], datetime.date(2021, 7, 30), datetime.time(15, 30), "FP homework")
        activity2 = Activity(5485, [4785, 4123, 7856], datetime.date(2021, 10, 14), datetime.time(11, 30), "Reading")
        activity3 = Activity(4785, [1234, 7845, 1452], datetime.date(2021, 11, 20), datetime.time(14, 00), "Swimming")
        activity_repo.add_activity(activity1)
        activity_repo.add_activity(activity2)
        activity_repo.add_activity(activity3)
        activity = activity_repo.find_activity_by_persons(2453)
        self.assertEqual(activity, [])
        activity = activity_repo.find_activity_by_persons(3281)
        self.assertEqual(activity, [3246])

    def test_add_activity(self):
        """
        Test function for adding an activity to the class
        """
        activity_repo = ActivityRepository()
        activity1 = Activity(3246, [2743, 3281, 9483], datetime.date(2021, 7, 30), datetime.time(15, 30), "FP homework")
        activity2 = Activity(5485, [4785, 4123, 7856], datetime.date(2021, 10, 14), datetime.time(11, 30), "Reading")

        activity_repo.add_activity(activity1)
        activity_list = list(activity_repo.activities)
        self.assertEqual(activity_list, [activity1])

        activity_repo.add_activity(activity2)
        activity_list = list(activity_repo.activities)
        self.assertEqual(activity_list, [activity1, activity2])

    def test_remove_activity(self):
        """
        Test function for removing an activity from the class
        """
        activity_repo = ActivityRepository()
        activity1 = Activity(3246, [2743, 3281, 9483], datetime.date(2021, 7, 30), datetime.time(15, 30), "FP homework")
        activity2 = Activity(5485, [4785, 4123, 7856], datetime.date(2021, 10, 14), datetime.time(11, 30), "Reading")
        activity3 = Activity(4785, [1234, 7845, 1452], datetime.date(2021, 11, 20), datetime.time(14, 00), "Swimming")
        activity_repo.add_activity(activity1)
        activity_repo.add_activity(activity2)
        activity_repo.add_activity(activity3)

        activity_repo.remove_activity(activity2)
        activity_list = list(activity_repo.activities)
        self.assertEqual(activity_list, [activity1, activity3])

        activity_repo.remove_activity(activity3)
        activity_list = list(activity_repo.activities)
        self.assertEqual(activity_list, [activity1])

        activity_repo.remove_activity(activity1)
        activity_list = list(activity_repo.activities)
        self.assertEqual(activity_list, [])

    def test_update_activity(self):
        """
        Test function for updating an activity in the class
        """
        activity_repo = ActivityRepository()
        activity1 = Activity(3246, [2743, 3281, 9483], datetime.date(2021, 7, 30), datetime.time(15, 30), "FP homework")
        activity2 = Activity(5485, [4785, 4123, 7856], datetime.date(2021, 10, 14), datetime.time(11, 30), "Reading")
        activity3 = Activity(5485, [1234, 7845, 1452], datetime.date(2021, 11, 20), datetime.time(14, 00), "Swimming")
        activity_repo.add_activity(activity1)
        activity_repo.add_activity(activity2)

        activity_repo.update_activity(5485, [1234, 7845, 1452], datetime.date(2021, 11, 20), datetime.time(14, 00),
                                      "Swimming")
        activity_list = list(activity_repo.activities)
        self.assertEqual(activity_list, [activity1, activity3])


class AllRepoTest:
    """
    All domain test class
    """

    def __init__(self):
        person_repo_test = PersonRepoTest()
        self._person_repo_test = person_repo_test
        activity_repo_test = ActivityRepoTest()
        self._activity_repo_test = activity_repo_test

    def all_tests(self):
        """
         Function for all test functions
        """
        self._person_repo_test.test_add_person()
        self._person_repo_test.test_remove_person()
        self._person_repo_test.test_remove_person()
        self._person_repo_test.test_find_person_by_id()
        self._person_repo_test.test_find_person_by_name()
        self._person_repo_test.test_find_person_by_phone_number()
        self._activity_repo_test.test_add_activity()
        self._activity_repo_test.test_remove_activity()
        self._activity_repo_test.test_update_activity()
        self._activity_repo_test.test_find_activity_by_id()
        self._activity_repo_test.test_find_activity_by_time()
        self._activity_repo_test.test_find_activity_by_date()
        self._activity_repo_test.test_find_activity_by_persons()
