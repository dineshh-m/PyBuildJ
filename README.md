# PyBuildJ

<!-- Badges -->
<img src="https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge">  <img src="https://img.shields.io/badge/Version-1.0-informational?style=for-the-badge">  <img src="https://img.shields.io/badge/-Python-green?style=for-the-badge&logo=Python">

A simple and lightweight build automation tool  written in python for simple and straightforward java projects.

## How to run
  - ### Requirements

     -  Python3
     -  GCC or any C compiler(for invoking the python script along with command line arguments)
    
  Compile the pyb.c source file using the appropriate compiler.
  `gcc pyb.c -o pyb` 
    
  - ### Path variables
    - After the compilation, export the project directory to `PATH` variable.   
    - Export the project directory to a new path variable called `PYBUIDJ`.
  
  invoke the `pyb --help` to see various options available.
  
## Subcommands
  - ### init
    - Intialized an empty java project with neccessary folder and files.
      - ***src/***: This directory contains all the java source files.
      - ***project.json***: This file contains the information about the project such as version, author, third-party dependencies and main class etc.
  - ### compile
    - Downloads all the dependencies specified in the `project.json` file.
    - Compiles all the java source files in the `src` directory.
    - Generates all the class files in the `build/classes` directory.
  - ### run
    - Run the main class specified in the `project.json` file.
    
## Specification file

`project.json` is a configuration or specification file. All of the information on dependencies will go into this file. Since this is a json file.
```json
{
  "name": "MyProject",
  "version": 1.0,
  "author": "Dinesh",
  "main": "com.myproject.Main",
  "dependencies": {
	  "junit:junit:4.13.2":"junit-4.13.2.jar",
  },
  "resources" : ["src/resources/"]
}

```
The `main` key specifies the main class for the java project and it specified in package notation. Here `com.myproject` is the package name
and `Main` is the name of the main class.

Dependencies are specified as `<group-id>:<artifact-id>:<version>`

The `resource` specifies any resource files to be used in the project such as static files, images, etc.

## To implement
  - Implement funtionality for generating jar files.
  - Install any number of third party dependencies with a `install` command(dependencies are automatically updated in the project.json too).
