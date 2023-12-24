class Solution:
  def toGoatLatin(self, sentence: str) -> str:
    ma = "ma"
    a = "a"

    vowels = "aeiouAEIOU"
    words = sentence.split(" ")

    count = 1
    newWords = []

    for word in words:
      if word[0] not in vowels:
        newWord = word[1:] + word[0]
      else:
        newWord = word
      newWord += ma + a * count
      count += 1
      newWords.append(newWord)
    

        
    return " ".join(newWords)
