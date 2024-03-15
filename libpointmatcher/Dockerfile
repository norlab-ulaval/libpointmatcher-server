# docker build . -t libpointmatcher
FROM ubuntu:22.04
SHELL ["/bin/bash", "-c"]

RUN apt update \
  && apt upgrade -y \
  && apt install -y \
      build-essential \
      clang cmake \
      g++ gcc gdb git \
  	  fuse \
      iputils-ping \
      libomp-dev libboost-all-dev libeigen3-dev libyaml-cpp-dev \
      ninja-build \
      python3-pip \
  && apt clean

# Virtual environment
RUN pip install virtualenv

RUN virtualenv venv \
    && source venv/bin/activate \
    && pip install \
    	build \
    	numpy \
    	pytest \
    	wheel \
        websockets
    
# Modify the PATH environment variable to include the virtual environment's bin directory.
ENV PATH="/venv/bin:$PATH"

# install libraries
RUN mkdir libraries

# pybind11
RUN cd /libraries \
	&& git clone https://github.com/pybind/pybind11.git \
	&& cd pybind11 \
	&& git checkout v2.5.0 \
	&& mkdir build && cd build \
	&& cmake .. \
	&& make -j 12 \
	&& make install

# libnabo
RUN cd /libraries \
	&& git clone https://github.com/ethz-asl/libnabo.git \
	&& cd libnabo/ \
	&& mkdir build && cd build \
	&& cmake -DCMAKE_BUILD_TYPE=Release .. \
	&& make -j 12 \
	&& make install

# libpointmatcher
RUN cd /libraries \
	&& git clone -b agagnon/project/server-eval https://github.com/norlab-ulaval/libpointmatcher.git \
	&& cd libpointmatcher/ \
	&& mkdir build && cd build/ \
	&& cmake -DCMAKE_BUILD_TYPE=Release -DPOINTMATCHER_BUILD_EXAMPLES=OFF \
		 -DPOINTMATCHER_BUILD_EVALUATIONS=OFF \
		 -DBUILD_PYTHON_MODULE=ON \
		 -DUSE_OPEN_MP=FALSE \
		 -D EVALUATION=TRUE .. \
	&& make -j 4 \
	&& make install
	
# libpointmatcher python bindings
RUN cd /libraries/libpointmatcher/python/ \
	&& python -m build --wheel --no-isolation --outdir ./dist \
	&& pip install ./dist/pypointmatcher-*.whl \
	&& python -c "from pypointmatcher import *" \
	&& rm -rf ./dist