from django.db import models


class Character(models.Model):

    # characters
    romaji = models.CharField(max_length=3)
    hiragana = models.CharField(max_length=2, unique=True)
    katakana = models.CharField(max_length=2, unique=True)
    # grouping indicators
    is_plain = models.BooleanField()
    is_dakuten = models.BooleanField()
    is_handakuten = models.BooleanField()
    is_yoon = models.BooleanField()
    # charting
    gojuon_row = models.IntegerField()
    gojuon_col = models.IntegerField()
    # extra
    alternate_romaji = models.CharField(max_length=3, null=True, blank=True, default=None)
    notes = models.TextField(null=True, blank=True, default=None)

    def save(self, *args, **kwargs):
        if self.is_handakuten:
            self.is_dakuten = True
        super(Character, self).save(*args, **kwargs)

    def __str__(self):
        return self.romaji
