def textfile_open(file):
    # open file
    f = open(file, 'r')

    # read text data,one per line
    data = f.read().split('\n')

    # close file
    f.close()

    return data


file = 'img_url.txt'
image_data = textfile_open(file)
print(image_data)
