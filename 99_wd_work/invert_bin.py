with open("ccb7_rid_77.bin", "rb") as binary_file:
    # Read the whole file at once
    data = binary_file.read()
    print(~data)