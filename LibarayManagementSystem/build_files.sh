echo "BUILD START"
python3.10.9 -m install -r requirments.txt
python3.10.9 manage.py collectstatic --noinput --clear
echo "BUILD START"