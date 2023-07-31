import json

while True:
    username = input('What is your name?')
    if username == 'quit':
        print('Bye!')
        break
    else:
        filename = 'username.json'
        try:
            with open(filename, encoding='utf-8') as f:
                contents = f.read()
        except FileNotFoundError:
            print('File is not found!')
            with open(filename, 'a') as f:
                f.write(username + '\n')
        else:
            l: list[str] = contents.split('\"')
            if username in l:
                print(f'Welcome back {username}!')
            else:
                with open(filename, 'a') as f:
                    json.dump(username, f, )
                    f.write('\n')
                print(f'We\'ll remember you when you come back,{username}!')
