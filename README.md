# python-proxy-test

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
