fd setup.py |xargs dirname | xargs -i pip install -e "{}/." --config-settings editable_mode=compat

