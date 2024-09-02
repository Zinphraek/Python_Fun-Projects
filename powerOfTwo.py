import math, random, time

def isPowerOfTwoForLoopVersion(arr):
    result = []
    for n in arr:
        if n == 0 or not math.log2(n) % 1 == 0:
            result.append(0)
        else:
            result.append(1)

    return result

def isPowerOftwoListCompVersion(arr):
    return [ 0 if n == 0 or not math.log2(n) % 1 == 0 else 1 for n in arr ]

# Testing the function.
def generateArray(n, maxRange=1000):
    """Generating a large dataset of random number."""
    return [random.randint(0, maxRange) for n in range(0, n+1, 3)]


originalArray = generateArray(1_000_000)
# print(f"Original array: {originalArray}")

startTime = time.time()
loopVerion = isPowerOfTwoForLoopVersion(originalArray)
endTime = time.time()
print(f"The loop version took: {endTime - startTime:.4f} seconds")
# print(f"Array of power of two for loop version: {loopVerion}")


####################################################################################
startTime = time.time()
listCompVersion = isPowerOftwoListCompVersion(originalArray)
endTime = time.time()
print(f"The list comprehension version took: {endTime - startTime:.4f} seconds")
# print(f"Array of power of two list comprehension version: {listCompVersion}")
