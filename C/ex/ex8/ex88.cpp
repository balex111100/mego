#include<stdio.h>

void main() {

    // declare vars
    int a, b, c;

    // input triangle
    printf("Enter 3 lengths of triangle: ");
    scanf_s("%d %d %d", &a, &b, &c);

    // check if legal -> display message
    if (a + b > c && c + b > a && a + c > b)
        printf("Triangle legal \n\n");
    else
        printf("Triangle illegal. \n\n");
}