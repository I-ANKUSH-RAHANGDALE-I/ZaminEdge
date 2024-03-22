echo "BUILD START"
python3.9 -m pip install requirement.txt
python3.9 manage.py collectstatic --noiput --clear
echo "BUILD END"