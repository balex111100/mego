


#include <stdio.h>

int main() {
    int num;
    printf("Enter a two-digit number: ");
    scanf("%d", &num);
    int tens = num / 10;
    int ones = num % 10;
    int diff = tens - ones;
    printf("The difference between %d and %d is %d.\n", tens, ones, diff);
    return 0;
}