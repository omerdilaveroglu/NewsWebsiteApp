from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class News(models.Model):
    header = models.CharField(max_length=250, blank=False, null=False)
    description = models.CharField(max_length=5000, blank=False, null=False)
    image = models.ImageField(upload_to="images/", null=True)
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.PROTECT)
    datetime = models.DateTimeField(verbose_name="DateTime", auto_now_add=True, null=False, blank=False)

    def category_id(self):
        return self.category.id if self.category else None

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
