from django.db import models

class ProductDetails(models.Model):
    name=models.CharField(max_length=100)
    quantity=models.IntegerField()
    price=models.IntegerField()
    image=models.ImageField(upload_to='image')
    def __str__(self):
        return '{}'.format(self.name)

