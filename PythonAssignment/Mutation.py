d'''

You are given an immutable string, and you want to make changes to it.
STDIN           Function
-----           --------awdwa
abracadabra     s = 'abracadrerabra'
5 k             position = 5, character = 'k'

output : abrackdabra


'''
def mutate_string(string, position, character):
    "Write your logic here."

    return

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
