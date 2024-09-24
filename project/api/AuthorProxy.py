from django.db import models
from .models import Author


class AuthorProxy(Author):
    class Meta:
        ordering = ["name"]
        verbose_name = "Author Proxy"
        verbose_name_plural = "Authors Proxy"
        proxy = True

    def get_age(self):
        from datetime import date

        return date.today().year - self.birth_date.year
