from sys import argv

cmd_options = argv

print(argv[0])

i = 1
for cmd in cmd_options:
  print("Argument ", i, "=", cmd)
  i += 1