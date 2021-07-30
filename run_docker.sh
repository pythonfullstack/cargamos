echo killing old docker processes
docker-compose rm -fs

echo building docker containers
docker-compose build

echo running docker containers
docker-compose up