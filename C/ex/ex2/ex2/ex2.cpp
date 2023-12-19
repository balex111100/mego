/*
#include<stdio.h>



void main() {

    // declare vars
    int number, currentDigit, max = 0, min = 9;


    // input number
    printf("Enter a number:");
    scanf_s("%d", &number);


    // loop to check each digit
    while (number != 0) {

        // compare digit with max and min till now
        currentDigit = number % 10;

        // insert if needed
        if (currentDigit > max)
            max = currentDigit;

        if (currentDigit < min)
            min = currentDigit;

        // remove most right digit
        number = number / 10; // number/=10;
    }

    // display max-min
    printf("difference = %d \n\n", max - min);
*/
#include<stdio.h>
#define ROWS 3
#define COLS 3

void main() {
    int arr2[ROWS][COLS] = { {1,2,3},{4,5,6},{7,8,9} };
    int i, j;

    for (i = 0; i < ROWS; i++) {
        for (j = 0; j < COLS; j++) {
            printf("%d ", arr2[i][j]);
        }
        printf("\n");
    }
}
