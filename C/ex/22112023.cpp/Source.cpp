#include<stdio.h>
#include<math.h>

int isPrime(int num);
int sumPrimes(int myNum);


void main() {

    int i;
    /*
        for (i = 2; i <= 10000; i+=2)
                if (isPrime(i) == 1)
                        printf("%d  ", i);
    */
    int result = sumPrimes(1000);
    printf("%d \n\n", result);
}

// check if prime
int isPrime(int num) {

    int isPrimeFlag = 1, i;
    int sqrtNum = (int)sqrt(num);

    // search dividers (with loop)
    for (i = 2; i <= sqrtNum; i++)
        // if we found divider -> NOT PRIME
        if (num % i == 0) {
            isPrimeFlag = 0;
            break;
        }

    // if divider not found -> IS PRIME
    return isPrimeFlag;
}

int sumPrimes(int myNum) {

    int i, sum = 0;
    for (i = 1; i <= myNum; i++)
        if (isPrime(i) == 1)
            sum += i;

    return sum;


}
