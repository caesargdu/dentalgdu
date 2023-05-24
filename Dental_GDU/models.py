from django.db import models



class Person(models.Model):
    nume = models.CharField(max_length=100)
    varsta = models.IntegerField()
    email = models.EmailField()
    # Add more fields as per your requirements

    def __str__(self):
        return self.nume

class Note(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='notes')
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    # Add more fields as per your requirements

    def __str__(self):
        return f"Note for {self.patient.nume} - {self.date}"

