from django.contrib.auth.models import User
from django.db import models

class Purchase(models.Model):
    class PuchaseStatus(models.IntegerChoices):
        CHOSEN = 1, 'Chosen'
        WAITING_PAYMENT = 2, 'Waiting Payment'
        SENT = 3, 'sent'
        DELIVERED = 4, 'Delivered'
        FINALIZED = 5, 'Finalized'
        
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='purchases')
    status = models.IntegerField(choices=PuchaseStatus.choices,
                                        default=PuchaseStatus.CHOSEN)
    def __str__(self):
        return "{} in status {}".format(self.user.username,self.status.__str__())
    