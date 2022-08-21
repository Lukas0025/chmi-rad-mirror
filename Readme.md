# Toto je CHMI-RAD zrcadlo
Program vytváří kopie radarových snímků z CHMI. K těmto snímkům lze přistupovat přes jednoduché API.

## Build pro docker

```sh
docker build . -t chmirad
```

## Spuštení Docker

```sh
docker run -p 5000:5000 chmirad
```

## Spuštení bez docker

```sh
flask --app web run -h 0.0.0.0 &
python deamon.py
```

## Spuštení bez docker a bez web API

```sh
python deamon.py
```