def lengthOfLongestWord(string: str):
    arr = string.split()
    word_lengths = []
    for i in range(len(arr)):
        word_lengths.append(len(arr[i]))
    return max(word_lengths)

string = 'Ye mera Jahan'
print(lengthOfLongestWord(string))