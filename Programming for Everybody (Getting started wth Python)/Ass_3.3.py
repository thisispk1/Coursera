score = input("Enter Score: ")
try:
    score = float(score)
    if score >1.0:
        print('Please put the score bet 0.0 to 1.0')
        exit()
except:
    print('Please put a numeric value')
    exit()
if score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
else:
    print('F')
