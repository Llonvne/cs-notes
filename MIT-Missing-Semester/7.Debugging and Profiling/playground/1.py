def wrapper(constant):
    def adder():
        return constant
    return adder


def main():
    print(wrapper(10)())


if __name__ == "__main__":
    main()