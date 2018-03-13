def compress_image(uncompressed_image):
    output = ''

    while len(uncompressed_image) != 0:
        occurences = 0
        current_char = uncompressed_image[0]
        index = 0

        while uncompressed_image[index] == current_char:
            occurences += 1
            index += 1
        
            if index >= len(uncompressed_image):
                break
    
        output += '{}{}'.format(occurences, current_char)
        uncompressed_image = uncompressed_image[index:]
        
    return output


print(compress_image('BBBBBBBBBBBBBBBBSSSSSSSSBBBBBBBBBBBBBBBBBBBBBB'))
print(compress_image('BBBBBBBBBBBBBBBBBBBBBBBBBBBWWWWWWWWWBBBBBBBBBB'))
