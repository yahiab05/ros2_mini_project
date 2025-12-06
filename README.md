🚗🔋Battery Temperature Monitor (ROS2 + Docker)

A small ROS2 project simulating a battery temperature system in an electric racing car.
The publisher simulates battery temperature changes, and the subscriber monitors thresholds and reacts (warning, critical cooling, etc).

The whole project can be run inside Docker, so you don't need ROS2 installed on your system.


🧰 Prerequisites

Make sure you have installed:

* Git

* Docker (Docker Engine)

* bash

* (Optional) VS Code or your IDE of choice


🐳 Running the Project With Docker

* step1: Building the project
    -command: `docker build https://github.com/yahiab05/ros2_mini_project.git#main -t yahia_project`

* step2: Running docker image
    -command: `docker run yahia_project`

* the project will automatically:
    -install dependencies
    -source ros2
    -Build workspace
    -Run launch file

📜 What You Should See (Expected Output)

Inside the running container, you will see logs such as:
    `[listener-1] [INFO] [1765060583.304757767] [battery_temp_subscriber]: ✔: The temperature is OK at 54.0°C
    [listener-1] [INFO] [1765060583.804076974] [battery_temp_subscriber]: ⚠: The temperature is high but not critical at 55.0°C`


