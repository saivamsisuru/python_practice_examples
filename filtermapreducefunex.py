import functools
lst=[int(val) for val in input().split() if 0<=int(val)<=1000]
sal0_500=list(filter(lambda n: 0<=n<=500,lst))
print("salaries from 0 to 500",sal0_500)
hikesal0_500=list(map(lambda n:n+n*10/100,sal0_500))
print("salaries from 0 to 500 with hike of 10percent",hikesal0_500)
totsal0_500=functools.reduce(lambda a,b:a+b,hikesal0_500)
print("total salaries from 0 to 500 with hike ",totsal0_500)
sal501_1000=list(filter(lambda n: 501<=n<=1000,lst))
print("salaries from 501 to 1000",sal501_1000)
hikesal501_1000=list(map(lambda n:n+n*20/100,sal501_1000))
print("salaries from 501 to 1000 with 20 percent of hike",hikesal501_1000)
totsal501_1000=functools.reduce(lambda a,b:a+b,hikesal501_1000)
print("totalsalaries from 501 to 1000 with hike",totsal501_1000)
totalsalaries0_1000=totsal0_500+totsal501_1000
print("totalsalaries given to 0 to 1000 with hike",totalsalaries0_1000)