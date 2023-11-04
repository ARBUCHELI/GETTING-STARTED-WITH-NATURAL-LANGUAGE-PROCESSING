load_file_in_context("script.py")

try:
  if my_sentence == "Your sentence goes here!":
    fail_tests("Give `my_sentence` a new value!")
except Exception as e:
  fail_tests(e)

pass_tests()