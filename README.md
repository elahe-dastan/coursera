docker compose up

uvicorn main:app --workers=5

curl 127.0.0.1:8000/students

curl -d '{"id":"9631036", "first_name":"elahe", "last_name":"dastan", "registration_date":"1396-07-01", "average":"18.1"}' -H "Content-Type: application/json" -X POST 127.0.0.1:8000/students
