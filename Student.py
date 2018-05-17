from peewee import *

db=SqliteDatabase('students.db')

class Student(Model):
    username= CharField(max_length=255, unique=True)
    points= IntegerField (default=0)

    class Meta:
        database=db
students=[
    {'username':'Aldo',
    'points': 5},
    {'username':'Rudy',
    'points': 6},
    {'username':'Jefferson',
    'points': 7},
    {'username':'Juan',
    'points': 8},
    {'username':'Oscar',
    'points': 8}
]
#METODOS PARA ADÑADIR ESTUDIANTES

def add_students():
    for student in students:
        try:
            Student.create(username=student['username'],
                            points=student['points'])
        except IntegrityError:
            #CUANDO NO EXISTA EL USUARIO SALE ERROR
            student_records=Student.get(username=student['username'])
            student_records.points=student['points']
            student_records.save() #para guardar

#metodo que me obtenga la calificacion mas alta
def top_student():
    topcalif= Student.select().order_by(Student.points.desc()).get()
    return topcalif

if __name__ == '__main__':
    db.connect() # permite coneccion a la base de datos
    db.create_tables([Student],safe=True) #crear tablas
    add_students()
    print('La mejor calificacion es : {}'.format(top_student().username))
