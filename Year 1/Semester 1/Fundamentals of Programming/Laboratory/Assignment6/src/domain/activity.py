from src.exception.exception import ActivityDomainException
import datetime

class Activity:
    def __init__(self, activity_id, person_id, date, time, description):
        """
        Create Activity with activity_id(the id of the activity), person_id(the ids of the persons participating),
        date(the date of the activity), time(the time of the activity), description(the description of the activity)
        """
        self._activity_id = activity_id
        self._person_id = person_id
        self._date = date
        self._time = time
        self._description = description

    def __str__(self):
        date = self._date.strftime("%d/%m/%Y")
        return "ID: " + str(self._activity_id) + "\nPerson ids: " + str(self._person_id) + "\nDate: " + str(
            date) + "\nTime: " + str(self._time) + "\nDescription: " + str(self._description) + '\n'

    def __eq__(self, other):
        return self.activity_id == other.activity_id

    @property
    def activity_id(self):
        return self._activity_id

    @property
    def person_id(self):
        return self._person_id

    @property
    def date(self):
        return self._date

    @property
    def time(self):
        return self._time

    @property
    def description(self):
        return self._description

    @activity_id.setter
    def activity_id(self, x):
        if x < 1000 or x > 9999:
            raise ValueError("Invalid activity ID")
        self._activity_id = x

    @person_id.setter
    def person_id(self, x):
        self._person_id = x

    @date.setter
    def date(self, x):
        self._date = x

    @time.setter
    def time(self, x):
        self._time = x

    @description.setter
    def description(self, x):
        self._description = x

    @staticmethod
    def list_of_descriptions():
        list_of_descriptions = [
            "Read (You little nerd)",
            "Study (Still hope to pass the exams, ha?)",
            "Attend classes (We all know that you are sleeping)",
            "Cook (Be careful not to start a fire)",
            "Relax (Just another excuse to procrastinate)",
            "Go to the gym (It's pointless, but at least you tried)",
            "Swim (Be careful not to drown)",
            "Meditate (You hope to become a new Buddha, but you are still angry af)",
            "Go shopping (You don't have enough money!!!)",
            "Eat outside ((You don't have enough money!!! x2)",
            "Take a walk (Oh, fresh air, just to forget how stupid you are)",
            "Skincare (You little princess)",
            "Go to party (We all know it doesn't happen)",
            "Watch a movie (Just another bullshit teenager romance movie)",
            "Play board games (We all know you have no friends)",
            "Drink alcohol like only computer science students can do",
            "Listen to music (Maneaua Otelul Galati, right?)",
            "Go to a concert (We all know you will headbang all night long and then complaining about neck pain "
            "an entire week) "
        ]
        return list_of_descriptions
