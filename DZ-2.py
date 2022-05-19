# Задание №2

with open('test_1.txt', 'w+') as test_file:
    content = ["I've seen things you people wouldn't believe...\nAttack ships on fire off the shoulder of Orion...\nI watched C-beams glitter in the dark near the Tannhäuser Gate.\nAll those moments will be lost in time, like tears in rain...\nTime to die.\n"]
    test_file.writelines(content)
    test_file.seek(0)

    lines = 0
    words = 0
    for line in test_file:
        lines += 1
        words += len(line.split())
        print(line)
    print(f'Lines: {lines}')
    print(f'Words: {words}')