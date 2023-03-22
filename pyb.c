#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, char *argv[]) {
	
	const char* ENV_VAR_NAME = "PYBUILDJ";
	#ifdef _WIN32
		char command[1024] = "python  ";
		char* path = getenv(ENV_VAR_NAME);
		char* exec_command;
		if(path == NULL) {
			printf("Environment Variable %s not set", ENV_VAR_NAME);
			return 1;
		}
		path = strcat(path, "\\main.py");
		exec_command = strcat(command, path);
		exec_command = strcat(exec_command, " ");
		for(int i = 1; i < argc; i++) {
			strcat(exec_command, argv[i]);
			strcat(exec_command, " ");
		}

	#endif
		/* char command[1024] = "python ./main.py"; */
		/* for(int i = 1; i < argc; i++) { */
		/* 	strcat(command, argv[i]); */
		/* 	strcat(command, " "); */
		/* } */


	#ifdef __linux__ 
		char command[1024] = "python3  ";
		char* path = getenv(ENV_VAR_NAME);
		char* exec_command;
		if(path == NULL) {
			printf("Environment Variable %s not set", ENV_VAR_NAME);
			return 1;
		}
		path = strcat(path, "/main.py");
		exec_command = strcat(command, path);
		exec_command = strcat(exec_command, " ");
		for(int i = 1; i < argc; i++) {
			strcat(exec_command, argv[i]);
			strcat(exec_command, " ");
		}
	#endif
	system(exec_command);
	return 0;
}

