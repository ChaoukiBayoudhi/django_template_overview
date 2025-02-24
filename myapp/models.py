from django.db import models

class Course(models.Model):
    #id=models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100,unique=True)
    language = models.CharField(max_length=100)
    duration=models.DurationField()
    description = models.TextField(null=True,blank=True)
    coefficient=models.FloatField()
    startDate=models.DateField(auto_now_add=True)
    photo=models.ImageField(upload_to='/images/course_photos',blank=True)

    class Meta:
        db_table='courses'
        #ordering=['title']#asc
        ordering=['-name']#desc
#2nd possibility : using models.TextChoices
#define a new type that have many possible choices
class TutorGrade(models.TextChoices):
    ASSISTANT=('ASS','Assistant Tutor')
    EXPERT=('EXP','Expert')
    PROFESSOR=('PROF','Professor')

class Tutor(models.model):
    name=models.CharField(max_length=100)
    familyName=models.CharField(max_length=100)
    birthdate =models.DateField()
    email=models.EmailField()
    photo=models.ImageField(upload_to="/images/tutor_photos",blank=True,null=True)
    #1st possiblity : using list of tuples
    """ grade=models.CharField(max_length=20,choices=
                           [('ASS','Assistant Tutor'),
                            ('MA','Master Assistance'),
                            ('PROF','Professor'),
                            ('EXP','Expert')],
                            default='EXP')
    """
    grade=models.CharField(max_length=20,choices=TutorGrade.choices,default=TutorGrade.EXPERT)
    class Meta:
        db_table='tutors'
        ordering=['name','familyName']
class Location(models.Model):
    locationNumber=models.CharField(max_length=50)
    streetName=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    zipCode=models.PositiveIntegerField()
    class Meta:
        db_table='locations'
        constraints=[models.UniqueConstraint(
            fields=['locationNumber','streetName','zipCode'],
            name='unique_number_street_zip')]

class Student(models.Model):
    cin=models.CharField(max_length=8,primary_key=True)
    name=models.CharField(max_length=100)
    familyName=models.CharField(max_length=100)
    birthdate =models.DateField()
    email=models.EmailField()
    class Meta:
        db_table='students'
        ordering=['name','familyName']
class Enrollment(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    enrollmentDate=models.DateField(auto_now_add=True)
    result=models.FloatField()
    class Meta:
        db_table='enrollments'
        ordering=['-enrollmentDate']

class Profile(models.Model):
    linkedIn=models.URLField()
    github=models.URLField()
    photo=models.ImageField(upload_to="/images/profile_photos",blank=True,null=True)
    #relationship between Profile and Student (1-1 )
    student=models.OneToOneField(Student,on_delete=models.CASCADE)
    class Meta:
        db_table='profiles'
        ordering=['linkedIn']
