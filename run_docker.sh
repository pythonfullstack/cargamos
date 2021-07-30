


echo killing old docker processes
docker-compose rm -fs

echo building docker containers
docker-compose build

echo migrating
docker-compose exec web sh
export FLASK_CONFIGURATION=production
flask db init
flask db migrate
flask db upgrade
exit

echo running docker containers
docker-compose up