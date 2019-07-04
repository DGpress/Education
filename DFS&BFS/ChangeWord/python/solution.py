'''
    DFS&BFS ChangeWord
    ChangeWord_README.md is explained this simulation.
'''

def solution(begin, target, words):
    '''
        Main body

        begin : (str) the first word for changing to target word.
        target : (str) the target word.
        words : (list) it has variety words.

        This simulation returns the least number of changing.
        Along simulation's conditions, word is changed another word one by one spell.
        If changed word is a target word, this simulation is ended.
        Before ending, this code block is returned the number of changes.
    '''
    answer = 'Error'

    # Check the possibility to change to target
    if target not in words:
        # If target word is not exist in words,
        # begin word is not changed to target word.
        # This case returns 0.
        return 0
    
    n = len(begin) # is an integer which length of inputted all words.
    k = len(words) # is an integer which length of inputted words list.

    level = 0
    # is an integer that means level to change.
    conversion_path = {0 : [begin]}
    # is a dict which has key(is an integer meaning level) and value(is a list which can store words).


    # Run
    while level < k:

        now_words = conversion_path[level]
        # is a list that has words before changing.

        # Check the break point
        if target in now_words:
            # If the target word is exist in now_words,
            # the changing process is no more needed.
            # And return level at the moment.
            return level
        
        level += 1 
        # 1 is added to level.

        availables = getAvailableWords(now_words, words, n)
        # is a list has possible words to change from now_words.

        conversion_path[level] = availables
        # conversion_path adds new key(1 added to level) and value(new level's words).

        words = list(set(words) - set(availables))
        # availables is removed from words.

    return answer

# Run examples
print(solution("hit", "cog", ["hot","dot","dog","lot","log","cog"])) # return 4
print(solution("hit", "cog", ["hot","dot","dog","lot","log"])) # return 0