#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {

	char command[1024] = "python3 /mnt/d/programming/python/build_tool/PyBuildJ/main.py ";
	
	for(int i = 1; i < argc; i++) {
		strcat(command, argv[i]);
		strcat(command, " ");
	}

	system(command);

	return 0;
}
