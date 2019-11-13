# introtorhythm.com

![Travis CI build badge](https://api.travis-ci.com/seanpierce/introtorhythm.com.svg?branch=master) ![Test coverage badge](coverage.svg)

Intro To Rhythm is a freeform mix series and live-streaming audio station that began in 2017. All episodes and content are owned by their creators and made exclusively for Intro To Rhythm.

Additionally, ITR is dedicated to open-source projects, and the collective idea sharing that fuels creative expression. If you're interested in developing your own live-streaming station or podcasting platform, you're invited to refer to ITR's source code (Licence MIT).

Send questions and comments to introtorhythm@gmail.com

-----

The purpose of this project it to take what I've learned with the [initial django build for introtorhythm.com](https://github.com/seanpierce/introtorhythm.com-archive), and rebuild it to be cleaner and scalable.

**Specific goals:**

* Unit tesable (ongoing) ✓
  * Add coverage badge to README ✓
* CI/CD pipeline (in progress with Travis CI)
* Integration with VueJS ✓
* Exposed (and enhanced) _Subscriber_ and _Episodes_ API

## Installation

```shell
# download repo
git clone [this repo] introtorhythm.com

# set up virtual environment
python -m venv introtorhythm.com/

# install dependencies
cd introtorhythm.com
pip install -r requirements.txt
```

## Versions

* Django 2.2.4
* Python 3.6.3

## Usage

```shell
# navigate into the project root
# cd introtorhythm.com

# activate the virtual environment
source ./venv/bin/activate # mac/ linux
source ./venv/Scripts/activate # windows

# migrate the database tables
python manage.py migrate

# run unit tests
python scripts/run-tests.py

# build front end application
cd app
yarn
yarn run serve

# start the development server
cd ../
python manage.py runserver
```
