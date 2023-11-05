load_file_in_context("script.py")

try:
  if edit_distance(three_away_from_code, "code") != 3:
    fail_tests("Assign `three_away_from_code` a word that has a Levenshtein distance of `3` from `'code'`.")
  elif edit_distance(two_away_from_chunk, "chunk") != 2:
    fail_tests("Assign `two_away_from_chunk` a word that has a Levenshtein distance of `2` from `'chunk'`.")
except Exception as e:
  fail_tests(e)
  
pass_tests()