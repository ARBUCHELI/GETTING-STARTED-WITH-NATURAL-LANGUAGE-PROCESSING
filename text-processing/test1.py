load_file_in_context("script.py")

try:
  if "went" in normalized:
    fail_tests("Did you change `stem()` to `lemmatize()`?")
except Exception as e:
  fail_tests(e)
  
pass_tests()