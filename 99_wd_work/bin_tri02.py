def main():
    with open("data.bin", "wb") as fout:
        bary = bytearray([0xFF, 0x12, 0x89, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18,
            0x19, 0x20, 0x21, 0x22])
        bary.append(0)
        bary.extend([1, 127])
        bary.extend([10, 20])
        fout.write(bary)

if __name__ == "__main__":
    main()
