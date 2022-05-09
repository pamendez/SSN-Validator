# SSN Validator - User Manual
This manual is intended to establish how the application is installed and used by users. 

## Table of contents
1. [Requirements](#requirements)
2. [Installation and execution](#installation-and-execution)
3. [Usage](#usage)

## Requirements
In order to be able to install and run the application, make sure you have installed in your machine the following programs:

* Git 2.36.0 or greater, available [here](https://git-scm.com/downloads).
* Python 3.10.1 or greater, available [here](https://www.python.org/downloads/).

## Installation and execution
Beforehand, make sure to satisfy the requirements of this project. To install the application, follow these steps:

1. Open the terminal or console present in your operating system, such as Command Prompt (CMD) or Powershell for Windows, Konsole or Terminal on Linux distros or Terminal on MacOS.

2. Next, type the following command and, optionally, insert the path of the repository with the application:
``` 
git clone https://github.com/pamendez/SSN-Validator <path-to-repo>
```

3. After cloning the application, type the following command with the path of the repository
```
cd <path-to-repo>
```

4. Next, to execute the application, use the following command:
```
python validate.py
``` 

5. If everything worked, the message ```'Enter a social security number'``` will appear on the terminal on your screen, and with that you successfully installed this application.

## Usage
Once in the application, you can insert the social security number after the previous message is shown. Depending on your input, the social security number can be valid or invalid:

* If the social security number entered is valid, a message will be shown indicating the validity.
* Otherwise, if the social security number is not valid, a message will be shown indicating the invalidity, alongside the reason why it was invalid.