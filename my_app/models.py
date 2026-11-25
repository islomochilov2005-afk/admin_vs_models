from django.db import models

class Kitob(models.Model):
    title=models.CharField(max_length=512)
    description=models.TextField()
    page_count=models.IntegerField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    created_at=models.DateField()

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitob"

    def __str__(self):
        return self.title


class Cars(models.Model):
    name=models.CharField(max_length=120)


    def __str__(self):
        return self.name



