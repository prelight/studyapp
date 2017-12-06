import asyncio

Seconds = [
    #[3, 4],
    ("first", 5),
    ("second", 0),
    ("third", 3)
]

async def sleeping(order, seconds, hook=None):
    print("start sleeping ...")
    await asyncio.sleep(seconds)
    if hook:
        hook(order)
    print("end sleeping ...")
    return order


async def basic_async():
    print("-- ok")
    # the order of result is nonsequential (not depends on order, even sleeping time)
    for s in Seconds:
        print("-- s")
        r = await sleeping(*s)
        print("{0} is finished.".format(r))
    return True


async def parallel_by_gather():
    print("start parallel_by_gather")
    # execute by parallel
    def notify(order):
        print(order + " has just finished.")

    #cors = []
    #for s in Seconds:
    #    r = sleeping(s[0], s[1], hook=notify)
    #    print("... nn")
    #    cors.append(r)

    cors = [sleeping(s[0], s[1], hook=notify) for s in Seconds]
    print(cors)
    results = await asyncio.gather(*cors)
    print(results)
    return results


async def action_print():
    print("start action_print.")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(parallel_by_gather())
    #r = await parallel_by_gather()
    #await asyncio.sleep(seconds)
    ##results = loop.run_until_complete(action_print())
    for r in results:
        print("asyncio.gather result: {0}".format(r))
