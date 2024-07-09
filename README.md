# Note Management

## For Setup this project locally you need docker in your system
   - For Ubuntu 
     https://gist.github.com/vikash8507/0b2e1f5532cb54d561ddb97f62dd6f15
   - For Windows
     https://docs.docker.com/desktop/install/windows-install/
   - For Mac
     https://docs.docker.com/desktop/install/mac-install/
   - More about docker - https://www.docker.com/

### Technologies are using
   1. Python for BE
   2. Django for Web Framework
   3. HTML, CSS (Bootstrap 4) for Frontend
   4. Postgresql for Database


## Setup Project Locally

1. Clone Repository
   
   git clone https://github.com/vikash8507/notemanagement.git

2. Go in to this directory (Cloned repository's directory)
3. Copy .envs.example and rename copied to .envs
4. Update Environment Variables according to you
   - Do not change DATABASE variable. If you changed it then need to update entry point according to this
5. Run command chmod +x ./entrypoint.sh to give permission for entrypoint.sh file
6. Build Application with Docker Locally
   - docker-compose build
7. Start Containers Locally
   - docker-compose up
        or
   - docker-compose up -d (in detach mode)
   - Now server is started
     - You can visit http://localhost:8000 or http://127.0.0.1:8000
8. Execute below command if you update any models or add any model run below command
   - docker-compose run --rm django python manage.py makemigrations
9. Execute below command if any new migration file generates
   - docker-compose run --rm django python manage.py migrate
10. Run below command to create super user
    - docker-compose run --rm django python manage.py createsuperuser
