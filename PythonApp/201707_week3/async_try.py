import asyncio

Seconds = [
    #[3, 4],
    ("first", 5),
    ("second", 0),
    ("third", 3)
]

async def sleeping(order, seconds, hook=None):
    await asyncio.sleep(seconds)
    #if hook:
    #    hook(order)
    return order


async def basic_async():
    print("-- ok")
    # the order of result is nonsequential (not depends on order, even sleeping time)
    for s in Seconds:
        print("-- s")
        r = await sleeping(*s)
        print("{0} is finished.".format(r))
    return True

if __name__ == "__main__":
    #t = 4, 6
    #print(t[1])


    #for s in Seconds:
    #    print(s[0])

    loop = asyncio.get_event_loop()
    loop.run_until_complete(basic_async())

