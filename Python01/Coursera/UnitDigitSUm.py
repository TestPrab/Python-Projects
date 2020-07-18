def last_digit_of_the_sum_of_fibonacci_numbers(n):
  assert 0 <= n <= 10 ** 18
  lis=[0,1]
  S6=280
  if n<60:
    for i in range(0,n+1):
        fib=lis[-1]+lis[-2]
        ld=fib%10
        lis.append(ld)
        p=sum(lis[0:-2])
    return (p%10)
  else:
                  r=n%60
                  d=n//60
                  add=d*S6
                  for i in range(0,r+1):
                    fib=lis[-1]+lis[-2]
                    ld=fib%10
                    lis.append(ld)
                    p=sum(lis[0:-2])
                  final=p+add
                  return (final%10)





if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))
    