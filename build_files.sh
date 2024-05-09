echo "Build Start"
python3 manage.py makemigrations
python3 manage.py migrate

echo "Build End"