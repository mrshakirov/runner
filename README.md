# Requirements
- docker
- docker-compose

# First start
- cd <PROJECT_ROOT>
- docker-compose up

# Settings
You can add your own directory into container. You just need to add the absolute
path of your directory into docker-compose.yml (as volume) and specify this path
as argument for script start command. Example:
- python main.py --root=/dir
- python main.py --root=/dir2
- python main.py --root=/dir3
