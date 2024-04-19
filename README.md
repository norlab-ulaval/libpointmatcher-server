# libpointmatcher-server

Web app to test and rank the result of the configuration used for [libpointmatcher](https://github.com/norlab-ulaval/libpointmatcher)

Note:
- Javascript for the frontend
- Python for the backend
- Mongo for the database for users information



# Quick start

It is recommended to use [docker](https://www.docker.com/), you can use the [documentation](https://docs.docker.com/desktop/) to install it.

To start use the command : 
```
docker compose up -d
```

To stop use the command :
```
docker compose down
```
Or the command to stop and remove the containers defined in the 'docker-compose.yml', be cautious when using this command, as it will permanently delete the local images, and you won't be able to bring the containers back up without rebuilding the images.:
```
docker compose down --rmi local
```

## General readme
[frontend's readme](web/README.md)

[api's readme](api/README.md)

[doc's readme](api/README.md)

[libpointmatcher's readme](libpointmatcher/README.md)

## Database readme
[data's readme](data/README.md)

[database's readme](db/README.md)

# Licence

The project is under the [MIT license](LICENSE)