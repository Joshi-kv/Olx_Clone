from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class Thread(models.Model):
    first_person = models.ForeignKey(User,on_delete=models.CASCADE,related_name='first_person')
    second_person = models.ForeignKey(User,on_delete=models.CASCADE,related_name='second_person')
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['first_person', 'second_person']
    
    def __str__(self):
        return f"thread between {self.first_person} and {self.second_person} "
    
class Message(models.Model):
    thread = models.ForeignKey(Thread,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField()
    timstamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"message : {self.message}"    