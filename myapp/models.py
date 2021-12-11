from django.db import models


class ProductType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.CharField(max_length=50)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} {self.type.name}"


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=300)
    text = models.CharField(max_length=500)

    def __str__(self) -> str:
        return f"{self.name} {self.email}"
