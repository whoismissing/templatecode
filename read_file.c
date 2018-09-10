/*********************************
    Program_name.c
Purpose:
    Program to...
Results:
    The program demonstrates...
Notes:

Returns:
    Returns the number of...
*********************************/
#include <stdio.h>
#include <stdlib.h>

/********** funcName *************
    int funcName (char * fileName)
Purpose:
    Function to print contents of a given file.
Parameters:
    I    char * fileName    Given filename that will be opened
Returns:
    Returns integer exit value on success or fail
Notes:
**********************************/
int funcName (char * fileName) {
    FILE * inFile;
    char szBuffer[101];

    inFile = fopen(fileName, "r");
    // Error handling open file
    if (inFile == NULL) {
        printf("Cannot open file for some reason\n");
        return -1;
        exit(99);
    }

    while (fgets(szBuffer, 101, inFile) != NULL) {
        printf("%s\n", szBuffer);
    }
    
    // Close file
    fclose(inFile);
    return 0;
}

int main (int argc, char ** argv) {

    // Usage output
    if (argc < 2) {
        printf("Usage: ./prog_name File_1 File_2 ... File_n\n");
        exit(99);
    }
    
    return 0;
}
