from django.db import models
# from django.db.models import DEFERRED

# @classmethod
# def from_db(cls, db, field_names, values):

#     if len(values) != len(cls._meta.concrete_fields):
#         values = list(values)
#         values.reverse()
#         values = [
#             values.pop() if f.attname in field_names else DEFERRED
#             for f in cls._meta.concrete_fields
#         ]
#     instance = cls(*values)
#     instance._state.adding = False
#     instance._state.db = db
#     # customization to store the original field values on the instance
#     instance._loaded_values = dict(zip(field_names, values))
#     return instance

# def save(self, *args, **kwargs):
#     # Check how the current values differ from ._loaded_values. For example,
#     # prevent changing the creator_id of the model. (This example doesn't
#     # support cases where 'creator_id' is deferred).
#     if not self._state.adding and (
#             self.creator_id != self._loaded_values['creator_id']):
#         raise ValueError("Updating the value of creator isn't allowed")
#     super().save(*args, **kwargs)

# class Instancmodel(models.Model):
#     title = models.CharField(max_length=100)

#     @classmethod
#     def create(cls, title):
#         book = cls(title=title)
#         # do something with the book
#         # if Instancmodel.objects.filter(title='name'):
        
#         print(Instancmodel.objects.all())
            
#         return book

        
# book = Instancmodel.create('the test book')


# class Book2Manager(models.Manager):
#     def create_book(self, title):
#         book = self.create(title=title)
#         # do something with the book
#         return book

# class Book2(models.Model):
#     title = models.CharField(max_length=100)

#     objects = Book2Manager()

# book = Book2.objects.create_book("Pride and Prejudice")