from django.db import models


class Blog(models.Model):
    Blog_Photo = models.ImageField(upload_to='Blog_Photo')
    Blog_Title = models.TextField()
    Blog_Composition = models.TextField()
    Date_Posted = models.TextField()

    def __str__(self):
        return self.Blog_Title + self.Blog_Composition


class Poetry(models.Model):
    Poem_Title = models.TextField()
    Poem_Composition = models.TextField()
    Poem_Photo = models.ImageField(upload_to='Poetry_Photos/')
    Date_Posted = models.TextField()

    def __str__(self):
        return self.Poem_Title + self.Poem_Composition + self.Date_Posted


class Fashion(models.Model):
    Description = models.TextField()
    Fashion_Photo = models.ImageField(upload_to='Fashion/')
    Fashion_Title = models.TextField()
    Date_Posted = models.TextField()

    def __str__(self):
        return self.Description + self.Fashion_Title + self.Date_Posted
