from django.contrib import admin
from account.models import UserAccount



@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "date_created")
    list_filter = ("full_name", "email")
    search_fields = ("full_name", "email", "phone_number")
    list_per_page = 30
    actions = ("set_mobile_to_null", )

    def get_ordering(self, request):
        if request.user.is_superuser:
            return ("full_name", "email")
        return ("email")
    

    def set_mobile_to_null(self, request, queryset):
        phone_number_status = queryset.update(phone_number=None)
        self.message_user(request, "{} User(s) phonenumber set to none successfully.".format(phone_number_status))

    set_mobile_to_null.short_description = "Mark selected Users phonenumber to none"    