dict = {}

def add():
    word1 = input('first word: ').lower().strip()
    word2 = input('second word: ').lower().strip()
    if word1 not in dict.keys():
        dict[word1] = {word2}
    else:
        dict[word1].add(word2)
    if word2 not in dict.keys():
        dict[word2] = {word1}
    else:
        dict[word2].add(word1)
    
def count():
    word = input('word: ').lower().strip()
    if word not in dict.keys():
        print(0)
    else:
        print(len(dict[word]))
        
def check():
    word1 = input('first word: ').lower().strip()
    word2 = input('second word: ').lower().strip()
    if word1 not in dict.keys() or word2 not in dict.keys():
        print('No')
    else:
        if word2 in dict[word1]:
            print('Yes')
        else:
            print('No')
            
def main():
    command = input('cmd:> ').lower().strip()
    if command == 'add':
        add()
    elif command == 'count':
        count()
    elif command == 'check':
        check()
    elif command == 'done':
        exit()
    else:
        print('invalid cmd!')
    
while(True):
    main()
