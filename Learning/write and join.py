def write_mul_items(file, separator, *args):
    file.write(separator.join(args))

test = open("/Projects/Learning/write and join.txt", "w")

test.write('Toi la mot bai test')


