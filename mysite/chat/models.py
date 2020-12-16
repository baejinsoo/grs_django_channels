from django.db import models


TAG_CHOICES = (
            ("", "Select Tag"),
            ("사원", "사원"),
            ("대리", "대리"),
            ("팀장", "팀장"),
            ("과장", "과장"),
            ("부장", "부장"),
            ("사장", "사장"),
        )

class User(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=100, null=True, blank=True)
    user_pic = models.ImageField(upload_to='',blank=True, null=True)
    user_rank = models.CharField(choices=TAG_CHOICES, max_length=100)
    birth = models.CharField(max_length=100)
    task= models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.user_id)

