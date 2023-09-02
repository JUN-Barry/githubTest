def calculate_sum(a, b, n):
    total_sum = 0
    year = 1

    while year <= n:
        total_sum += a
        a += a * b
        year += 1

    return total_sum

# Example values
oneraw = 1
initial_value = 17259000 * oneraw
ten_year_value = initial_value * (1 + 0.0516)
increase_rate = 0.012
years = 10

result = calculate_sum(initial_value, increase_rate, years)
print("First storage cost is: " + str(initial_value))
print("10th year's storage cost is: " + str(ten_year_value))
print(f"The sum of {years} years is: {result}")

# In this example, the calculate_sum function takes three arguments: 
# the initial value a, the year increase rate b, and the number of years n. 
# The while loop iterates from year 1 to n and accumulates the value of a in total_sum for each year. 
# The value of a is then updated based on the increase rate b. 
# Finally, the function returns the total sum over the given number of years.






