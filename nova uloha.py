def bubble(list):
    for a in range (0,len(list)):
        for i in range (0,len(list)-a-1):
            if list[i] > list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
                print(list)
    return list

print(bubble([3,8,4,2,5]))