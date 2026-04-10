# Basic tests for all endpoints
from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(name='Test', email='test@example.com', team='Marvel')
        self.assertEqual(user.email, 'test@example.com')
    def test_team_creation(self):
        team = Team.objects.create(name='Marvel', members=['a@b.com'])
        self.assertEqual(team.name, 'Marvel')
    def test_activity_creation(self):
        activity = Activity.objects.create(user_email='a@b.com', activity='Run', duration=10)
        self.assertEqual(activity.activity, 'Run')
    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(user_email='a@b.com', score=100)
        self.assertEqual(lb.score, 100)
    def test_workout_creation(self):
        workout = Workout.objects.create(name='Strength', description='desc')
        self.assertEqual(workout.name, 'Strength')
