import asyncio
import time

# def addition(a: int,b: int):
#     time.sleep(1)
#     return a + b

# def subtraction(a: int,b: int):
#     time.sleep(1)
#     return a - b

# def multiplication(a: int,b: int):
#     time.sleep(1)
#     return a * b

# def division(a: int,b: int):
#     time.sleep(1)
#     return a / b

# def main():  # coroutines
#     start_time = time.time()

#     result1 = addition(10,5)
#     result2 = subtraction(10,5)
#     result3 = multiplication(10,5)
#     result4 = division(10,5)

#     end_time = time.time()

#     print("overall time: ",end_time-start_time)

#     print("result1 is",result1)
#     print("result2 is",result2)
#     print("result3 is",result3)
#     print("result4 is",result4)


# if __name__ == "__main__":
#     main() 


async def addition(a: int,b: int):
    await asyncio.sleep(1)
    return a + b

async def subtraction(a: int,b: int):
    await asyncio.sleep(1)
    return a - b

async def multiplication(a: int,b: int):
    await asyncio.sleep(1)
    return a * b

async def division(a: int,b: int):
    await asyncio.sleep(1)
    return a / b


async def main():  # coroutines
    start_time = time.time()

    response = await asyncio.gather(
        addition(10,5),
        subtraction(10,5),
        multiplication(10,5),
        division(10,5),

    )
    end_time = time.time()

    print("overall time: ",end_time-start_time)

    print("overall time is: ",response)
    print("lenght of value is: ",len(response))

if __name__ == "__main__":
    asyncio.run(main()) 

'''

The event loop is the core engine behind asynchronous programming
It:
Runs asynchronous functions (coroutines)
Manages tasks
Decides wat runs next
Switches between tasks when they are waiting
In simple words:

'''

'''
The event loop is a manager that keeps track of all async tasks and runs them efficiently.

the event loop is provided by the built-in module:
asyncio.run(main())
Creates an event loop
Runs your async function
Closes the loop
    
'''


# You know:

# async def - Define async functions
# await - Wait without blocking
# create_task() - Start tasks immediately, get Task object
# gather() - Wait for all, returns LIST
# Use case decides the pattern