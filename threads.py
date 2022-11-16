import threading
import time

# create a thread with each list within the input.
#  iterate through that list suming all the values between the start and end of the list.
# create a total array that will hold each of the summed values.
# sum the total array to get the total sum. 

threading.Thread()
def runner(num, start, end):
    # """ Thread running function. """

    # for i in range(start, end):
    #     print(f"Running: {name} {i}")
    #     time.sleep(0.2)  # seconds
    print(num, start, end)
    total = 0
    for i in range(start, end + 1):
        total += i

    # print(total)
    result[num] = total

        
        


ex_input = [
    [10, 20],
    [1, 5],
    [70, 80],
    [27, 92],
    [0, 16]
]
thread_count = len(ex_input)
threads = []
total = []
result = [0] * thread_count

for i in range(thread_count):

    # Give them a name
    name = f"Thread{i}"


    # Set up the thread object. We're going to run the function called
    # "runner" and pass it two arguments: the thread's name and count:
    t = threading.Thread(target=runner, args=(i, ex_input[i][0], ex_input[i][1]), daemon=True)

    # The thread won't start executing until we call `start()`:
    t.start()

    # Keep track of this thread so we can join() it later.
    threads.append(t)

# Join all the threads back up to this, the main thread. The main thread
# will block on the join() call until the thread is complete. If the
# thread is already complete, the join() returns immediately.

for t in threads:
    t.join()
print(sum(result))