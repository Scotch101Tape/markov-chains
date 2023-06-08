import pickle
import config

text_file = open(config.TEXT_FILE, "r", encoding="utf-8")

counter = {}

current_phrase = []
for line in text_file.readlines():
  tokens = config.parse_line(line)

  for token in tokens:
    phrase = tuple(current_phrase)
    if phrase not in counter:
      counter[phrase] = {}
    if token not in counter[phrase]:
      counter[phrase][token] = 0
    counter[phrase][token] += 1

    current_phrase.append(token)
    if len(current_phrase) > config.PHRASE_LENGTH:
      current_phrase.pop(0)

weights = {}
for current_phrase, words in counter.items():
  weights[current_phrase] = {}
  total = sum(words.values())
  for word, count in words.items():
    weights[current_phrase][word] = count / total

with open(config.WEIGHTS_FILE, "wb") as weights_file:
  pickle.dump(weights, weights_file)
