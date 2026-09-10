# Generates headings (eg: ---- Heading ----) 1 usage
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

# Ask user for number to factor (between 1 and 200)
to_factor = num_check("To factor: ")
print("You chose ro factor", to_factor)

