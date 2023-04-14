#!/usr/bin/env python3

with open('nouns.txt', 'r') as file1, open('city_names.txt', 'r') as file2:
    words1 = [word.strip().replace(' ', '') for word in file1]
    words2 = [word.lower().strip().replace(' ', '') for word in file2]

with open('tv_shows.csv', 'r') as input_file, open('combined_cities_nouns.txt', 'w') as output_file:
  for i, word1 in enumerate(words1):
      for j, word2 in enumerate(words2):
          for k in range(100):
              combined_word = word1 + word2 + f"{k:02d}"
              output_file.write(combined_word + "\n")              
