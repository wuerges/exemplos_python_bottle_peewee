import peewee

db = peewee.SqliteDatabase('banco.db')

class BaseModel(peewee.Model):
    class Meta:
        database = db

class Chamado(BaseModel):
    name = peewee.CharField()
    
try:
    Chamado.create_table()
    print("Tabela 'Chamado' criada com sucesso!")

    Chamado.create(name="Teste 1")
    
except peewee.OperationalError:
    print("Tabela 'Chamado' ja existe!")    