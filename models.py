from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    copies = models.IntegerField()

    CONTENT_RATINGS = [('U',"Unrestricted public exhibition"), 
                       ('UA',"Parental guidance required for children under 12"),
                       ('S',"Restricted audience"),
                       ('A',"Adults only")]
    content = models.CharField(max_length=2, choices=CONTENT_RATINGS, default='U')

    def __str__(self):
        return self.title

   
    
class Member(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    email = models.EmailField()
    mobile = models.BigIntegerField()
    dob = models.DateField()
    password = models.CharField(max_length=50)

    MEMBER_TYPE = [('MEMBER',"Member"), ('LIBRARIAN',"Librarian")]
    type = models.CharField(max_length=10, choices=MEMBER_TYPE, default="MEMBER")

    def __str__(self):
        return self.name

    

class Record(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrowed_on = models.DateField(blank=True)
    return_by = models.DateField(blank=True)

    RESPONSE_TYPE = [("Accepted",'ACCEPT'), ("Denied", 'DENY')]
    book_response = models.CharField(max_length=10, choices=RESPONSE_TYPE, default="Denied")

    
 
