from django.db import models
  
class Theme(models.Model):
 
    # fields of the model
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'theme'