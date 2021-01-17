import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModeTest(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        pub_date 미래시점이면 was_published_recently() 는 False 반환해야 한다.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
