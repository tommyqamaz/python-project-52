[![Actions Status](https://github.com/tommyqamaz/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/tommyqamaz/python-project-52/blob/main/.github/workflows/hexlet-check.yml)
[![Project-check](https://github.com/tommyqamaz/python-project-52/actions/workflows/python-check.yml/badge.svg)](https://github.com/tommyqamaz/python-project-52/blob/main/.github/workflows/python-check.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/df31073a15237d90b400/maintainability)](https://codeclimate.com/github/tommyqamaz/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/df31073a15237d90b400/test_coverage)](https://codeclimate.com/github/tommyqamaz/python-project-52/test_coverage)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Task management
Is the process of managing a task through its life cycle. It involves planning, testing, tracking, and reporting. Task management can help either individual achieve goals, or groups of individuals collaborate and share knowledge for the accomplishment of collective goals.
- Task Manager - This is a web application that is used to remind you of scheduled events. 
- It can be used by several users at the same time.
- Registration and authorization are implemented.
- Tasks have labels and statuses.
- The application works with all kinds of databases.
- Russian and English languages are supported (see locale).
- Deployed at Heroku (until November 29 2022 (free dyno expired))
## Usage
Follow the [link](https://s777s.herokuapp.com/), register and enjoy
## Installation
1. `git clone git@github.com:tommyqamaz/task-manager.git`
2. Create .env file with the following contents:
```
SECRET_KEY= ...# your django key here (len=50)
DATABASE_URL=sqlite:///db.sqlite3 # sqlite3 for example
ROLLBAR_TOKEN= ... # Rollbar token for error tracking
```
3.a Use docker
```
docker build --tag task_manager:latest .
docker run -itd -p 8000:8000 task_manager
```
3.b Use poetry with python >= 3.8.13
```
make setup
make run
```
## Technologies
- Django, Python
- Error tracking with Rollbar
- CI/CD with GitHub Actions (one pipeline created by hexlet and one by me)
- Test coverage with coverage
- Heroku, gunicorn
- bootstrap4
- black, flake8
## Screenshots
![index scrn](/images/main.png "index")
![register scrn](/images/register.png "register")
![tasks scrn](/images/tasks.png "tasks")
![create_task scrn](/images/create_task.png "create task")
