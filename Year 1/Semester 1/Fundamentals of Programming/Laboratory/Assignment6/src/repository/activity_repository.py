class ActivityRepository:
    def __init__(self, activity_list=None):
        if activity_list is None:
            activity_list = []
        self._activity_list = activity_list

    @property
    def activities(self):
        return self._activity_list

    def add_activity(self, activity):
        self._activity_list = activity

    def remove_activity(self, activity):
        self._activity_list.remove(activity)
