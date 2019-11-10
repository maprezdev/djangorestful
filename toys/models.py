from django.db import models

# Create your models here.
class Toy(models.Model):
    # Withing the Toy class we define the attributes what represents a database column or field.
    created = models.DateTimeField(auto_now_add = True)
    name = models.CharField(max_length = 150, blank = False, default = '')
    description = models.CharField(max_length = 250, blank = True, default = '')
    toy_category = models.CharField(max_length = 200, blank = False, default = '')
    release_date = models.DateTimeField()
    was_included_in_home = models.BooleanField(default = False)

    class Meta:
        # Order by the 'name' attribute in ascending order
        ordering = ('name',)