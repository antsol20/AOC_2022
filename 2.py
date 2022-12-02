def partA():
    input = []

    f = open('input.txt', 'r')

    my_scores = {'X': 1, 'Y': 2, 'Z': 3}
    opp_map = {'A': 'X', 'B': 'Y', 'C': 'Z'}

    wins = {'AY', 'BZ', 'CX'}

    score = 0

    for line in f:
        newline = line.strip().replace(' ', '')

        if newline in wins:
            score += 6

        if newline[1] == opp_map[newline[0]]:
            score += 3
        
        score += my_scores[newline[1]]

    print(score)


def partB():

    wins = {'A': 'B', 'B': 'C', 'C': 'A'}
    loses = {'A': 'C', 'B': 'A', 'C': 'B'}
    scores_map = {'A': 1, 'B': 2, 'C': 3}

    f = open('input.txt', 'r')

    score = 0
    
    for line in f:
        newline = line.strip().replace(' ', '')
        
        if newline[1] == 'Z':
            score =+ 6
            score += scores_map[wins[newline[0]]]
           
        elif newline[1] == 'Y':
            score += 3
            score += scores_map[newline[0]]
        
        elif newline[1] == 'X':
            score += 0
            their = newline[0]
            loss = loses[their]
            loss_score = scores_map[loss]
            score += loss_score

    print(score)
            

def test():
    #Load the puzzle data
    with open('input.txt') as f:
        data = [line.strip() for line in f.readlines()]

    #Part 1
    wins = ['A Y', 'B Z', 'C X']
    draws = ['A X', 'B Y', 'C Z']
    score = 0
    for line in data:
        if line in wins:
            score += 6
        elif line in draws:
            score += 3
        score += ' XYZ'.index(line.split()[1])
    print(score)

    #Part 2
    score = 0
    for line in data:
        elf, me = line.split()
        if me == 'Y':
            score += 3 + ' ABC'.index(elf)
        elif me == 'Z':
            score += 6 + ' CAB'.index(elf)
        else:
            score += ' BCA'.index(elf)
    print(score)


partB()