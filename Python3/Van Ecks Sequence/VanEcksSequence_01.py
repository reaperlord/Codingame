import numpy

seqVal = int(input()) #current sequence val as string
end_n = int(input())
current_n = 1

counterArray = numpy.zeros(end_n, int)

while current_n != end_n:

    stepsAgo = current_n - counterArray[seqVal]

    if stepsAgo != current_n: #i.e. the array counter returned non-zero
        next_seqVal = current_n - counterArray[seqVal]
    else: #the seqVal was new
        next_seqVal = 0
    
    counterArray[seqVal] = current_n #regardless the counter for that index is set to the current_n

    seqVal = next_seqVal
    current_n += 1

print(seqVal)
