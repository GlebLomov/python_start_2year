file_name = "quotes.txt"
with open ("quotes.txt","r",encoding = "UTF-8") as file:
    for line in file:
        print(line)

pon = input("Хто соченил?")
with open ("quotes.txt","a",encoding = "UTF-8") as file:
    file.write(f"({pon})\n")

while True:
    pin = input ("Додайте цитату(так/ні)")
    pin = pin.lower()
    if pin == "так":
        pon = input("Ведіть цитату:")
        pin = input("Ведіть автора")
        file = open(file_name, "a" , encoding = "UTF-8")
        file.write(f"{pon}\n({pin})\n")
    else:
        break

with open(file_name,"r",encoding = "UTF-8") as file:
    for line in file:
        print(line)