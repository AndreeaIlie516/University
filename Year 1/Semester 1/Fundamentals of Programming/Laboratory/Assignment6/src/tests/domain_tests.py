from src.domain.domain import Person, Activity
import datetime


class DomainTest:
    """
    Domain test class
    """

    def __init__(self):
        pass

    def test_domain_person(self):
        person = Person(3564, "Mike Jordan", "0768321455")
        assert person.person_id == 3564
        assert person.name == "Mike Jordan"
        assert person.phone_number == "0768321455"

    def test_person_representation(self):
        person = Person(4573, "Alex Barton", "0789631456")
        assert str(person) == "ID: 4573, Name: Alex Barton, Phone Number: 0789631456"

    def test_domain_activity(self):
        activity = Activity(2, [3, 4, 5], datetime.date(2021, 7, 30), datetime.time(15, 30), "FP homework")
        assert activity.activity_id == 2
        assert activity.person_id == [3, 4, 5]
        assert activity.date == datetime.date(2021, 7, 30)
        assert activity.date.day == 30
        assert activity.date.month == 7
        assert activity.date.year == 2021
        assert activity.time == datetime.time(15, 30)
        assert activity.time.hour == 15
        assert activity.time.minute == 30
        assert activity.description == "FP homework"

    def test_activity_representation(self):
        activity = Activity(3246, [2743, 3281, 9483], datetime.date(2021, 7, 30), datetime.time(15, 30), "FP homework")
        assert str(
            activity) == "ID: 3246, Person ids: [2743, 3281, 9483], Date: 2021-07-30, Time: 15:30:00, " \
                         "Description: FP homework"

    def all_tests(self):
        self.test_domain_person()
        self.test_person_representation()
        self.test_domain_activity()
        self.test_activity_representation()
