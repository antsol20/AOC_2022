def partA():
    input = []

    f = open('input.txt', 'r')

    block_max = 1
    block_total = 0

    for line in f:

        if line == '\n':
            if block_total > block_max:
                block_max = block_total
            block_total = 0
            continue
        
        block_total += int(line.strip())


    print(block_max)

def partB():
    input = []

    f = open('input.txt', 'r')

    block_total = 0
    block_sizes = []
    
    for line in f:
        if line == '\n':
            block_sizes.append(block_total)
            block_total = 0
            continue
        
        block_total += int(line.strip())

    block_sizes.sort(reverse=True)
    print(block_sizes[0:3])
    print(sum(block_sizes[0:3]))


partB()