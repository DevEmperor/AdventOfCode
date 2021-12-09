with open("text_04.txt") as file:
    data = file.readlines()

print(sum(all(passphrase.split().count(word) == 1 for word in passphrase.split()) for passphrase in data))

print(sum(all(sum(sorted(word) == sorted(cmpr) for cmpr in passphrase.split()) == 1 for word in passphrase.split())
          for passphrase in data))
