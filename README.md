# Note Management

## Setup Project Locally

1. Clone Repository
   
   git clone repository

2. Go in to this directory
3. Copy .envs.example and relname it to .envs
4. Update Environment Variables according to you
5. Run command chmod +x ./entrypoint.sh to give permission for entrypoint.sh file
6. Build Application with Docker Locally
   - docker-compose build
7. Start Containers Locally
   - docker-compose up
        or
   - docker-compose up -d (in detach mode)
   - Now server is started
     - You can visit http://localhost:8000 or http://127.0.0.1:8000
8. Execute below command if you update any models or add any model
   - docker-compose run --rm django python manage.py makemigrations
9. Execute below command if any new migration file generates
   - docker-compose run --rm django python manage.py migrate
10. Run below command to create super user
    - docker-compose run --rm django python manage.py createsuperuser