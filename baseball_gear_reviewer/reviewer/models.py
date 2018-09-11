from django.db import models

# Create your models here.
class Bats(models.Model):
    bat_make = models.CharField(max_length=100)
    bat_model = models.CharField(max_length=100)
    bat_image_url = models.CharField(max_length=200, null=True)
    bat_description = models.CharField(max_length=300)
    bat_details = models.CharField(max_length=300)

class Gloves(models.Model):
    glove_make = models.CharField(max_length=100)
    glove_model = models.CharField(max_length=100)
    glove_image_url = models.CharField(max_length=200, null=True)
    glove_description = models.CharField(max_length=300)
    glove_details = models.CharField(max_length=300)

class Balls(models.Model):
    ball_make = models.CharField(max_length=100)
    ball_model = models.CharField(max_length=100)
    ball_image_url = models.CharField(max_length=200, null=True)
    ball_description = models.CharField(max_length=300)
  

class Helmets(models.Model):
    helmet_make = models.CharField(max_length=100)
    helmet_model = models.CharField(max_length=100)
    helmet_image_url = models.CharField(max_length=200, null=True)
    helmet_description = models.CharField(max_length=300)


class Bats_Review(models.Model):
    review = models.CharField(max_length=300)
    rating_number = models.CharField(max_length=5)
    recommend = models.CharField()
    id = models.ForeignKey(Bats, on_delete=models.CASCADE, related_name='bats_review')

class Gloves_Review(models.Model):
    review = models.CharField(max_length=300)
    rating_number = models.CharField(max_length=5)
    recommend = models.CharField()
    id = models.ForeignKey(Gloves, on_delete=models.CASCADE, related_name='gloves_review')

class Balls_Review(models.Model):
    review = models.CharField(max_length=300)
    rating_number = models.CharField(max_length=5)
    recommend = models.CharField()
    id = models.ForeignKey(Balls, on_delete=models.CASCADE, related_name='balls_review')

class Helmets_Review(models.Model):
    review = models.CharField(max_length=300)
    rating_number = models.CharField(max_length=5)
    recommend = models.CharField()
    id = models.ForeignKey(Bats, on_delete=models.CASCADE, related_name='helmets_review')