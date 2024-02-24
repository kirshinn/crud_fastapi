# local

pip install fastapi uvicorn sqlalchemy alembic

pip freeze > requirements.txt

python main.py

# docker

## build docker image
docker build --no-cache -t crud_fastapi:latest .

## run docker container
docker run -p 8080:8080 -v ./:/code/ --name=crud_fastapi -d crud_fastapi
