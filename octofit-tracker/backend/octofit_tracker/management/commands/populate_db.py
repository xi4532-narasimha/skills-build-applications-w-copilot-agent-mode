from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            # Clear existing data
            Activity.objects.all().delete()
            Leaderboard.objects.all().delete()
            Workout.objects.all().delete()
            User.objects.all().delete()
            Team.objects.all().delete()

            # Create Teams
            marvel = Team.objects.create(name='Marvel')
            dc = Team.objects.create(name='DC')

            # Create Users
            users = [
                User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
                User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
                User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
                User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            ]

            # Create Activities
            Activity.objects.create(user=users[0], type='Running', duration=30, date='2024-01-01')
            Activity.objects.create(user=users[1], type='Cycling', duration=45, date='2024-01-02')
            Activity.objects.create(user=users[2], type='Swimming', duration=60, date='2024-01-03')
            Activity.objects.create(user=users[3], type='Yoga', duration=40, date='2024-01-04')

            # Create Workouts
            w1 = Workout.objects.create(name='Hero Strength', description='Strength workout for heroes')
            w2 = Workout.objects.create(name='Agility Boost', description='Agility and speed workout')
            w1.suggested_for.set([users[0], users[2]])
            w2.suggested_for.set([users[1], users[3]])

            # Create Leaderboard
            Leaderboard.objects.create(team=marvel, points=150)
            Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
