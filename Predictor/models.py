from django.db import models

# Create your models here.
class Prediction(models.Model):
    location = models.CharField(max_length=50)
    area = models.IntegerField()
    bhk = models.IntegerField()
    bathrooms = models.IntegerField()
    property_age = models.IntegerField()
    furnishing = models.CharField(max_length=20)
    estimated_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.location} - {self.area} sq ft"

    # Shows the price in Indian format, e.g. 9775500 -> 97,75,500
    def formatted_price(self):
        digits = str(self.estimated_price)
        if len(digits) <= 3:
            return digits
        last_three = digits[-3:]
        rest = digits[:-3]
        parts = []
        while len(rest) > 2:
            parts.insert(0, rest[-2:])
            rest = rest[:-2]
        if rest:
            parts.insert(0, rest)
        return ",".join(parts) + "," + last_three