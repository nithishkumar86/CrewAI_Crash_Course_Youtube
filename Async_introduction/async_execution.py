import asyncio
import time

# def task(name,seconds):
#     print(f"{name} starts")
#     time.sleep(seconds) → blocks entire event loop
#     print(f"{name} ends")

# def main():
#     start_time = time.time()

#     task("task1",1) # 1st.task get started and completed it's work
#     task("task2",1) # then 2nd task get start and complete it's work.  
#     task("task3",1) # then only 3rd task start to work and completet 

#     # task it runs sequentially one after one 

#     endtime = time.time()

#     print("overall time: ",endtime-start_time)

# if __name__ == "__main__":
#     main()


# gather() is useful because:

#  One line instead of a loop
#  Waits for ALL tasks to finish
#  Returns results in order as a list
#  Built-in error handling with return_exceptions=True
#  Cleaner, more readable code


async def task(name,seconds):
    print(f"{name} starts")
    await asyncio.sleep(seconds)# non-blocking
    return f"{name} ends"

async def main():
    start_time = time.time()

    result = await asyncio.gather(   # gather() = Wait for ALL!
        task("task1",1),             # gather() runs coroutines concurrently
        task("task1",1),             # gather() we are waiting for the entire task to finish
        task("task1",1)
    )

    # gather() automatically does what we would manually do 
    # with a loop: create a list, wait for all tasks, and collect results in order.

    print(result)
    print(len(result))

    endtime = time.time()

    print("overall time: ",endtime-start_time)


# Simple - Just Run Tasks Together
# When: You just want to run multiple tasks concurrently, nothing else.
# Use: Direct coroutine calls in gather()

if __name__ == "__main__":
    asyncio.run(main())