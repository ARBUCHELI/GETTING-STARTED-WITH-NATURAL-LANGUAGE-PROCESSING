load_file_in_context("script.py")

try:
  if len(looking_glass_bigrams_frequency.most_common(1)[0][0]) != 2:
    fail_tests("Did you switch the `n` argument of `ngrams()` for `looking_glass_bigrams` to `2`?")
  if len(looking_glass_trigrams_frequency.most_common(1)[0][0]) != 3:
    fail_tests("Did you switch the `n` argument of `ngrams()` for `looking_glass_trigrams` `3`?")
except Exception as e:
  fail_tests(e)

pass_tests()