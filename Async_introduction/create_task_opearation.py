import asyncio

async def write_chapter(num):
    print(f"📝 Chapter {num} STARTED")
    await asyncio.sleep(2)
    print(f"✅ Chapter {num} DONE")
    return f"Chapter {num}"

async def main():
    tasks = []
    
    # Step 1: create_task - Tasks START immediately!
    print("Creating tasks...\n")
    for i in range(1, 4):
        task = asyncio.create_task(write_chapter(i))  # ← STARTS NOW!
        print(f"Task {i} object: {task}") 
        tasks.append(task)

#"In create_task() already the task submission is done 
# and it returns task object for reference"
    
    print("\n✨ All 3 tasks are NOW RUNNING in background!\n")
    print("Now using gather() to wait for them...\n")
    
    # Step 2: gather - Just WAITS for all to finish
    chapters = await asyncio.gather(*tasks)  # ← Waits here
    
    print(f"\n📚 Got all results: {chapters}")
    print(f"length of the data is :",len(chapters))

if __name__ == "__main__":
    asyncio.run(main())



# Creating tasks...

# Task 1 object: <Task pending name='Task-2'>
# 📝 Chapter 1 STARTED
# Task 2 object: <Task pending name='Task-3'>
# 📝 Chapter 2 STARTED
# Task 3 object: <Task pending name='Task-4'>
# 📝 Chapter 3 STARTED

# ✨ All 3 tasks are NOW RUNNING in background!

# Now using gather() to wait for them...

# ✅ Chapter 1 DONE
# ✅ Chapter 2 DONE
# ✅ Chapter 3 DONE

# 📚 Got all results: ['Chapter 1', 'Chapter 2', 'Chapter 3']



# ✅ Perfect Summary
# Corrected version of your understanding:

# ✅ create_task() immediately starts the function
# ✅ Returns a Task object (not just ID)
# ✅ We append Task objects to a list
# ✅ We unpack (*tasks) and pass to gather()
# ✅ Tasks are already executing concurrently
# ✅ gather() waits for ALL to complete
# ✅ Returns results in order as a list

# Grade: A+ 🌟

# 🎯 One Sentence Summary

# "create_task() starts tasks immediately and returns Task objects
#  We collect these objects in a list, unpack them, and pass to gather(),
#  which waits for ALL tasks to complete and returns results in order."