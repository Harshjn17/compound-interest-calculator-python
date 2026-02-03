# compound-interest-calculator-python

Description :-
This Python program calculates the final balance using compound interest.
It ensures that the user enters valid positive values for:
• Principal amount
• Interest rate
• Time (in years)
If the user enters an invalid value (≤ 0), the program keeps asking until a valid input is provided.

🧠 Concepts Used
• while loop
• Input validation
• Conditional statements (if)
• Type casting (int, float)
• Mathematical formula for compound interest
• pow() function
• Formatted output (f-string)

Compound Interest formula:

A = P × (1 + R/100) ^ T

Where:
P = Principal amount
R = Interest rate
T = Time (in years)
A = Final amount

How the Program Works

1. Asks the user to enter the principal amount
    • Rejects zero or negative values
2. Asks for the interest rate
    • Rejects zero or negative values
3. Asks for the time in years
    • Rejects zero or negative values
4. Calculates the final balance using compound interest
5. Displays the result with 2 decimal places

Sample output:-

Enter the principle amount: 1000
Enter the interset rate: 5
Enter the Time in years: 2
Balance after 2 year/s: $1102.50
