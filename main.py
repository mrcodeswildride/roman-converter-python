print()

numeral = input("Enter a Roman numeral: ").upper()

rom_to_dec = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

while numeral == "" or any(letter not in rom_to_dec for letter in numeral):
  print("Invalid input.\n")
  numeral = input("Enter a Roman numeral: ").upper()

decimal = 0
i = 0

while i < len(numeral):
  letter = numeral[i]
  value = rom_to_dec[letter]

  if i + 1 < len(numeral):
    next_letter = numeral[i + 1]
    next_value = rom_to_dec[next_letter]
  else:
    next_value = None

  if next_value is None or value >= next_value:
    decimal += value
    i += 1
  else:
    decimal += next_value - value
    i += 2

print(f"\n{numeral} = {decimal}")
