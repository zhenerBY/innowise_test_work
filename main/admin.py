from django.contrib import admin

from .models import Message,Ticket


class MessagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticket', 'author',)
    list_display_links = ('author',)
    search_fields = ('ticket', 'author',)
    ordering = ('ticket',)


class TicketsAdmin(admin.ModelAdmin):
    list_display = ('id', 'creator', 'status', 'created_at', 'updated_at')
    list_display_links = ('creator', 'status')
    search_fields = ('creator', 'status')
    ordering = ('ticket',)


admin.site.register(Message, MessagesAdmin)
admin.site.register(Ticket, TicketsAdmin)
