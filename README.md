# AlkeBFT
### What is AlkeBFT?
AlkeBFT is a framework that allows the implementation of wireless sensor networks that are fault-tolerant to arbitrary faults, also known as Byzantine faults.
### What are the objectives?
The objectives of this project are to enable networks composed of small low-end devices to achieve fault tolerance in distributed communication. In particular, it allows the implementation of trust policies, which are necessary in high-risk environments where errors are not tolerated and where it is likely that a node may behave maliciously.
### What are the features of the project?
The main features of the project must contend with the limitations of the available hardware. In fact, the framework is designed to run on microcontrollers with RAM memory capacity not exceeding 300KB and slightly more Flash memory. Therefore, it will be necessary to implement a lightweight algorithm that is both correct and functionally complete.
### What are the limitations of the project?
The limitations of the project are due to the implementation language. In fact, Alke is implemented in MicroPython and tested on Raspberry Pi Pico W boards. This choice was made solely for ease of implementation. In the embedded environment, many software solutions are dependent on the operating system architecture or, even worse, on the hardware itself if bare-metal programming is required.