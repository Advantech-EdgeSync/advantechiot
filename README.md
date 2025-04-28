# SUSI APIs (Secure, Unified, and Smart Interface)
## Introduction
As a software developer or system integrator, writing applications requiring direct hardware access can be challenging, especially with modern operating systems. Studying extensive specifications to write appropriate drivers is a complex and time-consuming task.

To simplify this process, Advantech has developed SUSI (Secure and Unified Smart Interface), a suite of Software APIs (Application Programming Interfaces) that bridges the gap between hardware and application implementation efficiency. SUSI provides not only the necessary underlying drivers but also user-friendly, intelligent, and integrated interfaces that accelerate development, enhance security, and offer added value for Advantech platforms.

This allows customers to more easily program and configure features while maintaining full control over their applications. By acting as a catalyst between developers and solutions, SUSI makes Advantech embedded platforms simpler and easier to adopt, improving the overall operation of customer applications.

## Architecture

![image](photo.png)

## Service Highlights

| System Protection | Device Monitoring | I/O Control | Application Extension |
| ----------------- | ----------------- | ----------- | ----------- |
| *Data security <br>*Watch Dog Timer <br>*Thermal protection<br> *System throttling              | *Smart fan <br>*Hardware monitoring <br>*System information <br>*AI information             | *GPIO <br>*SMBus/I2C <br>*Backlight on/off <br>*Brightness <br>*CANBus | *PoE <br>*G-sensor <br>*RAM <br> *Battery <br>*Virtual COM |

## Drivers and APIs

### SUSI 4.0
SUSI 4.0 driver supports include not only newer SUSI 4.0 APIs, but also the APIs of SUSI 3.02 and iManager 2.0. Therefore, the old customers, who bought SUSI 3.02 or iManager 2.0 before, can install SUSI 4.0 driver with no effort. Customers will enjoy better performance which is SUSI 4.0 driver carries out.

### SUSI Device
SUSI Device is auxiliary library that depends on SUSI library, making customers access some SMBus devices, such as G-Sensor, RAM, Battery and so on, more efficiently.

### SUSI CANBus
SUSI CANBus API provides customers to manipulate Advantech Embedded Controller functions, including send, receive and set configuration etc.

### SUSI IoT
SUSI IoT is an IoT-oriented library aiming at simplifying the complicated IoT integration developing works. SUSI IoT provides an simple unified interface sets to our users to access various of hardware or software modules.

### SUSI AI
SUSI AI is used to get and set information of AI accelerated devices, such as NVIDIA x86 GPU card, NVIDIA ARM platform, and Intel x86 CPU / GPU; meanwhile, information of docker image and container could be retrieved as well.

# SUSI Iot with Python

## Install SUSI IOT
https://github.com/ADVANTECH-Corp/SUSI

* ReleasePackage
* Choice ARM or x86 Architecture
* Choice Board Type
* Un-Zip and Run Installation

## On x86 Ubuntu
```bash
sudo docker run \
    -it \
    --name kengweisusiiotdemo \
    --privileged \
    --mount type=bind,source=/opt/Advantech/susi/service/,target=/opt/Advantech/susi/service/,readonly \
    --mount type=bind,source=/etc/Advantech/susi/service/,target=/etc/Advantech/susi/service/,readonly \
    --mount type=bind,source=/usr/lib/x86_64-linux-gnu/libjansson.so.4,target=/usr/lib/x86_64-linux-gnu/libjansson.so.4,readonly \
    --mount type=bind,source=/usr/lib/libjansson.so.4,target=/usr/lib/libjansson.so.4,readonly \
    --mount type=bind,source=/usr/lib/libjansson.so,target=/usr/lib/libjansson.so,readonly \
    --mount type=bind,source=/usr/lib/libSusiIoT.so,target=/usr/lib/libSusiIoT.so,readonly \
    --mount type=bind,source=/usr/lib/libSUSIDevice.so.1,target=/usr/lib/libSUSIDevice.so.1,readonly \
    --mount type=bind,source=/usr/lib/libSUSIDevice.so,target=/usr/lib/libSUSIDevice.so,readonly \
    --mount type=bind,source=/usr/lib/libSUSIAI.so.1,target=/usr/lib/libSUSIAI.so.1,readonly \
    --mount type=bind,source=/usr/lib/libSUSIAI.so,target=/usr/lib/libSUSIAI.so,readonly \
    --mount type=bind,source=/usr/lib/libSUSI-4.00.so.1,target=/usr/lib/libSUSI-4.00.so.1,readonly \
    --mount type=bind,source=/usr/lib/libSUSI-4.00.so,target=/usr/lib/libSUSI-4.00.so,readonly \
    --mount type=bind,source=/usr/lib/libSUSI-3.02.so.1,target=/usr/lib/libSUSI-3.02.so.1,readonly \
    --mount type=bind,source=/usr/lib/libSUSI-3.02.so,target=/usr/lib/libSUSI-3.02.so,readonly \
    --mount type=bind,source=/usr/lib/libEApi.so.1,target=/usr/lib/libEApi.so.1,readonly \
    --mount type=bind,source=/usr/lib/libEApi.so,target=/usr/lib/libEApi.so,readonly \
    --mount type=bind,source=/usr/lib/Advantech,target=/usr/lib/Advantech,readonly \
    -v /home/:/volume \
    susiiot_x86:1 \
    bash
```

## On ARM Ubuntu
```bash
sudo docker run \
        -it \
        --name susiiot_demo \
        --privileged \
        --mount type=bind,source=/lib/libSUSI-4.00.so,target=/lib/libSUSI-4.00.so,readonly \
        --mount type=bind,source=/lib/libSUSI-4.00.so.1,target=/lib/libSUSI-4.00.so.1,readonly \
        --mount type=bind,source=/lib/libSUSI-4.00.so.1.0.0,target=/lib/libSUSI-4.00.so.1.0.0,readonly \
        --mount type=bind,source=/lib/libjansson.a,target=/lib/libjansson.a,readonly \
        --mount type=bind,source=/lib/libjansson.so,target=/lib/libjansson.so,readonly \
        --mount type=bind,source=/lib/libjansson.so.4,target=/lib/libjansson.so.4,readonly \
        --mount type=bind,source=/lib/libjansson.so.4.11.0,target=/lib/libjansson.so.4.11.0,readonly \
        --mount type=bind,source=/lib/libSusiIoT.so,target=/lib/libSusiIoT.so,readonly \
        --mount type=bind,source=/lib/libSusiIoT.so.1.0.0,target=/lib/libSusiIoT.so.1.0.0,readonly \
        --mount type=bind,source=/usr/lib/Advantech/,target=/usr/lib/Advantech/,readonly \
        -v /home/:/volume \
        ubuntu:20.04 \
        /bin/bash
```

## PIP Install advantechiot Package
```sh
sudo pip3 install git+https://github.com/EdgeSync-Adv/advantechiot.git
```
## Get Demo Code
```sh
git clone https://github.com/EdgeSync-Adv/advantechiot.git
cd advantechiot/tests
```
### In the Container
```sh
python3 -m unittest -v test_advantechiot
```
### In the Host
```sh
sudo python3 -m unittest -v test_advantechiot
```