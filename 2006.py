cAnswer = int(input())

cAnswers = 0

comp1, comp2, comp3, comp4, comp5 = map(int, input().split())

if comp1 == cAnswer:
    cAnswers += 1
    
if comp2 == cAnswer:
    cAnswers += 1
    
if comp3 == cAnswer:
    cAnswers += 1
    
if comp4 == cAnswer:
    cAnswers += 1
    
if comp5 == cAnswer:
    cAnswers += 1
    
print(cAnswers)