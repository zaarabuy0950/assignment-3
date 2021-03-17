# Write code that will print out the anagrams (words that use the same letters) from a paragraph of text.


def anagrams(asd):
    if len(asd) <= 1:
        yield asd
    else:
        for word in anagrams(asd[1:]):
            for i in range(len(asd)):
                yield word[:1] + asd[0:1] + word[1:]
            return f"{asd}"


result = input("enter a word:")
print(list(anagrams(result)))
