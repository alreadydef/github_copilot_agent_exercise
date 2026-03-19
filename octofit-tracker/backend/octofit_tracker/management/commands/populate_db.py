from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Очистка данных
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Создание команд
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Создание пользователей
        tony = User.objects.create_user(username='tony', email='tony@marvel.com', password='ironman', team=marvel)
        steve = User.objects.create_user(username='steve', email='steve@marvel.com', password='cap', team=marvel)
        bruce = User.objects.create_user(username='bruce', email='bruce@marvel.com', password='hulk', team=marvel)
        clark = User.objects.create_user(username='clark', email='clark@dc.com', password='superman', team=dc)
        bruce_dc = User.objects.create_user(username='bruce_dc', email='bruce@dc.com', password='batman', team=dc)
        diana = User.objects.create_user(username='diana', email='diana@dc.com', password='wonderwoman', team=dc)

        # Создание активностей
        Activity.objects.create(user=tony, type='run', duration=30)
        Activity.objects.create(user=steve, type='cycle', duration=45)
        Activity.objects.create(user=bruce, type='swim', duration=60)
        Activity.objects.create(user=clark, type='fly', duration=120)
        Activity.objects.create(user=bruce_dc, type='fight', duration=90)
        Activity.objects.create(user=diana, type='train', duration=50)

        # Создание тренировок
        Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes')
        Workout.objects.create(name='Strength Training', description='Strength for all heroes')

        # Лидерборд
        Leaderboard.objects.create(user=tony, score=100)
        Leaderboard.objects.create(user=clark, score=120)
        Leaderboard.objects.create(user=steve, score=90)
        Leaderboard.objects.create(user=bruce, score=80)
        Leaderboard.objects.create(user=bruce_dc, score=110)
        Leaderboard.objects.create(user=diana, score=95)

        self.stdout.write(self.style.SUCCESS('octofit_db успешно заполнена тестовыми данными!'))
