from django.contrib import admin

from .models import Question, Choice

# Any changes to admin page must be registered here

# Tells Django that Choice objects are edited on the Question admin page
# That's pretty cool
# Change the default admin.StackedInline to admin.TabularInline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date']}),
    # ]
    
    # List the details of each item in questions in a table format
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # Add the inline method here
    inlines = [ChoiceInline]
    # Add a search box on admin's page
    list_filter = ['pub_date']


admin.site.register(Question, QuestionAdmin)

