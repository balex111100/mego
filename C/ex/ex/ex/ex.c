
#include<stdio.h>

void main() {

    // declare vars
    int i, number;

    for (i = 100; i <= 200; i++) {
        if (i % 2 != 0)
            continue;

        printf("%d ", i);
}