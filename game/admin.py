from django.contrib import admin
from game.models import PlayerChar
from game.models import ItemsOfWorld

# Register your models here.
admin.site.register(PlayerChar)
admin.site.register(ItemsOfWorld)