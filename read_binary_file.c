#include <stdio.h>
#include <stdlib.h>

int funcName (char * fileName) {
    FILE * inFile;
    unsigned char szBuffer[8]; // need unsigned so bytes are not sign extended
    int i;

    // r for read, b for binary
    inFile = fopen(fileName, "rb");
    // Error handling open file
    if (inFile == NULL) {
        printf("Cannot open file for some reason\n");
        return -1;
        exit(99);
    }

    // fread will return 1 in this case - number of elements read successfully
    while (fread(szBuffer, sizeof(szBuffer), 1, inFile) == 1) {

        for (i = 0; i < 8; i++) {
            printf("%x ", szBuffer[i]);
        }
        printf("\n");

    }

    // Close file
    fclose(inFile);
    return 0;
}

int main(int argc, char **argv) {
    // Usage output
    if (argc < 2) {
        printf("Usage: ./prog_name File_1\n");
        exit(99);
    }

    funcName(argv[1]);

    return 0;
}
