from django.db import models

# Create your models here.
class djangoClasses(models.Model):
    title = models.CharField(max_length=60)
    course_number = models.IntegerField()
    instructor_name = models.CharField(max_length=60)
    duration = models.FloatField(max_length=100)

    objects = models.Manager()

    def __str__(self):
        return self.title


class1 = djangoClasses.objects.create(title="Economics", course_number=101, instructor_name="Bob Smith", duration=1.5)

class2 = djangoClasses.objects.create(title="Algebra", course_number=102, instructor_name="Carol Danvers", duration=3)

class3 = djangoClasses.objects.create(title="History", course_number=103, instructor_name="Henry Johnson", duration=3)


