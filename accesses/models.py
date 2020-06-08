from django.db import models
from users.models import User
from editors.models import Editor


class Access(models.Model):
    SOCIALS = (
        (1, 'Instagram'),
        (2, 'Facebook'),
        (3, 'Telegram')
    )
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    social_name = models.IntegerField(choices=SOCIALS)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()

    def __str__(self):
        return f"{self.customer} to {self.editor}, from {self.date_start} to {self.date_end}"
