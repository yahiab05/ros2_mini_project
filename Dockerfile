FROM ros:jazzy-ros-base

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /ros2_ws

COPY src/mini_project/package.xml src/mini_project/package.xml

RUN apt-get update && rosdep update \
    && rosdep install --from-paths src --ignore-src --rosdistro jazzy -r -y

COPY src/ src/


SHELL ["/bin/bash", "-c"]

RUN source /opt/ros/jazzy/setup.bash && \ 
    colcon build --symlink-install --packages-select mini_project

COPY entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

CMD = ["ros2", "launch", "mini_project", "project.launch.py"]