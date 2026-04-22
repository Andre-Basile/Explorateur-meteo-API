from datetime import datetime
import locale
import time
locale.setlocale(locale.LC_TIME,'French_France')

print(datetime.now())

print(datetime.now().strftime("%A %d %B %Y à %H:%M").capitalize())

#fonction d'attente de <duration> secondes(un float)
def wait(duration):
    start = round(time.time(),1)
    while(round(time.time(),1) - start <= duration):
        pass
    


print("debut de test")
for i in range(20):
    print(i)
    wait(0.5)
print("fin de test")
wait(5)
print(round(time.time()))

for i in range(101):
    barre = "#" * (i//2)
    print(f"\r[{barre:<50}] {i}%",end="")
    time.sleep(0.03)
print()