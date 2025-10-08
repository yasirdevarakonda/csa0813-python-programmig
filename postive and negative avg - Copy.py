positive_sum=0
positive_count=0
negative_sum=0
negative_count=0
while True:
    num=int(input())
    if num==-1:
        break
    elif num>=0:
        positive_sum+=num
        positive_count+=1
    else:
        negative_sum+= num
        negative_count+=1
positive_avg=positive_sum//positive_count
negative_avg=negative_sum//negative_count
print(positive_avg)
print(negative_avg)
