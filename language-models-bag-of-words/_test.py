load_file_in_context("script.py")

try:
  if text == looking_glass_text:
    fail_tests("Change `text` to something new!")
except Exception as e:
  fail_tests(e)

pass_tests()