#!/usr/bin/env python3

import itertools
import random
import string

# Common words and leetspeak mapping derived from rockyou and yes i typed it by hand because im retarded
common_words = ["password", "admin", "user", "login", "root", "welcome", "guest", "letmein", "12345", "password1",
                "cerberus", "adminadmin", "bosco", "bonzai", "yeet", "babygirl", "love", "awesome", "amazon", "sucks", 
                "children", "stanley", "goober", "doraemon", "ingrid", "father", "geraldine", "dimple", "dillon", "romance", 
                "bunny", "bhaby", "baby", "winner", "tweetybird", "kathryn", "paramore", "allstar", "abcde", "something", 
                "runescape", "jermaine", "jefferson", "pitbull", "seventeen", "romania", "france", "emotional", "nigger", "mariela", 
                "fucku", "bitchy", "ballin", "loveless", "smallville", "ricky", "peluche", "godbless", "blue123", "alonso", "meghan", 
                "garrett", "mexicol", "clover", "vanesa", "smudge", "cooldude", "chopper", "cassidy", "andreita", "134679", "cherries", 
                "070707", "skippy", "kaykay", "domino", "ximena", "julie", "goldie", "daisy1", "bella1", "thailand", "puppy", "gladys", 
                "computer1", "boricua", "karate", "janjan", "freddie", "acuario", "yugioh", "marjorie", "maggie1", "blueberry", "joyce", 
                "basket", "sunset", "hummer", "destiny1", "annie", "angelbaby" "amber1", "pakistan", "negrita", "kendra", "kyndra", "blue22", 
                "dipset", "coconut", "kirsty", "danilo", "alexis1", "whatever1", "cameron1", "booboo1", "aileen", "191919", "samantha1", "sponge", 
                "abraham", "ilovemyself", "guillermo", "groovy", "cheeky", "swordfish", "kevin1", "dragon1", "blahblah", "babyboy1", "granny", 
                "bintang", "harmony", "wrestling", "poopie", "green1", "cheryl", "alfonso", "nathan1", "dragonfly", "yourock", "ragnarok", 
                "jazmine", "bonbon", "carlo", "theone", "serena", "rock", "you", "manunited", "iloveboys", "blacky", "karlita", "bogdan", 
                "mikey", "love69", "jillian", "eclipse", "catalin", "punkrock", "mollie", "bugsbunny", "patrick1", "supergirl", "melisa", 
                "lilwayne", "miracle", "alianza", "warrior", "christy", "harley1", "jennifer1", "hollie", "violeta", "puppylove",
                "munchkin", "fender", "moreno", "maureen", "makayla", "emilio", "brother", "ilovechris", "gymnastics", "helpme", 
                "doggie", "bailey1", "milkshake", "racheal", "rachael", "goodgirl", "athena", "kenzie", "john316", "blabla", 
                "mathew", "virgin", "159951", "juanita", "juan", "ingeras", "pepper1", "kevin786921", "mckenzie", "katkat", 
                "caramel", "heyhey", "estrela", "steven1", "kenny", "love14", "holly", "estefania", "bullet", "manuela", "baseball" ]


leetspeak_map = {
    'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7'
}

# Function to generate random words
def generate_random_words(num_words, word_length):
    words = []
    for _ in range(num_words):
        word = ''.join(random.choices(string.ascii_lowercase, k=word_length))
        words.append(word)
    return words

# Function to generate random numbers
def generate_random_numbers(num_numbers, number_length):
    numbers = []
    for _ in range(num_numbers):
        number = ''.join(random.choices(string.digits, k=number_length))
        numbers.append(number)
    return numbers

# Function to generate random special characters
def generate_random_special_chars(num_chars):
    special_chars = string.punctuation
    return random.sample(special_chars, num_chars)

# Function to generate leetspeak variations
def generate_leetspeak(word):
    leetspeak_variations = set()
    # Generate all possible combinations of leetspeak
    combinations = itertools.product(*[leetspeak_map.get(c, c) for c in word])
    for combination in combinations:
        leetspeak_variations.add(''.join(combination))
    return leetspeak_variations

# Generate random data
num_base_words = 10
num_prefixes = 5
num_suffixes = 5
num_numbers = 5
num_special_chars = 5

base_words = generate_random_words(num_base_words, 8) + common_words
prefixes = generate_random_words(num_prefixes, 3)
suffixes = generate_random_words(num_suffixes, 3)
numbers = generate_random_numbers(num_numbers, 2)
special_chars = generate_random_special_chars(num_special_chars)

def generate_wordlist(base_words, suffixes, prefixes, numbers, special_chars):
    wordlist = set()
    
    # Combine base words with prefixes and suffixes
    for base_word in base_words:
        for prefix in prefixes:
            for suffix in suffixes:
                wordlist.add(f"{prefix}{base_word}{suffix}")

    # Add numbers and special characters to the combinations
    for base in list(wordlist):
        for number in numbers:
            wordlist.add(f"{base}{number}")
            for special in special_chars:
                wordlist.add(f"{base}{number}{special}")
                wordlist.add(f"{special}{base}{number}")
                wordlist.add(f"{number}{base}{special}")

    # Add original base words with numbers and special characters
    for base_word in base_words:
        for number in numbers:
            wordlist.add(f"{base_word}{number}")
            for special in special_chars:
                wordlist.add(f"{base_word}{number}{special}")
                wordlist.add(f"{special}{base_word}{number}")
                wordlist.add(f"{number}{base_word}{special}")

    # Add leetspeak variations
    for base_word in base_words:
        leetspeak_variations = generate_leetspeak(base_word)
        for variation in leetspeak_variations:
            wordlist.add(variation)
            for number in numbers:
                wordlist.add(f"{variation}{number}")
                for special in special_chars:
                    wordlist.add(f"{variation}{number}{special}")
                    wordlist.add(f"{special}{variation}{number}")
                    wordlist.add(f"{number}{variation}{special}")

    return wordlist

def save_wordlist(wordlist, filename):
    with open(filename, 'w') as f:
        for word in wordlist:
            f.write(f"{word}\n")

def main():
    wordlist = generate_wordlist(base_words, suffixes, prefixes, numbers, special_chars)
    filename = "generated_wordlist2.txt"
    save_wordlist(wordlist, filename)
    print(f"Wordlist generated and saved to {filename}")

if __name__ == "__main__":
    main()
