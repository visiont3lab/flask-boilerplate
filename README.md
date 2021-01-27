# Instructions

```
# Setup
virtualenv --python=python3 env
source env/bin/activate
pip install -r requirements.txt

# TO run 
flask run
or
gunicorn -w 4 -b 0.0.0.0:8000 app:app --threads 2 
```