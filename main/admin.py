from django.contrib import admin

from .models import Message,Ticket


class MessagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticket', 'author',)
    list_display_links = ('ticket', 'author',)
    search_fields = ('ticket', 'author',)
    ordering = ('ticket',)


class TicketsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creator', 'status', 'created_at', 'updated_at')
    list_display_links = ('title', 'creator', 'status')
    search_fields = ('title', 'creator')
    ordering = ('ticket',)


admin.site.register(Message, MessagesAdmin)
admin.site.register(Ticket, TicketsAdmin)
