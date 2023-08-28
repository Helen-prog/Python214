from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.conf import settings


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True)
    is_verify_email = models.BooleanField(default=False, verbose_name="Подтверждение электронной почты")


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f"EmailVerification object for {self.user.email}"

    class Meta:
        verbose_name = "верификацию"
        verbose_name_plural = "Верификация по почте"

    def send_verification_email(self):
        send_mail(
            "Subject here",
            "Here is the message.",
            settings.EMAIL_HOST_USER,
            [self.user.email],
            fail_silently=False,
        )
