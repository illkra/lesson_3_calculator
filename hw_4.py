# 1
text1 = "Hello, World!"

# a.
print(text1[2])

# b.
print(text1[-2])

# c.
print(text1[:5])

# d.
print(text1[:-2])

# e.
print(text1[::2])

# f.
print(text1[1::2])

# g.
print(text1[::-1])

# h.
print(text1[-1::-2])

# i.
print(len(text1))

# 2
text2 = "Some example text"

print(text2)
word_count = text2.count(' ') + 1
print(f"Word count: {word_count}")


# 3
s = input("Enter a string: ")
ch = input("Enter a symbol: ")

positions = []

position = s.find(ch)
while position != -1:
    positions.append(position)
    position = s.find(ch, position + 1)
if positions:
    print(f"Symbol '{ch}' found on position: {positions}")
else:
    print(f"Symbol '{ch}' not found.")

# 4

text3 = "hello, how are you? hello, there!"

text3 = text3[:text3.find('h')+1] + text3[text3.find('h')+1:text3.rfind('h')].replace('h', 'H') + text3[text3.rfind('h'):]
print(text3)