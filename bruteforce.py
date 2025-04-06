import bcrypt

wordlist=input("specify the wordlist: ")
hashfile=input("specify the hash file: ")

with open(hashfile, 'r', encoding='utf-8') as f:
    target_hash=f.readline().strip().encode()
speed=bcrypt.gensalt(rounds=6)
with open(wordlist, 'r', encoding='utf-8') as f:
    for line in f:
        word=line.strip().encode()
        if bcrypt.checkpw(word, target_hash):
            print(f"[+] KEY FOUND: {word.decode()}")
            break
        else:
            print(f"[-] ATTEMPTING: {word.decode()}")

