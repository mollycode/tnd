from django.core.management.base import BaseCommand, CommandError

from courses.models import *

class Command(BaseCommand):
    args = ''
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        try:
            pass
        except Poll.DoesNotExist:
            raise CommandError('Error in adding testing courses')

        self.stdout.write('Successfully added courses\n')
        
def cambron():
    instructor = Instructor(name = 'Keith Cambron')
    with open('/images/cambron.jpg', 'r') as f:
        instructor.image = f
    instructor.save()
    
def how_internet_works():
    course = Course()