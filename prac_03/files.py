# Question 1

out_file = open("name.txt", "w")
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

# Question 2

in_file = open("name.txt")
name_from_file = in_file.read().strip()
print(f"Hi {name_from_file}!")
in_file.close()
