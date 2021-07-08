from django.contrib import admin
from .models import Venue,Event,MyClubUser


#admin.site.register(Venue)
#admin.site.register(Event)
#admin.site.register(MyClubUser)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name','address','phone')
    ordering = ('name',)
    search_fields= ('name','address','phone','email')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name','event_date','venue')
    ordering = ('event_date',)
    search_fields = ('name','venue__name','venue__zip_code','venue__address','event_date')

@admin.register(MyClubUser)
class AdminMyclubUser(admin.ModelAdmin):
    list_display=('first_name','last_name','user_email')
    search_fields=('first_name','user_email','last_name')
    ordering = ('first_name',)




