from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(
        'Почта',
        max_length=200,
        unique=True,
    )
    username = models.CharField(
        'Юзернейм',
        max_length=200,
        unique=True
    )
    USERNAME_FIELD = ('email')
    REQUIRED_FIELDS = ('password', 'username')

    class Meta:
        ordering = ('username',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username


class File(models.Model):
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='files',
        verbose_name='Автор'
    )
    file = models.FileField(
        'Файл',
        upload_to='files/',
        null=False,
        blank=False,
        validators=[FileExtensionValidator(allowed_extensions=['py'])]
    )
    new = models.BooleanField(
        'Новый файл',
        default=True
    )
    review = models.CharField(
        'Ревью',
        max_length=1000,
        default=None,
        null=True,
        blank=True
    )
