def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []
    summation=0
    i=0
    while True:
      i+=1
      summation=sum(summands)+i
      if summation<=n:
        summands.append(i)
        continue
      else:
        break
     
    summation=sum(summands)
    if summation<n:
     
      last=summands[-1]
      add=n-sum(summands)
    
      summands[-1]=last+add
    return summands

if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)