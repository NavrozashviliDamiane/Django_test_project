from django.db import models


class Pizzeria(models.Model):
    pizzeria_name = models.CharField(max_length=200, blank=False)
    street = models.CharField(max_length=400, blank=True)
    city = models.CharField(max_length=400, blank=True)
    description = models.TextField(blank=True)
    logo_image = models.ImageField(upload_to='pizzeriaImages', blank=True, 
                                   default="pizzeriaImages/pizzalogo.png")
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{}, {}".format(self.pizzeria_name, self.city)


class Image(models.Model):
    Pizzeria = models.ForeignKey(Pizzeria, on_delete=models.CASCADE, related_name='pizzeria_images', blank=True, null=True)
    image = models.ImageField(upload_to='photos', blank=True)
    image_title = models.CharField(max_length=120, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']
