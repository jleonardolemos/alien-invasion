## Alien Invaders From Python Crash Course

![Alient Invasion game image](http://l30.space/storage/general/alien_invaders.png)

## What is this game

I was learning python from the book ["Python Crash Course"](https://www.amazon.com.br/Python-Crash-Course-Eric-Matthes/dp/1593279280/) and i end with this little game when following the book chapters. After reading the book i decided to publish in my github in order to evolve the game.

## RoadMap

- [x] Add a requirements.txt
- [x] Add a Pub/Sub feature in order to decouple the classes
- [x] Add interactive menus
- [ ] Add some static analysis
- [x] Add tests
- [ ] Add a CI pipeline
- [ ] Add Brazilian Metal Songs
- [ ] Add ability to increase the ship
- [x] Add ability to increase the ship weapon
- [ ] Add another aliens more stronger and faster
- [ ] Add ability to earn lives
- [ ] Publish on Ubuntu Software
- [ ] Publish on Steam(we can dream!!!)
- [ ] Create Engine Package, EventMap Location!

## Inpirations

There are two main inspirations for this game that i would like to turn this game in:

1. [Chicken invaders](https://www.youtube.com/watch?v=jM0v4VemWu8)

2. [Strike Gunner](https://www.youtube.com/watch?v=Ay6132F5pcw)

## Running the game

```sh
# Install dependencies
pip install -r requirements.txt

#Run the game
python alien_invasion.py
```

## Versions

The game was tested with Python 3.8.10 and pip 20.0.2

**OBS: you must install pygame with pip before running**

## Running tests

```sh
python -m unittest
```
## Building with Pyinstaller

```sh
pyinstaller main.py --add-data images:images
```