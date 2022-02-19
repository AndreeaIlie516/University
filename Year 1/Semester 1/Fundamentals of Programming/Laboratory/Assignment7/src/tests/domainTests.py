from src.domain.person import Person
from src.domain.activity import Activity
import datetime
import unittest


class PersonDomainTest(unittest.TestCase):
    """
    Person domain test class
    """

    def test_person_domain(self):
        """
        Test function for person domain
        """
        person = Person(3564, "Mike Jordan", "0768321455")
        self.assertEqual(person.person_id, 3564)
        self.assertEqual(person.name, "Mike Jordan")
        assert person.phone_number == "0768321455"

    def test_person_representation(self):
        """
        Test function for person domain representation
        """
        person = Person(4573, "Alex Barton", "0789631456")
        self.assertEqual(str(person), "ID: 4573\nName: Alex Barton\nPhone Number: 0789631456\n")

    def test_person_equals(self):
        """
        Test function for person domain equality
        """
        person1 = Person(1234, "James Hetfield", "0786352410")
        person2 = Person(1234, "James Hetfield", "0786352410")
        person3 = Person(4256, "Dave Mustaine", "0784564213")

        self.assertEqual(person1, person2)
        self.assertNotEqual(person1, person3)

    def all_tests(self):
        """
         Function for all test functions
        """
        self.test_person_domain()
        self.test_person_representation()
        self.test_person_equals()


class ActivityDomainTest(unittest.TestCase):
    """
    Activity domain test class
    """

    def test_activity_domain(self):
        """
        Test function for activity domain
        """
        activity = Activity(2453, [3425, 4745, 5235], datetime.date(2021, 7, 30), datetime.time(15, 30), "FP homework")
        self.assertEqual(activity.activity_id, 2453)
        self.assertEqual(activity.person_id, [3425, 4745, 5235])
        self.assertEqual(activity.date, datetime.date(2021, 7, 30))
        self.assertEqual(activity.date.day, 30)
        self.assertEqual(activity.date.month, 7)
        self.assertEqual(activity.date.year, 2021)
        self.assertEqual(activity.time, datetime.time(15, 30))
        self.assertEqual(activity.time.hour, 15)
        self.assertEqual(activity.time.minute, 30)
        self.assertEqual(activity.time.second, 0)
        self.assertEqual(activity.description, "FP homework")

    def test_activity_representation(self):
        """
        Test function for activity domain representation
        """
        activity = Activity(3246, [2743, 3281, 9483], datetime.date(2021, 7, 30), datetime.time(15, 30), "FP homework")
        self.assertEqual(str(
            activity), "ID: 3246\nPerson ids: [2743, 3281, 9483]\nDate: 30/07/2021\nTime: 15:30:00\n"
                       "Description: FP homework\n")

    def test_activity_equal(self):
        """
        Test function for activity domain equality
        """
        activity1 = Activity(3246, [2743, 3281, 9483], datetime.date(2021, 7, 30), datetime.time(15, 30), "FP homework")
        activity2 = Activity(3246, [2743, 3281, 9483], datetime.date(2021, 7, 30), datetime.time(15, 30), "FP homework")
        activity3 = Activity(3247, [2743, 3281, 9483], datetime.date(2021, 7, 30), datetime.time(15, 30), "Reading")

        self.assertEqual(activity1, activity2)
        self.assertNotEqual(activity1, activity3)

    def all_tests(self):
        """
         Function for all test functions
        """
        self.test_activity_domain()
        self.test_activity_representation()
        self.test_activity_equal()
