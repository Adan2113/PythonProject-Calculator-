from django.db import models

class UserQuery(models.Model):
    user_id = models.BigIntegerField()
    expression = models.CharField(max_length=255)
    result = models.CharField(max_length=50)
    answer = models.TextField(verbose_name="Ответ поддержки", blank=True, null=True) # Новое поле!
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id}: {self.expression} = {self.result}"