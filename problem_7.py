# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'. 1111 -> 1, 1, 1, 1; 11, 11;1,11,1; 1, 1, 11; 11, 1, 1

# You can assume that the messages are decodable. For example, '001' is not allowed.

letters = ['a', 'b', 'c', 'd']


def possibleCombinations(k):
    kList = []
    kList[:0] = k
    validList = []

    if kList[0] == '0':
        print('invalid input')
    else:
        for i in range(kList.count):
            currentDigit = int(kList[i], 10)
            nextDigit = int(kList[i+1], 10)

            if currentDigit > 0:
                validList.append(currentDigit)
            if currentDigit < 2:


def decode(k):
    pass
