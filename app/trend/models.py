from django.db import models

class Trend(models.Model):

    id = models.AutoField(primary_key=True)
    context = models.CharField(max_length=200)
    event = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.context
    class Meta:
        db_table = 'trend'