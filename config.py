# Tokens in a phrase
PHRASE_LENGTH = 10

# Text file to pull weights from
TEXT_FILE = "gatsby.txt"

# Pickle file to drop weights in
WEIGHTS_FILE = "weights.pkl"

# Number of tokens to predict
PREDICT_LENGTH = 100

# What the markov chain starts with
PREDICT_PREDICATE = "Once there was a"

# parses a line of text into tokens
def parse_line(line: str) -> list[hash]:
  return list(line)

# displays a list of tokens in the final format
def tokens_display(tokens: list[hash]) -> str:
  return "".join(tokens)
