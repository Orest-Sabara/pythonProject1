# 𝑦 = 2𝑥^2 − 5𝑥 − 8, dla 𝑥 ∈ [−4, 4]
# import math
# print("y = 2x^2 − 5x − 8, x jest od -4 do 4 z krokiem 0.5")
# print("{:<10} {:>10}".format("x", "y"))
# x = -4
# while x <= 4:
#     y = 2 * pow(x, 2) - 5 * x - 8
#     print("{:<10} {:>10}".format(x, y))
#     x += 0.5

solutions_string = ""
current_number = -4
while current_number <= 4:
    solutions_string += f"f({current_number}) = {2 * current_number ** 2-5 * current_number -8}\n"
    current_number += 0.5
print(solutions_string)