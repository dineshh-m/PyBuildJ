import json
import sys
import os
import urllib.request

from pybuildj.exceptions import ProjectConfigNotFound, DownloadError
from termcolor import colored
from shutil import rmtree


class BuildTool:

    repo_url = repo_url = "https://repo1.maven.org/maven2/"
    success_color = "green"
    fail_color = "red"
    note_color = "yellow"
    class_path = "lib"
    build_dir = "build"
    src_dir = "src"


    def __init__(self):
        try:
            with open('project.json', 'r') as project_config:
                self.project_data = json.load(project_config)

            self.main_meth_data = self.project_data.get("main")
            if not self.main_meth_data:
                print("Specify the main class through the main key in the file my com.package.MainClass")
                sys.exit(1)
        except ProjectConfigNotFound:
            print("File project.json not found make sure it is a pybuildj project\n execute init command to initialize a empty project")
            sys.exit(1)
        except Exception:
            print("Error occured while reading file")


       
    def coordinate_to_path(self, coordinate):
        parts = coordinate.split(":")
        return "/".join(parts[0].split(".")) + "/"+parts[1] + "/"+parts[2] + "/"+parts[1]+"-"+parts[2]+".jar"



    def download_dependencies(self):
        try:
            print("Downloading Dependencies")
            dependencies = self.project_data.get("dependencies")

            if not os.path.exists("lib"):
                os.makedirs("lib")

            for coordinate, filename in dependencies.items():
                url = BuildTool.repo_url + self.coordinate_to_path(coordinate)
                print(url)
                print("Downloading", coordinate, end='', flush=True)
                urllib.request.urlretrieve(url, "lib/"+filename)
                sys.stdout.write("\r")
                print(coordinate, colored(": Download complete", self.success_color))
        except Exception as ex:
            print("Error occured while downloading dependencies. Make sure you are connected to internet")
            print(ex) 
            sys.exit(1)



    def compile(self):
       print(colored("Compiling", color=self.note_color))
       dependencies = self.project_data.get("dependencies")
       main_meth_path = "/".join(self.main_meth_data.split("."))
       self.download_dependencies() 
       depends = []
       for coordinate, filename in dependencies.items():
           depends.append(BuildTool.class_path +'/'+ filename)
       local_class_path = ";".join(depends)
       # print(f"javac -d {BuildTool.build_dir}/classes/ -cp {local_class_path}; {BuildTool.src_dir}/{main_meth_path}.java")
       print(f"javac -d {BuildTool.build_dir}/classes/ -cp {local_class_path}; {BuildTool.src_dir}/*.java")
       compile_status = os.system(f"javac -d {BuildTool.build_dir}/classes/ -cp {local_class_path}; {BuildTool.src_dir}/{main_meth_path}.java")
       if compile_status == 0:
           print(colored("Compilation complete", BuildTool.success_color))
       else:
           print(colored("Compilation failed", BuildTool.fail_color))
           sys.exit(1)
        


    def run(self):
        exec_status = os.system(f"java -cp build/classes/;lib/ {self.main_meth_data}")
        

    def build(self):
        pass


    def clean(self):
        ans = input("Are you sure(Y/N)? ")

        if ans == 'y' or ans == 'Y':
            rmtree(BuildTool.build_dir)
        else:
            sys.exit(0)
