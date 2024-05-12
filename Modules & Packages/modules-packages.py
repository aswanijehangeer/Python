## Modules and Packagaes ----



 
# import func
# from func import greeting, wish
# from func import *
# from func import greeting as greet, wish as wishing


# greeting("Jehangeer")
# wish("Jehangeer")


# greet("Jehangeer")
# wishing("Jehangeer")


## Package ----

# from func import func, func2
# from func.func import wish

# wish("Saraj")

# func.greeting("Jehangeer")
# func.wish("Jehangeer")

# func2.bye("Jehangeer")



## Random Module ----

from random import *

# print(
#     round(random(), 3),
#     randint(0, 10),
#     uniform(1.25, 2.0),
#     randrange(0, 100, 4),
#     randrange(1, 101, 2)
# )

# def die(num):
#     seed = num
#     return randint(1, 6)

# print(die(2))

# lst = ["a", "b", "c", "d", "e", "f"]
# shuffle(lst)

# print(lst)

# print(
#     choice(lst),
#     sample(lst, 3)
# )


## Date-Time Module ----

from datetime import datetime, date

Time = datetime.now()
Date = date.today()

Custom_time = datetime(year = 2001, month = 8, day = 4, hour = 15, minute = 30, second = 12)

print(Custom_time)


print(
    Time,
    Time.year,
    Time.month,
    Time.day,
    Date
)

TimeDiff = Time - Custom_time
print(TimeDiff)

