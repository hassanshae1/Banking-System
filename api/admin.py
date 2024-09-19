from django.contrib import admin
# from __future__ import unicode_literals

from .models import (
    Branch,
    Bank,
)

# Register your models here.
admin.site.register(Branch)
admin.site.register(Bank)

