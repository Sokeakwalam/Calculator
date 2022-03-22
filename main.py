from calculator import Calculate

def main():
    run_calculator = Calculate()
    for answer in run_calculator.calculation():
        print(f'The solution to the inputed calculation is: {answer}')

if __name__ == '__main__':
    main()