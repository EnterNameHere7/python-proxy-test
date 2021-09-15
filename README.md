# python-proxy-test

### The thinking behind this
When working with static data (data that doesn't change or get updated frequently) its better to place a caching layer infront of the database, the idea is to rather hit a caching layer than hit the database directly, obviosly each use case is different and would need to be carefully considered.

The idea behind this is to lessen the load on the database and try to controll the hits to the database.

This is just an example to do the caching yourself.

#### NOTE: rename .env.example to .env before running

## Endpoints

##### Load data into mysql - ALWAYS first on new setup
```
/civilizations
```

##### query data
```
/civilization?civ_id=1
```

```
/civilization?name=Slavs
```


## Building and running container environments
```bash
docker-compose up --build
```

When you want to do a full teardown : 
```
docker-compose --remove-orphans
```

Tired of having all these images? :
```
docker system prune -a
