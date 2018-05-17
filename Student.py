from peewee import *

db=SqliteDatabase('students.db')

class Student(Model):
    username= CharField(max_length=255, unique=True)
    points= IntegerField (default=0)

    class Meta:
        database=db

if __name__ == '__main__':
    db.connect() # permite coneccion a la base de datos
    db.create_tables([Student],safe=True) #crear tablas
