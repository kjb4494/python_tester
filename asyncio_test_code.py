
import asyncio
import time


async def async_test(num):
    print('start' + str(num))
    await loop.run_in_executor(None, time.sleep, 3)
    print('start second loop!' + str(num))
    await loop.run_in_executor(None, time.sleep, 1)
    print('end' + str(num))


if __name__ == '__main__':
    futures = [async_test(num) for num in range(100)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(futures))
    print('finished')
