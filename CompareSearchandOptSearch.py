from tabulate import tabulate
import random
import time

# generate data
def generate_dateset():
    A = []
    while len(A) < 10**6:
        A.append(random.randint(0, 10**6))
    return A


# generate_key
def generate_key():
    key = []
    while len(key) < 10:
        temp = random.randint(0, 10**6)
        if temp not in key:
            key.append(temp)
    return key


# Search
def Search(A, x):
    for i in range(len(A)):
        if A[i] == x:
            return i
    return -1

# OptSearch
def OptSearch(A, x):
    A.append(x)
    if A.index(x)==len(A)-1:
        return -1
    else: return A.index(x)

# Now, we start to compare
def compare(A, key):
    result = []
    for i in range(len(key)):
        AnswerEachKey = []
        # Search
        start_Search = time.time()
        ans_Search = Search(A, key[i])
        end_Search = time.time()
        # optSearch
        start_optSearch = time.time()
        ans_optSearch = OptSearch(A, key[i])
        end_optSearch = time.time()

        # AnswerEachKey = [time_Search, time_optSearch, index]
        if ans_Search != ans_optSearch:
            AnswerEachKey.append('Your function is Error, go to the hell!')
        else:
            AnswerEachKey.append(key[i])
            AnswerEachKey.append(end_Search-start_Search)
            AnswerEachKey.append(end_optSearch-start_optSearch)
            AnswerEachKey.append(ans_Search)
        # finally save in result
        result.append(AnswerEachKey)
    return result

# main
if __name__ == '__main__':
    A = generate_dateset()
    key = generate_key()
    result = compare(A,key)
    print(tabulate(result,headers = ["KEY", "SEARCH", "OPTSEARCH","INDEX"],tablefmt='orgtbl'))

