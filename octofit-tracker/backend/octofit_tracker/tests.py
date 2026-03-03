from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        u1 = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        u2 = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        Activity.objects.create(user=u1, type='Running', duration=30, date='2024-01-01')
        Workout.objects.create(name='Hero Strength', description='Strength workout for heroes')
        Leaderboard.objects.create(team=marvel, points=100)

    def test_user_count(self):
        self.assertEqual(User.objects.count(), 2)
    def test_team_count(self):
        self.assertEqual(Team.objects.count(), 2)
    def test_activity_count(self):
        self.assertEqual(Activity.objects.count(), 1)
    def test_workout_count(self):
        self.assertEqual(Workout.objects.count(), 1)
    def test_leaderboard_count(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
