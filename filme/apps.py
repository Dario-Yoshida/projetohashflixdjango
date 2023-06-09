from django.apps import AppConfig


class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'

    def ready(self):
        from .models import Usuario
        import os

        email = os.getenv("EMAIL_ADMIN")
        senha = os.getenv("SENHA_ADMIN")

        usuario = Usuario.objects.filter(email=email)
        print(usuario)
        print(email)
        print(senha)
        if not usuario:
            Usuario.objects.create_superuser(username="Yoiti", email=email, password=senha, is_active=True, is_staff=True)

