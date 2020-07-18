def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
      assert 0 <= from_index <= to_index <= 10 ** 18
      lis=[0,1]
      S6=280
      start=from_index-1
      final=0
      final1=0
      if (start)<60:
        for i in range(0,from_index):
            fib=lis[-1]+lis[-2]
            ld=fib%10
            lis.append(ld)
            p=sum(lis[0:-2])
            final=p
      else:
                      r=start%60
                      d=start//60
                      add=d*S6

                      for i in range(0,r+1):
                        fib=lis[-1]+lis[-2]
                        ld=fib%10
                        lis.append(ld)
                        p=sum(lis[0:-2])
                      final=p+add

      if to_index<60:

        nlis=[0,1]
        ld=0
        for i in range(0,to_index+1):
            fi=nlis[-1]+nlis[-2]
            ld=fi%10
            nlis.append(ld)
            P2=sum(nlis[0:-2])
            final1=P2

      else:

                      nlis=[0,1]
                      ld=0
                      r=to_index%60
                      d=to_index//60
                      add1=d*S6
                      for i in range(0,r+1):
                        fib=nlis[-1]+nlis[-2]
                        ld=fib%10
                        nlis.append(ld)
                        p2=sum(nlis[0:-2])
                      final1=p2+add1
      final3=final1-final
      return (final3%10)



if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))