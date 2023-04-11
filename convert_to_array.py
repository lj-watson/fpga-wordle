from lib2to3.pytree import convert


def convert_to_array(words: list[str]) -> None:
  """
  Takes in a list of uppercase words and converts them to a format that can be inserted into
  a C array

  Used to create a word bank

  Input: words -> a list of uppercase strings
  """
  words_lowercase = ['"' + word.lower() + '"' for word in words]
  result = ", ".join(words_lowercase)

  print(result)


words = ["AARGH", "HUNTS", "FLAKE", "FLOAT", "NIGHT", "CLOTH"]
convert_to_array(words)

# prints "aargh", "hunts", "flake", "float", "night", "cloth"
