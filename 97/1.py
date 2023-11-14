# Multi-threading

# Import the threading and time modules
import threading
import time

# Define a function that simulates some task being done


def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)


# Create three threads, each representing a task with different durations
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])

# Start the threads to execute the tasks concurrently
t1.start()
t2.start()
t3.start()

# Wait for all threads to complete using join
t1.join()
t2.join()
t3.join()
