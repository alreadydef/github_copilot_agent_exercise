from django.test import TestCase
from rest_framework.test import APIClient
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name='TestTeam')
        user = User.objects.create_user(username='testuser', email='test@test.com', password='testpass', team=team)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.team, team)


class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Avengers')
        self.assertEqual(str(team), 'Avengers')


class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name='TestTeam')
        user = User.objects.create_user(username='testuser', email='test@test.com', password='testpass', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=30)
        self.assertEqual(activity.type, 'run')
        self.assertEqual(activity.duration, 30)


class LeaderboardModelTest(TestCase):
    def test_create_leaderboard_entry(self):
        team = Team.objects.create(name='TestTeam')
        user = User.objects.create_user(username='testuser', email='test@test.com', password='testpass', team=team)
        entry = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(entry.score, 100)


class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Morning Run', description='A morning cardio run')
        self.assertEqual(workout.name, 'Morning Run')

    def test_create_workout_with_schedule_and_max_attendance(self):
        workout = Workout.objects.create(
            name='Manga Maniacs',
            description='Explore the fantastic stories of the most interesting characters from Japanese Manga (graphic novels).',
            schedule='Tuesdays at 5pm',
            max_attendance=25,
        )
        self.assertEqual(workout.name, 'Manga Maniacs')
        self.assertEqual(workout.schedule, 'Tuesdays at 5pm')
        self.assertEqual(workout.max_attendance, 25)


class APIEndpointTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_api_root(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)

    def test_users_endpoint(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)

    def test_teams_endpoint(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, 200)

    def test_activities_endpoint(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, 200)

    def test_leaderboard_endpoint(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, 200)

    def test_workouts_endpoint(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, 200)
