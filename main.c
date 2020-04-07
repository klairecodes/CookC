#include <stdio.h>

void displayBoard(char * pgameBoard)
int main() {
    printf("Welcome to CookC!\n");

    char gameBoard[][3] = {
            {'`', '`', '`'},
            {'`', '`', '`'},
            {'`', '`', '`'}
    };
    char * pgameBoard = &gameBoard;

    displayBoard(*&pgameBoard);

    return 0;
}

void displayBoard(char board[][3]) {
    int i, j;
    for (i=0; i < 3; i++) {
        for (j=0; j < 3; j++) {
            printf(board[i][j]);
        }

    }
}

//int * getArray() {
//    ;
//}