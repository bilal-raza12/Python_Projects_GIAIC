def digits_sum(num: int) -> int:
    sum: int = 0

    for i in str(num):
        sum += int(i)
        
    return sum


res: int = digits_sum(2345)
print(res)