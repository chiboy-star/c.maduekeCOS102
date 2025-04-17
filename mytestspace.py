
'''
s = 'python'
output = ''
for i in range(-1,-len(s)-1,-2):
    output += s[i]
print(output)

text = "looping"
result = ""
for i in range(len(text)):
    if i in (1,3,5):
        continue
    result += text[i]
print(result)

def mystery(lst):
    temp = []
    for i in range(len(lst)):
        if lst[i] not in temp:
            temp.append(lst[i])
        else:
            temp.remove(lst[i])
    return temp

numbers = [1,2,2,3,1,4,4]
print(mystery(numbers))
'''
'''
data = [1,2,3,4,5,6]
i = 0
while i < len(data):
    if data[i] % 3 == 0:
        data.insert(i+1,data[i]*2)
        i+=2
    else:
        i += 1
print(data)


text = 'mississippi'
output = ''
for i in range(len(text)):
    if i % 2 == 0:
        continue
    if text[i] in output:
        break
    output += text[i]

print(output)'''