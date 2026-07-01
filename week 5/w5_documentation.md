1.1 Define the problem statement

Answer:
Develop a Python program that automatically calculates a customer’s café bill based on the quantities of coffee, tea, and sandwiches ordered, then prints a receipt.

⸻

1.2 What are the inputs?

Answer:

* Customer name
* Coffee quantity
* Tea quantity
* Sandwich quantity

⸻

1.3 What are the outputs?

Answer:

* Customer name
* Quantity of each item
* Total bill (RM)

⸻

1.4 Typical process flow

Answer:

1. Enter customer name.
2. Enter quantity of coffee.
3. Enter quantity of tea.
4. Enter quantity of sandwiches.
5. Calculate the total price.
6. Print the receipt.

⸻

1.5 Constraints

Answer:

* Quantities must be zero or positive integers.
* Prices are fixed:
    * Coffee = RM8.50
    * Tea = RM6.00
    * Sandwich = RM12.00

⸻

2. Decompose the problem into smaller tasks

Answer:

1. Get customer information.
2. Read item quantities.
3. Calculate the total price.
4. Display the receipt.

⸻

3. Pseudocode

START
Set coffee price = 8.50
Set tea price = 6.00
Set sandwich price = 12.00
Input customer name
Input coffee quantity
Input tea quantity
Input sandwich quantity
total = (coffee quantity × coffee price)
      + (tea quantity × tea price)
      + (sandwich quantity × sandwich price)
Display receipt
Display customer name
Display coffee quantity
Display tea quantity
Display sandwich quantity
Display total
END`