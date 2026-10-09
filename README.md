# Cobot Vision Robot Pipeline
This project aims to replicate a cobot in a production line detecting a certain item from its color
(color red in this project by default) and sends a command to an imitated robot server to move towards that item.

the code transforms pixels into real coordinates by creating a homography. and sends the command to server.

also pixel_text.py can be used for detect pixel points of a certain video in order to use in this program.




## System Architecture

* `data/`  keeps the static data to be processed. 

* `src/vision.py` handles the video stream. Applies HSV filtering and morphological noise reduction to get the best results. also calculates the moments of the objects that it filtered and draws a border around it and shows the center and coordinates of the object. 
*  `src/transform.py`  makes a homography transformation to turn 2D pixel information into physical (X,Y) millimeter coordinate for robot base.
*  `src/robot_interface.py`  connects to our mock robot server and sends the data.

* `tests/transform_test` tests how accurate is the data processes.


## How to Run

* **first after you navigate to project folder you need to run robot_server_test.py to turn the server on:
```bash
python3 robot_server_test.py
```

after run the main.py:

```bash
python3 main.py
```

## How to deploy
the pipeline fully containerized to be able to deploy it on industrial edge pc's.
to build the project:
```bash
docker build -t edge-cobot-vision .

```
after that run the server:
```bash
python3 robot_server_test.py
```
to do the tests:
```bash
docker run --rm edge-cobot-vision-pipeline python -m unittest tests.transform_test

```
to run:
```bash
docker run --rm edge-cobot-vision-pipeline_copy
```
for running locally without docker it is needed to uncomment 
`cv.imShow()` and `cv.waitKey()` lines because docker does not have an GUI they are commented. also at `robot_interface.py` the host should be `127.0.0.1` instead of `host.docker.internal` and on `robot_server_test.py` the `HOST = '0.0.0.0'` should be `127.0.0.1` too.

#### the project's code is yet to be commented... 
