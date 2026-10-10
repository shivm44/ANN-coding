# This project is the implenentation of OR logic gate function using perceptron algorithm.

# taking input from the user. 
x_input = []
for i in range (2):
    usr_input = int(input("Enter the number: "))
    x_input.append(usr_input)
w_weights = [0.5,0.5]
bias = 0.0
threshold = 0.5
print(x_input)
# print(w_weights)

def step(weighted_sum):
    if weighted_sum > threshold:
        return 1
    else:
        return 0

def perceptron():
    weighted_sum = 0
    for x,w in zip(x_input,w_weights):
        weighted_sum += x*w
        print(weighted_sum)

    weighted_sum += bias
    return step(weighted_sum)

output = perceptron()

print("output: " +str(output))
