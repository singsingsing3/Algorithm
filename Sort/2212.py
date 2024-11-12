sensor_num=int(input())
k_num=int(input())
sensors=list(map(int,input().split()))
sensors.sort()
distances=[]
for i in range(len(sensors)-1):
    distance=sensors[i+1]-sensors[i]

    distances.append(distance)
distances.sort(reverse=True)
distances=distances[k_num-1:]


print(sum(distances))