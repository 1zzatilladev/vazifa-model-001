from django.db import models

# Create your models here.
class Tree(models.Model):
    name=models.CharField(max_length=233,null=False)
    age = models.PositiveSmallIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
class AppleTree(models.Model):
    name=models.CharField(max_length=233,null=False)
    tree=models.ForeignKey(Tree,on_delete=models.CASCADE)
    fruit_count=models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Cheese(models.Model):
    name=models.CharField(max_length=233,null=False)
    milk_type=models.CharField(max_length=233,null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
class Milk(models.Model):
    name=models.CharField(max_length=233,null=False)
    cheeses=models.ManyToManyField(Cheese,blank=True, related_name="milks")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
class NutTree(Tree):
    nut_count = models.PositiveIntegerField()

class Orchard(models.Model):
    name = models.CharField(max_length=233)
    trees = models.ManyToManyField(Tree, related_name="orchards")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class House(models.Model):
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Apartment(House):
    floor = models.PositiveSmallIntegerField()

class Villa(House):
    yard_count=models.PositiveSmallIntegerField()

class Fruit(models.Model):
    name = models.CharField(max_length=233)
    trees = models.ForeignKey(Tree,on_delete=models.CASCADE, related_name="fruits")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Village(models.Model):
    name = models.CharField(max_length=233)
    location = models.CharField(max_length=233)
    tree = models.OneToOneField(Tree, on_delete=models.CASCADE, related_name="village")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name



class NeighborTree(models.Model):
    trees = models.ManyToManyField(Tree, related_name="neighbors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




