from src.domain.person import Person
from src.domain.activity import Activity
import datetime


class PersonDomainTest:
    """
    Person domain test class
    """

    def __init__(self):
        pass

    @staticmethod
    def test_person_domain():
        """
        Test function for person domain
        :return:
        """
        person = Person(3564, "Mike Jordan", "0768321455")
        assert person.person_id == 3564
        assert person.name == "Mike Jordan"
        assert person.phone_number == "0768321455"

    @staticmethod
    def test_person_representation():
        """
        Test function for person domain representation
        :return:
        """
        person = Person(4573, "Alex Barton", "0789631456")
        assert str(person) == "ID: 4573\nName: Alex Barton\nPhone Number: 0789631456\n"

    @staticmethod
    def test_person_equals():
        """
        Test function for person domain equality
        :return:
        """
        person1 = Person(1234, "James Hetfield", "0786352410")
        person2 = Person(1234, "James Hetfield", "0786352410")
        person3 = Person(4256, "Dave Mustaine", "0784564213")

        assert person1 == person2
        assert person1 != person3


class ActivityDomainTest:
    """
    Activity domain test class
    """

    def __init__(self):
        pass

    @staticmethod
    def test_activity_domain():
        """
        Test function for activity domain
        :return:
        """
        activity = Activity(2453, [3425, 4745, 5235], datetime.date(2021, 7, 30), datetime.time(15, 30), "FP homework")
        assert activity.activity_id == 2453
        assert activity.person_id == [3425, 4745, 5235]
        assert activity.date == datetime.date(2021, 7, 30)
        assert activity.date.day == 30
        assert activity.date.month == 7
        assert activity.date.year == 2021
        assert activity.time == datetime.time(15, 30)
        assert activity.time.hour == 15
        assert activity.time.minute == 30
        assert activity.time.second == 0
        assert activity.description == "FP homework"

    @staticmethod
    def test_activity_representation():
        """
        Test function for activity domain representation
        :return:
        """
        activity = Activity(3246, [2743, 3281, 9483], datetime.date(2021, 7, 30), datetime.time(15, 30), "FP homework")
        assert str(
            activity) == "ID: 3246\nPerson ids: [2743, 3281, 9483]\nDate: 30/07/2021\nTime: 15:30:00\n" \
                         "Description: FP homework\n"

    @staticmethod
    def test_activity_equal():
        """
        Test function for activity domain equality
        :return:
        """
        activity1 = Activity(3246, [2743, 3281, 9483], datetime.date(2021, 7, 30), datetime.time(15, 30), "FP homework")
        activity2 = Activity(3246, [2743, 3281, 9483], datetime.date(2021, 7, 30), datetime.time(15, 30), "FP homework")
        activity3 = Activity(3247, [2743, 3281, 9483], datetime.date(2021, 7, 30), datetime.time(15, 30), "Reading")

        assert activity1 == activity2
        assert activity1 != activity3


class AllDomainTest:
    """
    All domain test class
    """

    def __init__(self):
        person_domain_test = PersonDomainTest
        self._person_domain_test = person_domain_test
        activity_domain_test = ActivityDomainTest
        self._activity_domain_test = activity_domain_test

    def all_tests(self):
        """
        Function for all test functions
        :return:
        """
        self._person_domain_test.test_person_domain()
        self._person_domain_test.test_person_representation()
        self._person_domain_test.test_person_equals()
        self._activity_domain_test.test_activity_domain()
        self._activity_domain_test.test_activity_representation()
        self._activity_domain_test.test_activity_equal()
