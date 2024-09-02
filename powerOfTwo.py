# Exploring different solutions to determine If numbers in an Array are Powers of Two

import math, random, time

# 1. List Comprehension with Bitwise Operation (Fastest)
def isPowerOfTwoListComp(arr):
    return [1 if n > 0 and (n & (n - 1)) == 0 else 0 for n in arr]

# 2. Generator Function Converted to List (Second Fastest)
def isPowerOfTwoGeneratorToList(arr):
    return list(1 if n > 0 and (n & (n - 1)) == 0 else 0 for n in arr)

# 3. List Comprehension with Logarithm-based Modulo Check (Third Fastest)
def isPowerOftwoListCompVersion2(arr):
    return [0 if n == 0 or not math.log2(n) % 1 == 0 else 1 for n in arr]

# 4. For Loop Version with Logarithm-based Check (Fourth Fastest)
def isPowerOfTwoForLoopVersion(arr):
    result = []
    for n in arr:
        if n == 0 or not math.log2(n) % 1 == 0:
            result.append(0)
        else:
            result.append(1)
    return result

# 5. List Comprehension with Logarithm-based Integer Conversion (Fifth Fastest)
def isPowerOfTwoLogIntVersion(arr):
    return [1 if n > 0 and 2**int(math.log2(n)) == n else 0 for n in arr]


# Testing the functions.
def generateArray(n, maxRange=1000):
    """Generating a large dataset of random numbers."""
    return [random.randint(0, maxRange) for _ in range(n)]

# Generating a large array of 1,000,000 random numbers
originalArray = generateArray(1_000_000)

# Dictionary to store function references and their descriptions
functions_to_test = {
    "List Comprehension (Bitwise Operation)": isPowerOfTwoListComp,
    "Generator to List (Bitwise Operation)": isPowerOfTwoGeneratorToList,
    "List Comprehension (Log Int Conversion)": isPowerOfTwoLogIntVersion,
    "List Comprehension (Log Modulo Check)": isPowerOftwoListCompVersion2,
    "For Loop (Log Modulo Check)": isPowerOfTwoForLoopVersion
}

# Testing each function and measuring execution time
for description, func in functions_to_test.items():
    startTime = time.time()
    result = func(originalArray)
    endTime = time.time()
    elapsed_time = endTime - startTime
    print(f"{description} took: {elapsed_time:.4f} seconds")
