"""
for i in range(1, 11, 2):
    print(i)

print()

for i in range(1, 11):
    print(i)

print()

for i in range( 11 ):
    print( i )
"""

#Write a Python program to find those numbers which
#are divisible by 7 and multiple of 5, between
#1500 and 2700 (both included).

"""
for i in range( 1500, 2701):
    if( (i%5 == 0) and (i%7 == 0) ):
        print(i)

"""

"""
  1   #w1         #W2
  2   #w1
  3   #w1
  4   #w1
  5   #w1
  1               #W2
  2
  3
  4
  5
  1               #W2
  2
  3
  4
  5
"""
#W3 = W2 * 4


count_i = 0
count_j = 0
count_k = 0

for k in range(1, 5):
    for j in range(1, 4):
        for i in range(1, 6):
            print(i)
            count_i = count_i + 1

        count_j = count_j + 1

    count_k = count_k + 1


print( 'count_i', count_i )
print( 'count_j', count_j )
print( 'count_k', count_k )
