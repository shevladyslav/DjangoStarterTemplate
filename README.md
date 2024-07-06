DjangoStarterTemplate
------------
The DjangoStarterTemplate is a foundational template designed to streamline the development process for new 
Django projects. This template provides a robust and flexible structure, pre-configured with essential settings 
and tools, allowing developers to quickly set up and start their projects. With built-in support for Docker, 
Docker Compose, and a base set of requirements, DjangoStarterTemplate aims to simplify project initialization 
and ensure best practices are followed from the outset.

------------
### Technology stack
- Docker
- Docker Compose
- Django
- PostgreSQL
- Celery
- Redis
- PgAdmin
- Flower
- pre-commit
- pytest
- coverage

------------
### Installation

1. Clone the repository:

`git clone https://github.com/shevladyslav/DjangoStarterTemplate.git`

`cd DjangoStarterTemplate`

2. Create local.py file

`cd src/project_src/settings`

`touch local.py`

***Copy all the code from local_template.py and merge it into the newly created local.py.
Replace secret_key with your own***

3. Build and start the Docker containers:

`docker-compose -f docker/docker-compose-develop.yaml up --build`

4. Create a superuser:

`docker-compose -f docker/docker-compose-develop.yaml exec django python manage.py createsuperuser`

5. Install pre-commit hooks:

`pre-commit install`