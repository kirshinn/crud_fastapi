from fastapi import FastAPI
import uvicorn

from app.database import SessionLocal, engine, Base
from app.routers import user as UserRouter

# Создание всех таблиц в базе данных
Base.metadata.create_all(bind=engine)

# Инициализация FastAPI
app = FastAPI()
app.include_router(UserRouter.router, prefix='/user')


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080, reload=True, workers=4)
