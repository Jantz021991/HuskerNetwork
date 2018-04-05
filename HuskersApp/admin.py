from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Group, Venue, Post, Player





# Register your models here.


class VenueList(admin.ModelAdmin):
    list_display = ('name', 'address_line_1', 'address_line_2', 'city', 'state', 'country')
    list_filter = ('name', 'city', 'state')
    search_fields = ('name', 'city', 'state')

class GroupList(admin.ModelAdmin):
    list_display = ('name', 'venue', 'meeting_time', 'groupAdmin', 'hashtag',)
    list_filter = ('name', 'venue', 'meeting_time')
    search_fields = ('name', 'venue')


class PostList(admin.ModelAdmin):
    list_display = ('post_text', 'group', 'user')
    list_filter = ('group',)
    search_fields = ('group',)

class PlayerInline(admin.StackedInline):
    model = Player
    can_delete = False
    verbose_name_plural = 'player'

class UserAdmin(BaseUserAdmin):
    inlines = (PlayerInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupList)
admin.site.register(Venue, VenueList)
admin.site.register(Post, PostList)

