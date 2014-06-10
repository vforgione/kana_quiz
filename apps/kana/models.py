from django.db import models


class Character(models.Model):

    romaji = models.CharField(max_length=3)
    hiragana = models.CharField(max_length=2, unique=True)
    katakana = models.CharField(max_length=2, unique=True)
    is_dakuten = models.BooleanField()
    is_handakuten = models.BooleanField()
    is_yoon = models.BooleanField()
    gojuon_row = models.IntegerField()
    gojuon_col = models.IntegerField()
    notes = models.TextField(null=True, blank=True, default=None)

    def __str__(self):
        return self.romaji
