from django.contrib import admin
from .models import empower, Testimonial
# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display = ('name', 'working')
    list_editable = ('working',)
    search_fields = ('name',)
    list_filter = ('working',)
admin.site.register(empower, EmpAdmin)
admin.site.register(Testimonial)