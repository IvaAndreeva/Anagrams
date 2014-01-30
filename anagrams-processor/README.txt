Task:
An anagram derivation is a N-letter word derived from a N-1 letter word by adding a letter and rearranging. Write a program that will find the longest such derivation from a 3-letter word in a list of words where every derived word also exists in the list of words. (Process the longest derivations for all the 3 letter words in the dictionary)

Algorithm:
Before running the search i'm indexing the dictionary the following way:
	dict: { $word_length: { $word_hash: $word,
							$word_hash: $word,
							...
						},
						
			$word_length:{ $word_hash: $word,
							$word_hash: $word,
							...
						},
			...
	}
	
Since the hash function is returning the same hash only for words with the same letters but rearranged, we don't really care which one we save in the dictionary because we don't care about the order of the letters anyway.
For finding the derivations:
	1. take the given word (ex. "ail")
	2. for each letter in alphabet try:
		2.1. add letter to the given word (ex. "s" to "ail")
		2.2. calculate the hash of the newly created word
		2.3. check if there is such a hash in the dictionary in the words with length(given word) + 1
			- if yes add to derivations and move on
	
Hash function:
It's basically "home made" - for each letter in the word:
	hash *= ascii code (letter) * prime num(ex. 7) + number of times letter is in word * prime number (ex. 23)
	
By default the script works with words.txt in the zip, but that can be changed to wordsEn.txt (100 000+ words).
