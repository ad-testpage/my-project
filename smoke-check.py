import sys
import os

# ANSI escape kode za barve
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"


# Preveri, ali datoteka index.html obstaja
if not os.path.isfile("index.html"):
    print(f"{RED}index.html missing{RESET}")
    sys.exit(1)
else:
    print(f"{GREEN}index.html obstaja{RESET}")


# Preveri osnovne HTML tage
try:
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read().lower()  # pretvori vsebino v male črke

    tags = ["<html", "<head", "<body"]
    all_found = True

    for tag in tags:
        if tag in content:
            print(f"{GREEN}{tag} obstaja{RESET}")
        else:
            print(f"{RED}{tag} ne obstaja{RESET}")
            all_found = False

except Exception as e:
    print(f"{RED}Napaka pri branju datoteke: {e}{RESET}")
    sys.exit(1)

# --------------------------

if all_found:
    print(f"{GREEN}smoke OK: vsi osnovni HTML tagi prisotni{RESET}")
    sys.exit(0)
else:
    print(f"{RED}smoke FAIL: manjkajo nekateri osnovni HTML tagi{RESET}")
    sys.exit(1)