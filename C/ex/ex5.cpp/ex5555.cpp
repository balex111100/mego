#include<stdio.h>



void main() {

    /*
    int i;

    for (i = 100; i <= 200; i++) {
        if (i%2==0)
        printf("%d\n", i);

    */
    /*
      float i;
    for (i = 0; i <= 5; i+=0.5)
    {
        printf("%.1f\n", i);
    }
    */
    /*
     int i, sum = 0, number;
      float avr = 0;
      for (i = 0; i <= 7; i++) {
          printf("enter the students score >>> ");
          scanf_s("%d", &number);
          sum += number;
      }
          avr = sum / 7;

              printf("the avreg score is %.2f\n", avr);
              i += 1;
    */
    
   /*
   int i, fact = 1, num;


    printf("enter a number>>> ");
    scanf_s("%d", &num);

    for (i = 1; i <= num; i++) {

        fact = fact * i;

    }



    printf("the factorial %d is %d\n", num, fact);
    
   */
   
    
     // אותן דבר בלולאת while

   // int i, fact=1, num;


    //printf("enter a number>>> ");
    //scanf_s("%d",&num);
    //i = 1;
    //while(i <= num)
    //{
       // fact = fact * i;
      //  i++;


   // printf("the factorial %d is %d\n", num,fact);
    
    
    //int i, num, fact;
    //printf("enter a number>>\n ");
    //scanf_s("%d\n", &num);
    //for (i = 1; i <=num; i++) {
      //  fact = num % i;
        //if 

    // declare vars
    int i, factorial = 1, number;

    // input factorial result
    printf("Enter a number: ");
    scanf_s("%d", &number);

    // loop -> calculate factorial
    for (i = 1; factorial < number; i++)
        factorial *= i;

    // check if our number equals to calculation
    if (factorial == number)
        printf("input is factorial result \n\n");
    else
        printf("input is NOT factorial result \n\n");

    }


    
        


