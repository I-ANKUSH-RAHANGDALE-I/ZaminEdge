
echo "BUILD START"
python3.2.0 -m pip install requirement.txt
python3.2.0 manage.py collectstatic --noinput --clear
echo "BUILD END"