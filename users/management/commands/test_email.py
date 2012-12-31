from django.core.management.base import BaseCommand, CommandError
from django.core.mail import EmailMessage

from users.models import User

class Command(BaseCommand):
    args = ''
    help = 'Sends all users a test message'

    def handle(self, *args, **options):
        all_users = User.objects.all()
        bcc_list = []
        for user in all_users:
            if user.email:
                bcc_list.append(user.email)
                self.stdout.write('Added email "%s"\n' % user.email)
        
        message = EmailMessage("Test Message from 3ND", 
                               "This is a test message from the 3ND site, please ignore", 
                               "3ndteam@gmail.com",
                               ["3ndteam@gmail.com"],
                               bcc = bcc_list)
        
        self.stdout.write('Constructed test email message\n')
        message.send(fail_silently = False)
        self.stdout.write('Sent test email message\n')
        # self.stdout.write('Successfully sent email to poll "%s"' % poll_id)