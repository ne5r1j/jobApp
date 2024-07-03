from django.contrib import admin

from app.models import JobPost, Author, Location, Skills

class JobAdmin(admin.ModelAdmin):
  list_display = ('title', 'salary', 'date')
  list_filter = ("date","salary")
  search_fields = ['title']
  search_help_text = "Write in your query and hit enter"
  # fields = [('title', 'description'), 'expiry']
  # exclude = ('title',)
  fieldsets = (
    ("Basic information", {
      'fields': ('title', 'description')
    }),
    ("More information", {
      'classes': ('collapse',),
      'fields': ('salary', 'expiry', 'slug')
    })
  )

# Register your models here.
# admin.site.register(JobPost, JobAdmin)
admin.site.register(JobPost)
admin.site.register(Author)
admin.site.register(Location)
admin.site.register(Skills)

