from src.tests.domainTests import PersonDomainTest, ActivityDomainTest
from src.tests.repoTests import AllRepoTest
from src.tests.serviceTests import AllServiceTest
from src.repo.personRepository import PersonRepository
from src.repo.activityRepository import ActivityRepository
from src.service.personService import PersonService
from src.service.activityService import ActivityService
from src.ui.ui import UI

if __name__ == '__main__':
    """
    The main function
    """
    testPersonDomain = PersonDomainTest()
    testPersonDomain.all_tests()
    testActivityDomain = ActivityDomainTest()
    testActivityDomain.all_tests()
    testRepo = AllRepoTest()
    testRepo.all_tests()
    testService = AllServiceTest()
    testService.all_tests()
    person_repository = PersonRepository()
    activity_repository = ActivityRepository(person_repository)
    person_service = PersonService(person_repository, generate=True)
    activity_service = ActivityService(activity_repository, person_repository, person_service, generate=True)
    ui = UI(person_service, activity_service)
    ui.create_menu()
