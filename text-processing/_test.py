load_file_in_context("script.py")

try:
  if "went" in lemmatized:
    fail_tests("Did you give `lemmatize()` a second argument of `get_part_of_speech(token)`?")
except Exception as e:
  fail_tests(e)
  
pass_tests()