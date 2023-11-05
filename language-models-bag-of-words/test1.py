load_file_in_context("script.py")

bow = Counter(normalized)

try:
  if bow != bag_of_looking_glass_words:
    fail_tests("Did you set `bag_of_looking_glass_words` equal to `Counter(normalized)`?")
except NameError:
  fail_tests("Did you define `bag_of_looking_glass_words`?")

pass_tests()