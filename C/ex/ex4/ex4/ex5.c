


	/*

	int a;
	a = 10;
	a = a + 5;//15
	//scanf_s("%d", &a);
	//printf("after scanf a= %d\n", a);

	a += 5;
	printf("%d\n", a);

	char f;
	f = '3';
	printf("%c \n", f);


	float g;
	g = 5.5;
	printf("%.0f \n", g);



	int cc;
	cc = 20;
	int k;
	k = cc + a;
	printf("%d", k);

	*/
	/*
	int length, width, s, p;
	printf("Enter the length and width of the rectangle \n ");
	scanf_s("%d %d", &length,&width );
	p = (length + width) * 2;
	s = length * width;
	printf("%d\n", s);
	printf("%d\n", p);
	*/

	/*
	int prise, amount, discount, sum;
	printf("enter the prise ");
	scanf_s("%d", &prise);
	printf("enter the amount yo wont ");
	scanf_s("%d", &amount);
	printf("What is the discount percentage? ");
	scanf_s("%d", &discount);
	sum = (prise * amount) * (100 - discount) / 100;
	printf("%d\n", sum);



	float radius, s, p, pai;

	printf("enter the radius cercel ");
	scanf_s("%f", &radius);
	pai = 3.14;
		s = (radius * 2) * pai;
		p = (radius * radius) * pai;
		printf("The circumference of the circle is: %.2f\n" ,s);
		printf("The area of the circle is : %.2f\n", p);
	*/
	/*
	int hour, minutes, time;
	printf("wat is the hour? ");
	scanf_s("%d", &hour);
	printf("\nend how meny minutes? ");
	scanf_s("%d", &minutes);

	time = (hour * 60) + minutes;
	printf("\nhoures and minutes: % d \n\n",time);
	*/
	/*
	float score1, score2, score3, average;
	printf("Enter your grades: ");
	scanf_s("%f", &score1);
	scanf_s("%f", &score2);
	scanf_s("%f", &score3);

	average = (score1 + score2 + score3) / 3;
	printf("\n%.2f", average);
	if (average > 90)
		printf("\nvery good!!!");
	if (average < 90 && average>55)
		printf("\nnu nu");


	if (average < 55)
		printf("\nNeed to improve grades");
	*/

	/*
	float gmh, food, education, transportation, Total_monthly_expenses, annual_expenses;

	printf("How much do you spend on food per month?");
	scanf_s("%f", &food);
	printf("How much do you spend on gmh per month?");
	scanf_s("%f", &gmh);
	printf("How much do you spend on Education per month?");
	scanf_s("%f", &education);
	printf("How much do you spend on transportation per month?");
	scanf_s("%f", &transportation);
	Total_monthly_expenses = gmh + education + transportation + food;
	annual_expenses = (Total_monthly_expenses * 12);
	printf("annual expenses: %.2f", annual_expenses);
	if ("%.2f" , Total_monthly_expenses * 12 > 100000)
		printf("Expenses need to be streamlined");
	if (Total_monthly_expenses * 12 < 100000)
		printf("\nexcellent");
	*/
	/*
	float unit_price, num_of_units, sum;
		printf("price fo unit? ");
		scanf_s("%f", &unit_price);
		printf("number fo units? ");
		scanf_s("%f", &num_of_units);
		sum = (unit_price * num_of_units) * 1.17;
		printf(" % .2f", sum);
		if (sum > 10000)
			printf("\nYou can pay in 6 installments");
		if(sum < 10000)
			printf("\ncash only");

	*/


	/*
	float Grade1, Grade2, Grade3, average;
	printf("enter your first grade: ");
	scanf_s("%f", &Grade1);
	printf("enter your second grade: ");
	scanf_s("%f", &Grade2);
	printf("enter your third grade: ");
	scanf_s("%f", &Grade3);
	average = (Grade1 + Grade2 + Grade3) / 3;
	printf("average:" "%.2f", average);
	if (average > 65 && Grade1 != 0 && Grade2 != 0 && Grade3 != 0)
		printf("\nYou passed the course!");
	else
		printf("\nYou did not pass the course.");
	*/

	/*
	int avi, yosi, tal;
		printf("\nenter your age: \n");

		scanf_s("\n%d"  "\n%d" "\n%d", &avi, &yosi, &tal);
		if (avi >= 18 && yosi >= 18 && tal >= 18)
			printf("enter the movie");
		else
			printf("Go to a movie that suits your age");
	*/


	/*
	int a, b, c;
		printf("Enter 3 lengths of triangle: \n\n ");
		scanf_s("\n%d" "\n%d" "\n%d", &a, &b, &c);
		if ((a + b) > c && (c + b) > a && (a + c) > b)
			printf("The triangle is legal");
		else
			printf("The triangle is not legal");
	*/

	/*
	int i;
		for (i = 100; i <= 200; i++)
			if (i % 2 == 0)
				printf("%d\n\n", i);
	*/

/*
#include<stdio.h>



void main()
{

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


}
*/



#include<stdio.h>
#include<math.h>

// check dividers -> display to screen
void checkDividers(int a, int b);

void main() {

	int num1, num2;

	checkDividers(10, 20);
	checkDividers(6, 3);

	printf("enter 2 numbers: ");
	scanf_s("%d %d", &num1, &num2);

	checkDividers(num1, num2);



}



// check dividers -> display to screen
void checkDividers(int a, int b) {

	//check dividers
	if (a % b == 0 || b % a == 0)
		printf("dividers \n");
	else
		printf("NOT dividers \n");

}














