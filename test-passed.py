import time
from colored import fore, back, style


print (fore.LIGHT_GRAY + back.RED + style.BOLD + "Hello World !!" + style.RESET)

class signs:
    PASSED = (fore.LIGHT_GREEN + style.BOLD + "✔ Passed")
    FAILED = (fore.LIGHT_RED + style.BOLD + "✘ Failed")
    
for i in range(1,9):
    time.sleep(0.5)
    print(fore.LIGHT_GREEN, "Test", i, ": ",  signs.PASSED)

print("\n")
time.sleep(0.5)
print("\nTest finished." + style.RESET)
print(fore.LIGHT_RED + style.BOLD + "Taking-over whole universe is", signs.FAILED + style.RESET)
