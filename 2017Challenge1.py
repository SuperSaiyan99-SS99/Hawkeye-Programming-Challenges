'''
Image Compression
'''

def compress_image(uncompressed_image):

    # Unpack input
    # Don't really care about the number of rows,
    # we'll figure it out when looping over them anyway
    _, num_columns, *rows = uncompressed_image.split('\n')
    
    for row in rows:
        occurence = 0
        current_char = row[0]
        output = ''
        
        for i in range(int(num_columns)):
            if row[i] == current_char:
                occurence += 1
            else:
                output += '{}{}'.format(occurence, current_char)
                occurence = 1
                current_char = row[i]

        # Add last one we were counting when loop ended
        output += '{}{}'.format(occurence, current_char)
            
        print(output)
        
sample_input_0 = '''2
46
BBBBBBBBBBBBBBBBSSSSSSSSBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBBBBBWWWWWWWWWBBBBBBBBBB'''
compress_image(sample_input_0)
