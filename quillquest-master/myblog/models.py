from django.db import models

class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('tech', 'Tech'),
        ('sports', 'Sports'),
        ('politics', 'Politics'),
        ('adventure', 'Adventure'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='tech')  # Change 'tech' to your desired default value

    def __str__(self):
        return self.title

