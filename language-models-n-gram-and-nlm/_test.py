load_file_in_context("script.py")

try:
  if len(looking_glass_ngrams_frequency.most_common(1)[0][0]) <= 3:
    fail_tests("Did you switch the `n` argument of `ngrams()` for `looking_glass_ngrams` to a number greater than `3`?")
except Exception as e:
  fail_tests(e)

pass_tests()