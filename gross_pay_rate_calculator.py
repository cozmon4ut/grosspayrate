# Set initial values, this is for error handling
hours = 0.0
payRate = 0.0
prompt = True

# Set variables for the hours and pay rate, set type to floating point to avoid type error. Use while loop for error handling
while prompt: 
    try:
        hours = float(input("Enter the number of hours the employee worked. "))
        payRate = float(input("\nEnter the employee's hourly pay rate. "))
        prompt = False
    # Make sure the inputs are actually numbers
    except ValueError: 
        print("\nInvalid input, please input a number.")

# Set gross pay value
grossPay = (hours * payRate)

# Display gross pay value, limit to two decimal places for brevity
print(f"\nThe employee's gross pay is: ${grossPay:.2f}")

