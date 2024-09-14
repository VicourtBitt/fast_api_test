from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import connect
from pydantic import BaseModel

# Criando uma instância do FastAPI 
app = FastAPI()

# Definindo configurações de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Definindo modelo de resposta
class UserGC24(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    course: str
    city: str
    phone: str
    userRegisterId: int

# Definindo a rota raiz da API
@app.get("/")
async def root():
    try: 
        connection = connect()
        cursor = connection.cursor()
        query = 'SELECT * FROM userInfo'
        cursor.execute(query)
        users = cursor.fetchall()
        connection.close()

    except Exception as e:
        return  {
            'error': str(e)
        }

    # Retornando um JSON
    return [
        UserGC24(
            id=user[0],
            name=user[1],
            age=user[2],
            gender=user[3],
            course=user[4],
            city=user[5],
            phone=user[6],
            userRegisterId=user[7]
        ) for user in users
    ]

@app.get("/user/{user_id}")
async def get_user(user_id: int):
    try: 
        connection = connect()
        cursor = connection.cursor()
        query = f'SELECT * FROM userInfo WHERE id = {user_id}'
        cursor.execute(query)
        user = cursor.fetchone()
        connection.close()

    except Exception as e:
        return  {
            'error': str(e)
        }

    # Retornando um JSON
    return UserGC24(
        id=user[0],
        name=user[1],
        age=user[2],
        gender=user[3],
        course=user[4],
        city=user[5],
        phone=user[6],
        userRegisterId=user[7]
    )
