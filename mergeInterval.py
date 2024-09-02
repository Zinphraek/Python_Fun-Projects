
import random, time

def mergeIntervalsWithPointers(intervals):
    """Merge overlapping arrays from an array of arrays. """
    # Sorting intervals based on the starting time
    intervals.sort(key=lambda interval: interval[0])

    # Initialyzing the resulting merged array and pointers
    mergedIntervalsArray = []
    index = 0
    intervalsLength = len(intervals)

    while index < intervalsLength:
        # Starting with the current interval
        currentStart, currentEnd = intervals[index]

        # Merging all overlapping intervals
        nextIndex = index + 1
        while nextIndex < intervalsLength and intervals[nextIndex][0] <= currentEnd:
            currentEnd = max(currentEnd, intervals[nextIndex][1])
            nextIndex += 1

        # Storing the merged interval
        mergedIntervalsArray.append([currentStart, currentEnd])

        # Moving to the next interval
        index = nextIndex

    # Returning the result
    return mergedIntervalsArray


def mergeIntervalsWithListOperations(intervals):

    # Sorting the intervals based on the starting time
    intervals.sort(key=lambda interval: interval[0])

    # Initialyzing the resulting merged array and pointers
    mergedIntervalsArray = []

    for interval in intervals:
        # Add the interval in the merged array if it is empty, or if there is no overlap
        if not mergedIntervalsArray or mergedIntervalsArray[-1][1] < interval[0]:
            mergedIntervalsArray.append(interval)
        else:
            # There is an overlap, merging the intervals
            mergedIntervalsArray[-1][1] = max(mergedIntervalsArray[-1][1], interval[1])

    # Returning the merged array
    return mergedIntervalsArray


# Testing and comparing both versions.

def generateIntervals(n, max_range=1000):
    """Generating a large dataset of random intervals."""
    intervals = []
    for _ in range(n):
        start = random.randint(0, max_range)
        end = random.randint(start, start + random.randint(0, 100))
        intervals.append([start, end])
    return intervals


####################################################################################
# Generating a dataset with 1,000,000 intervals
intervals = generateIntervals(1_000_000)
#print(f"Generated list: {intervals}")

# Testing the first merge function version
startTime = time.time()
mergedWithPointer = mergeIntervalsWithPointers(intervals.copy())
endTime = time.time()
print(f"The version with pointers took: {endTime - startTime:.4f} seconds")
# print(f"Merged intervals: {mergedWithPointer}")

####################################################################################
# Testing the second merge function version
startTime = time.time()
mergedWithoutPointer = mergeIntervalsWithListOperations(intervals.copy())
endTime = time.time()
print(f"The version without pointers took: {endTime - startTime:.4f} seconds")
# print(f"Merged intervals: {mergedWithoutPointer}")
