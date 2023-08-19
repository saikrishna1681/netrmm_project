
from peewee import *

db = SqliteDatabase('my_app.db')

class BaseModel(Model):
    class Meta:
        database = db

class Script(BaseModel):

    name=CharField(max_length=100,null=False)
    body=TextField()

    def __str__(self):

        return f'{self.id}____{self.name}'

class ExecutionLog(BaseModel):

    script=ForeignKeyField(Script, backref="script")
    output=CharField(max_length=1)
    starttime=DateTimeField()
    endtime=DateTimeField()
    duration=DecimalField(max_digits=17, decimal_places=7)

    def __str__(self):

        return f'{self.id}'
    

# def create_tables():
#     with db:
#         db.create_tables([Script, ExecutionLog])
#     print("done")
    
# create_tables()