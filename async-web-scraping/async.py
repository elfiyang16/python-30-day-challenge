import time
import asyncio

iteration_times = [1, 3, 2, 4]

async def sleeper(seconds, i=-1):
    start_time = time.time()
    if i != -1:
        print(f"{i}\t{seconds}s")
    await asyncio.sleep(seconds)
    return time.time() - start_time

run_time = 0
total_compute_run_time = 0
async def main():
    global run_time
    global total_compute_run_time
    tasks = []
    for i, second in enumerate(iteration_times):
      tasks.append(asyncio.create_task(sleeper(second, i =i)))
    result = await asyncio.gather(*tasks)
    print(result)
# 0       1s
# 1       3s
# 2       2s
# 3       4s
# [1.0019781589508057, 3.0044989585876465, 2.0033936500549316, 4.003766059875488]
    for run_time_result in result:
      total_compute_run_time += run_time_result
      if run_time_result > run_time:
        run_time += run_time_result
        
        
asyncio.run(main())
print(f"Ran for {run_time} seconds, with a total of {total_compute_run_time}")

# 0       1s
# 1       3s
# 2       2s
# 3       4s
# [1.0050408840179443, 3.004312038421631, 2.004349946975708, 4.00273585319519]
# Ran for 4.009352922439575 seconds, with a total of 10.016438722610474