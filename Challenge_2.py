word = str(input())
if (len(word)%2 == 0):
    print(f"The given string {word} is even .\nExtracting the middle two characters : {word[(len(word)-1)//2:(len(word)+2)//2]}")

else:
    print(f"The given string {word} is odd .\nExtracting the middle character : {word[(len(word)-1)//2:(len(word)+2)//2]}")



