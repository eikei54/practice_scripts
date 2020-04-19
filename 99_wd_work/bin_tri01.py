import struct

def main():
    with open("data", "wb") as fout:
        for x in [0xFF, 0x12, 0x89]:
            fout.write(struct.pack("B", x))

if __name__ == "__main__":
    main()

