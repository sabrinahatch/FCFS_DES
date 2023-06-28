**Pseudocode for FCFS single server model**
<br>
*system objects:*
jobs, server
<br>
*system events:*
job arrival, job departure
<br>
*system variables:* 
queueLen, serverStatus, interArrivalTime, serviceTime, departThreshold, count

1. while count <= departThreshold
2. determine the next event (arrival or departure)
      1. If arrival:
         1. on current event, schedule the curr event's departure and generate a scheduled time for next arrival based on distribution. 
         2. If time of next arrival < time of departure, process next arrival (see step 3 for specific instructions)
         3. else if time of departure < time of arrival, process departure (see step 3 for specific instructions), inc count
         4. go back to step 1
      2. else if departure:
         1. inc count
         2. process departure (see step 3 for specific instructions)
         3. Go back to step 1
3. Process the next event
   1. when a job arrival event occurs, the state var queueLen is incremented by one.
   If the state variable serverStatus is set to "available", a job service start event is triggered w/o any delay.
   2. Once a job service start event occurs, the state var serverStatus is changed to "busy"
   and a job service end event is scheduled with a delay based on the service time.
   3. Once a job service departure event is triggered, the state var queueLen is decremented by one (the job leaving the system), and count is incremented by one.
   If the state var queueLen is not zero, a job service start event is triggered without any delay.
   If the queue is empty, the serverStatus is set to available and the system waits for a new job arrival to occur. 
4. Go back to step one. Loop through above steps until the departThreshold is met. 

<br>
<br>
<!-- end of the list -->

**Pseudocode for SRPT single server model**
<br>
*system objects:*
A < B
jobs, server
<br>
*system events:*
job arrival, job departure
<br>
*system variables:* 
jobSize, queueLen, interArrivalTime, departThreshold, count, lastTime, delta, serverStatus

1. while count <= departThreshold
2. determine the next event (arrival or departure)
      1. If arrival:
         1. on current event, determine the current event's service time based on job size and generate a scheduled time for next arrival based on distribution. 
         2. If the current arrival's service time < remaining service time of event being serviced, preempt current event being serviced and begin servicing the current arrival (set serverStatus to busy).
         3. else if current arrival service time > remaining service time of event being serviced, continue processing current job until departure
            (see step 3 for more instructions) and queue*** then wait until next event
         4. On next event, go back to step 2
      2. else if departure:
         1. inc count
         2. process departure (see step 3 for specific instructions)
         3. Go back to step 1
3. Process the next event
   1. when a job arrival event occurs, the state var queueLen is incremented by one.
   If the state variable serverStatus is set to "available", a job service start event is triggered w/o any delay.
   2. Once a job service start event occurs, the lastTime variable is assigned to the exact time the job begins getting serviced
      1. if the job is preempted during processing, calculate delta by subtracting lastTime from the current time and subtracting this
      difference from the job's total service time attriubute to update it's current remaining processing time. 
      2. if the job is not preempted, continue running the job until a new arrival arrives that is smaller than it. 
   3. Once a job service departure event is triggered, the state var queueLen is decremented by one (the job leaving the system), and count is incremented by one.
   If the state var queueLen is not zero, a job service start event is triggered without any delay based on the smallest remaining processing time of each job.
   If the queue is empty,the system waits for a new job arrival to occur. 
4. Go back to step one. Loop through above steps until the departThreshold is met. 

