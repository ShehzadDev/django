from django.contrib import admin
from .models import Author
from django.utils import timezone  # Correct import for timezone


class BirthMonthFilter(admin.SimpleListFilter):
    title = "Birth Month"
    parameter_name = "birth_month"

    def lookups(self, request, model_admin):
        return [
            (1, "January"),
            (2, "February"),
            (3, "March"),
            (4, "April"),
            (5, "May"),
            (6, "June"),
            (7, "July"),
            (8, "August"),
            (9, "September"),
            (10, "October"),
            (11, "November"),
            (12, "December"),
        ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(birth_date__month=self.value())
        return queryset


@admin.action(description="Change Author Name")
def change_author_name(modeladmin, request, queryset):
    queryset.update(name="Deafult Name")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "birth_date", "is_birthday_today")
    list_filter = (BirthMonthFilter,)
    search_fields = ("name",)
    actions = [change_author_name]

    def is_birthday_today(self, obj):
        return obj.birth_date == timezone.now().date()

    is_birthday_today.short_description = "Birthday Today"
    is_birthday_today.boolean = True


admin.site.register(Author, AuthorAdmin)
