# Generates headings (eg: ---- Heading ----) 1 usage
from tkinter.ttk import tclobjs_to_py


def statement_generator (statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
 Instructions go here.
- instructions 1
- instructions 2
- etc
    ''')


def num_check(question):
    """Ask user for an integer between 1 and 200."""

    error = "Please enter a number that is between 1 and 200 inclusive\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
             # ask the user for a number
             response = int(question)

             # check that the number is more than zero

             if 1 <= response <= 200:
                 return response
             else:
                 print(error)

        except ValueError:
            print(error)


# Main routine goes here

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions "
                           "or any key to continue ")

if want_instructions == "":
    instructions()

while True:

    comment = ""

    # Ask user for number to be factorised
    to_factor = num_check("\nEnter an integer (or xxx to quiet):")

    if to_factor =="xxx":
        break

    # get factors for integers that are 2 or more
    elif to_factor != 1:
        all_factors = factor(to_factor)

    # Set up comments for unity
    else:
        all_factors = ""
        comment = "One is UNITY! It only has one factor. Itself :)"

    # comment for squares / primes

    # Prime numbers have only two factors
    if len(all_factors) == 2:
        comment = f"{to_factor} is a prime number"

    # check if the list has an odd number of factors
    elif len(all_factors) % 2 == 1:
        comment = f"{to_factor} is a perfect square"

    # Set up headings
    if to_factor > 1:
        heading = f"Factors of {to_factor}"
    else:
        heading = "One is special..."

    # output factors and comments
    print()
    statement_generator(heading, "*")
    print(all_factors)
    print(comment)

print("Thank you for using the factors calculator")