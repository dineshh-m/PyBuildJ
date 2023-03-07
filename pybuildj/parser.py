"""Parser for the PyBuildJ System

This module contains the code implementing the parser for the
Command Line Interface
"""

import argparse as argp
from pybuildj import initialize, functions, build

build_sys = build.BuildTool()

global_parser = argp.ArgumentParser(prog='pybuildj',
                                    description='A Simple and Lightweight build automation tool for the Java language')

#defining the subparser(subcommands)
sub_parser = global_parser.add_subparsers(title='Commands', help='All commands')

init_parser = sub_parser.add_parser("init",
                                    help="Initialize the empty project")
init_parser.set_defaults(func=initialize.init_project)

compile_parser = sub_parser.add_parser("compile",
                                        help='Compiles the java source files in the default or specified source directory')
compile_parser.set_defaults(func=build_sys.compile)

build_parser = sub_parser.add_parser("build",
                                      help="Builds the project by downloading the dependencies and setting up classpaths into the build directory")
build_parser.add_argument('-o', '--output' )
build_parser.set_defaults(func=build_sys.build)

run_parser = sub_parser.add_parser("run",
                                    help="Run the project")
run_parser.set_defaults(func=build_sys.run)

clean_parser = sub_parser.add_parser("clean",
                                     help="Clean the build directory")
clean_parser.set_defaults(func=build_sys.clean)

args = global_parser.parse_args()
args.func() #Invoking the corresponding subcommand routine
