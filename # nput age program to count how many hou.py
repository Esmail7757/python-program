# nput age program to count how many hours days yeas and months week minutes and seconds you lived
age = int(input("what\'s your age?").strip())
print(age)
print(type(age))
# Get age in all time unites
months = age*12
weeks = months*4
days = age*365
hours = days*24
minutes = hours*60
seconds = minutes*60

print("you lived for:")
print(f"{mpnths} months")
print(f"{weeks:,} Weeks")
print(f"{days:,} days")
print(f"{hours:,} months")
print(f"{minutes:,} months")
print(f"{seconds:,} months")
