
# Напишите программу, удаляющая из текста слова абв

string = ' Питон - пожаабвлуй лучший из худабвших языков в мире'
new_list = list(filter(lambda word: not 'абв' in word, string.split()))
print(' '.join(new_list))


new_list = [x for x in string.split() if not 'абв' in x]
print(' '.join(new_list))