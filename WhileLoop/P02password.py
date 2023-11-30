username = input()
password = input()

input_data = input()

while input_data != password:
    input_data = input()
print(f'Welcome {username}!')
