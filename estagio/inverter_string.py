string = input("Escreva uma palavra: ")
vetor = list(string)
string_reversed = [''] * len(string)

for i in range(len(string)):
    string_reversed[i] = vetor[len(string) - i - 1]

string_reversed = ''.join(string_reversed)
print(string_reversed)
