from functions import add_three, divide_by_two, square


def main(x=42):
    """Main function."""
    answer = square(x)
    answer = divide_by_two(answer)
    answer = add_three(answer)
    return answer


if __name__ == "__main__":
    num = main()
    print(num)
