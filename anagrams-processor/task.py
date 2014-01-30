#!/usr/bin/env python
import sys

backup_words = ["ail", "tennis", "nails", "desk", "aliens", "table", "engine", "sail", "tail","sailq","aliensd", "taile", "pail", "pile", "lipea", "in", "sin", "sina"] 
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def read_words():
	try:
		with open("words.txt") as f:
			content = f.read()
		f.close()
	except IOError:
		return backup_words
	return content.split("\n")
	
def hash_word(word):
	multi = 1
	for letter in list(word):
		multi *= hash_letter(word, letter)
	return multi
	
def hash_letter(word, letter):
	return ord(letter) * 7 + word.count(letter) * 23

def find_longest_of_initial_word(word, dict):
	final_der = find_longest_derivation(word, dict, [])
	final_der.append(word)
	final_der.sort(key = lambda s: len(s))
	return final_der

def find_longest_derivation(word, dict, der_list):
	derivations = find_derivations(word, dict)
	for derivation in derivations:
		inner_list = []
		inner_list.append(derivation)
		longest = find_longest_derivation(derivation, dict, inner_list)
		inner_list.extend(longest)
		if len(inner_list)>len(der_list):
			der_list=inner_list
	return list(set(der_list))

def find_derivations(of_word, dict):
	if not dict.has_key(len(of_word)+1):
		return []
	result = []
	length = len(of_word) + 1
	for letter in alpha:
		new_hash = hash_word(of_word + letter)
		if dict[length].has_key(new_hash):
			result.append(dict[length][new_hash])
	return result
	
def index_words(words):
	dict = {}
	for word in words:
		hash = hash_word(word)
		length = len(word)
		if length < 3:
			continue
		if not dict.has_key(length):
			dict[length] = {}
		if not dict[length].has_key(hash):
			dict[length][hash] = ""
		dict[length][hash] = word
	return dict
	
def words_with_length(dict, length):
	words = []
	if not dict.has_key(length):
		return words
	for hash in dict[length].keys():
		words.append(dict[length][hash])
	return words
	
if __name__ == "__main__":
	print "Reading words ..."
	words = read_words()
	print "Indexing dictionary ..."
	dict = index_words(words)
	ders = []
	for word in words_with_length(dict, 3):
		print "Looking for derivations of ", word, "..."
		final_der = find_longest_of_initial_word(word, dict)
		ders.append(final_der)
		print "Longest path of derivation of ", word, ": ", final_der
		
	print "Longest path of derivation of all the three letter words is: ", max(ders, key=len)