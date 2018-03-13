'''
TwoSum
'''

def contains_pair(num_list):
    num_list = [int(x) for x in num_list.split('\n')]
    
    for i in range(len(num_list)):
        for j in range(len(num_list)):
            if i == j:
                continue
            if num_list[i] + num_list[j] == 0:
                print('Yep, {} + {} = 0'.format(num_list[i], num_list[j]))
                return True
    
    return False
    
print(contains_pair('3\n-1\n4\n1'))
