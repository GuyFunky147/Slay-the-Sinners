def typewriter(text, speed=0.05):
    
    for character in text:
        
        print(character, end="", flush=True)
        
        time.sleep(speed)

    print()

def say(speaker, text):
    typewriter(f"\n{speaker}:")
    typewriter(text)


def choice(speaker, text, *options):
    typewriter(f"\n{speaker}:")
    typewriter(text)

    for i, option in enumerate(options, 1):
        typewriter(f"({i}) {option}")
    while True:
        answer = input("> ")

        if answer.isdigit():
            index = int(answer)

            if 1 <= index <= len(options):
                return options[index - 1]