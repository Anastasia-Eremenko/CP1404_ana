def print_heart(number):
    """Prints a custom shape."""
    print("  " * number + "00" * number + "  " * number + "00" * number )
    print(" " * number + "00000000" * number)
    print("  " * number + "000000" * number)
    print("   " * number + "0000" * number)
    print("    " * number + "00" * number)

def print_square(size):
    for i in range(size):
        print(" * " * size)

