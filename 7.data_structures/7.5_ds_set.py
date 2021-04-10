############################################ 集合 ############################################
# 集合（Set）是简单对象的无序集合（Collection）
# 集合适用于判断其中是否存在某个项目的场景

bri = set(['brazil', 'russia', 'india'])
print('india' in bri)
print('usa' in bri)
bric = bri.copy()
bric.add('china')
print(bric.issuperset(bri))
bri.remove('russia')
print(bri & bric) # OR bri.intersection(bric)
{'brazil', 'india'}

print('bri===>', bri)
print('bric===>', bric)

