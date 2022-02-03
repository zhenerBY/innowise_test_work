from django.db import models


class Ticket(models.Model):
    class TicketStatus(models.TextChoices):
        OPEN = 'OPN', 'Open'
        CLOSED = 'CLD', 'Closed'
        FROZEN = 'FRO', 'Frozen'

    title = models.CharField(max_length=250, verbose_name='Title')
    creator = models.ForeignKey('auth.User',
                                on_delete=models.CASCADE,
                                verbose_name='creator',
                                related_name='Creator')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Created')
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Updated')
    status = models.CharField(max_length=3, choices=TicketStatus.choices, default=TicketStatus.OPEN)

    def __str__(self):
        return f'Ticket - {self.creator} | {self.title} | {self.status}'

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'


class Message(models.Model):
    text = models.TextField(verbose_name='Message text')
    ticket = models.ForeignKey(Ticket,
                               on_delete=models.CASCADE,
                               verbose_name='Ticket',
                               related_name='ticket_messages')
    author = models.ForeignKey('auth.User',
                               on_delete=models.CASCADE,
                               verbose_name='Author',
                               related_name='author')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Created')

    def __str__(self):
        return f'Message - {self.ticket}|{self.author}'

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
