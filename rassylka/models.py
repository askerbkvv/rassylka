from django.db import models

STATUS_CHOICES = (
    ('S', 'send'),
    ('N', 'not send'),
)


class Client(models.Model):
    number = models.PositiveIntegerField()
    code = models.CharField(max_length=10)
    tag = models.CharField(max_length=49, null=True, blank=False)
    time_zone = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class Links(models.Model):
    start_send_time = models.DateTimeField()
    text = models.TextField()
    tag = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    end_send_time = models.DateTimeField()

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'


class Message(models.Model):
    send_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    link = models.ForeignKey(Links, on_delete=models.CASCADE, related_name='messages')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages')

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
