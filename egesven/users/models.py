from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Usuario(AbstractUser):
    email = models.EmailField(_("Correo electrónico"), unique=True)
    direccion = models.CharField(_("Dirección"), max_length=255, blank=True, null=True)
    telefono = models.CharField(_("Teléfono"), max_length=15, blank=True, null=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="usuarios_personalizados",
        blank=True,
        verbose_name=_("Grupos"),
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="usuarios_personalizados",
        blank=True,
        verbose_name=_("Permisos de usuario"),
    )

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return f"{self.username} ({self.email})"


class Cliente(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cliente",
    )

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"Cliente: {self.usuario.username}"
