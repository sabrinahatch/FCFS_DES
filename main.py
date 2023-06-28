# create for different loads, save each as its own file
# figure out how to plot after that??
# do for different distributions (deterministic, bimodal, weibull)

import numpy as np


class Job:
    def __init__(self, arrivalTime, size):
        self.arrivalTime = arrivalTime
        self.size = size
        self.departureTime = None

        # job size / arrival time s.t. 10/ i


def generateJobSize():
    return np.random.exponential(1)


# Function that generates an interarrival time
def generateInterarrivalTime():
    return np.random.exponential(10 / 9)


def handleArr():
    global clock, serverEmpty, servingJob, nextArrTime, nextDepTime, completionTimes, jobSizes
    size = generateJobSize()
    job = Job(arrivalTime=clock, size=size)
    jobSizes.append(size)
    if serverEmpty:
        servingJob = job
        nextDepTime = clock + servingJob.size
        serverEmpty = False
    else:
        jobQueue.append(job)
    interArrTime = generateInterarrivalTime()
    nextArrTime = clock + interArrTime


def handleDep():
    global clock, departures, serverEmpty, servingJob, nextDepTime, completionTimes
    departures += 1
    servingJob.departureTime = clock + servingJob.size
    completionTimes.append(servingJob.departureTime - servingJob.arrivalTime)

    if len(jobQueue) != 0:
        # double check
        servingJob = jobQueue.pop()
        nextDepTime = clock + servingJob.size
    else:
        serverEmpty = True
        nextDepTime = float("inf")
        servingJob = None

seed = 0
maxDepartures = 5
runCompletions = []

runs = 10
for i in range(runs):
    np.random.seed(seed)


    departures = 0
    nextDepTime = float('inf')
    jobQueue = []
    completionTimes = []
    jobSizes = []

    serverEmpty = True

    nextArrTime = generateInterarrivalTime()
    clock = 0.0

    while departures <= maxDepartures:
        if nextArrTime <= nextDepTime:
            clock = nextArrTime
            handleArr()
        else:
            clock = nextDepTime
            handleDep()
    runCompletions.append(completionTimes.pop())
    # runCompletions.append(completionTimes.pop())
    seed += 1
print(len(runCompletions))





print(sum(completionTimes) / len(completionTimes))
print(sum(jobSizes) / len(jobSizes))

# turns the list of completion times into a numpy array

# with open("FCFS_LOAD_0.9.txt", "w") as fp:
#     for item in runCompletions:
#         fp.write("%s\n" % item)

runCompletions = np.array(runCompletions)
print(runCompletions)
np.save("testFile.npy", runCompletions)

# save the last one




