fd setup.py |xargs dirname | xargs -i echo "{}/." | xargs pip install

