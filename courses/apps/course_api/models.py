from django.db import models

class course_info(models.Model):
    course_name = models.CharField(max_length=100,
                            null=False,
                            blank=False,
                            )

    course_author_name = models.CharField(max_length=100,
                            null=False,
                            blank=False,
                            )

    price = models.PositiveIntegerField(blank=False,
                                         null=False,
                                         verbose_name="Project Budget"
                                         )
    def __str__(self):
        return self.course_name