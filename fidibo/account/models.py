from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



class UserAccount(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="FullName")
    email = models.EmailField(unique=True, verbose_name="Email")
    phone_number = PhoneNumberField(unique=True, region="IR", verbose_name="PhoneNumber")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="date")
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True, verbose_name="Profile_Picture")
    age = models.PositiveIntegerField(default=0)


    class Meta:
        db_table = "Profiles_Accounts"
        db_table_comment = "Stores Profiles and Accounts"
        order_with_respect_to = "full_name"
        unique_together = [["phone_number", "age"]]
        constraints = [
            models.CheckConstraint(condition=models.Q(age__gte=18), name="age_gte_18"),
        ]

    def __str__(self):
        return f"{self.full_name} - {self.email}"
    

    permissions = [
        ("can_view_profiles", "Can view user profiles"),
        ("can_edit_profiles", "Can edit user profiles"),
        ("can_delete_profiles", "Can delete user profiles")
    ]