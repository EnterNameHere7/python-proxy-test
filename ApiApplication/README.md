# Local WSL2 setup

```bash

# fresh install
sudo apt update
sudo apt upgrade
sudo apt install python3-pip python3-venv
sudo ln -s /usr/bin/pip3 /usr/bin/pip

# create venv
python3 -m venv venv

# enter venv
source venv/bin/activate

# install needed packages
pip install wheel setuptools --no-cache-dir

# install packages if you have a requires file
pip install -r requirements.txt --no-cache-dir

# install needed packages
pip install <packages>

# save installed package list
pip freeze > requirements.txt

# exit venv
deactivate
```
