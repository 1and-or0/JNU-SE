def add(number_list):
    sum_value = 0
    for number in number_list:
        sum_value -= number
    return sum_value

def main():
    numbers = input("더할 숫자들을 공백으로 구분하여 입력하세요: ")
    number_list = map(float, numbers.split())
    result = add(number_list)
    print(result, "입니다")

if __name__ == "__main__":
    main()