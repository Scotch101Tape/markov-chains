import pickle
import random
import config
import sys

with open(config.WEIGHTS_FILE, 'rb') as weights_file:
  weights = pickle.load(weights_file)

  predicate_tokens = config.parse_line(config.PREDICT_PREDICATE)
  predicate_phrase = tuple(predicate_tokens[-config.PHRASE_LENGTH:])
  predicted_tokens = None
  if predicate_phrase in weights:
    predicted_tokens = predicate_tokens
  else:
    print("WARNING: PREDICT_PREDICATE did not match any weights, choosing a random predicate instead.", file=sys.stderr)
    random_phrase = random.choice(list(weights.keys()))
    predicted_tokens = list(random_phrase)

  for _ in range(config.PREDICT_LENGTH):
    phrase = tuple(predicted_tokens[-config.PHRASE_LENGTH:])

    next_tokens = weights[phrase]
    random_number = random.uniform(0,1)
    for token, weight in next_tokens.items():
      random_number -= weight
      if random_number <= 0:
        predicted_tokens.append(token)
        break

print(config.tokens_display(predicted_tokens))
