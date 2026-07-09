from django.db import models

# Create your models here.
class Empower(models.Model):
    name = models.CharField(max_length = 200)
    emp_ID = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 10)
    address = models.CharField(max_length = 150)
    working = models.BooleanField(default = True)
    department = models.CharField(max_length = 10)
    def __str__(self):
        return self.name
class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    testimonial = models.TextField()
    picture = models.ImageField(upload_to="testimonials/")
    rating = models.IntegerField()
    def __str__(self):
        return self.testimonial