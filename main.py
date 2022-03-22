from data_cleaning import clean_data
from calculator import Calculate

def main():
    user_input = list(input('Please input a calculation you want: '))
    clean_data(user_input)

    def main_calculator():
        run_calculator = Calculate()
        for answer in run_calculator.calculation(user_input):
            return f'The solution to the inputed calculation is: {answer}'
    
    print(main_calculator())

if __name__ == '__main__':
    main()