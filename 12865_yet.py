N, K = map(int, input().split())


values = list()


for i in range(N):
    W, V = map(int, input().split())
    
    each_v =  V / W 
    values.append({
        'W': W,
        'V': V,
        'each_V': each_v
    })
    

list_value = [v['each_V'] for v in values]

index_max = max(range(len(values)), key=values.__getitem__)

print(list_value.index.max(list_value))
# highest = values.index.max(list(v['each_V'] for v in values))
# highest = [max(x.each_V) for x in values]
# print(highest)