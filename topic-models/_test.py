load_file_in_context("script.py")

try:
  if len(stop_list) == 0:
    fail_tests("Add some words to `stop_list`!")
  elif len(stop_list) < 10:
    fail_tests("Make sure `stop_list` has at least 10 words.")
except Exception as e:
  fail_tests(e)

pass_tests()