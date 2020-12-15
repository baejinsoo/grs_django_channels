from django.db import models


TAG_CHOICES = (
            ("", "Select Tag"),
            ("0", "사원"),
            ("1", "대리"),
            ("2", "팀장"),
            ("3", "과장"),
            ("4", "부장"),
            ("5", "사장"),
        )

class User(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=100, null=True)
    # thumbnail = models.ImageField(upload_to='images/',blank=True, null=True)
    user_rank = models.CharField(choices=TAG_CHOICES, max_length=100)
    birth = models.CharField(max_length=100)

    def __str__(self):
        return self.user_id

class photo(models.Model):
    img_name = models.CharField(max_length=100)
    img = models.FileField()
    
    def __str__(self):
        return self.img_name
