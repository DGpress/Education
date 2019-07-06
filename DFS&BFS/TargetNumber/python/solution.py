'''
    DFS&BFS TargetNumber
    TargetNumber_README.md is explained this simulation.
'''

def solution(numbers, target):
    '''
        Main body

        numbers : (list) has integers.
        target : (int) is an integer.

        This simulation returns the number of all combinations which is making target
        with number from numbers.
    '''
    result = [] # The list storing all combinations.

    # Run
    for number in numbers:

        if len(result) < 1:
            # The initial case.
            result.append(number) # The case of first added number.
            result.insert(0, number*-1) # The case of first subtracted number.
            
        else:
            # After initial case.
            temp = [] # for storing subtracted numbers.

            for i in range(len(result)):
                # get a number by result's index.
                temp.append(result[i] - number) # temp appends subtractted numbers.
                result[i] += number # all number of result added with number.
            
            result.extend(temp) # merge result with temp.
            
            result.sort() # sort the result
            
    answer = result.count(target)
    # After Run, all cases of combinations are in result.
    # And count target number from result.

    return answer

# Run example
print(solution([1,1,1,1,1], 3)) # returns 5