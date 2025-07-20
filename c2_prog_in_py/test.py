try:
    with open('./test.txt',mode='r') as file:
        for x in file:
            print(x)
except FileNotFoundError as e:
    print("Error",e)

trial = 'reversal'
trial = trial[::-1]
print(trial)
