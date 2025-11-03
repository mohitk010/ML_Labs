import logging


# SECTION 1 & 2: Import and Basic Configuration


# Configure logging to write to both console and file
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('calculator.log'),
        logging.StreamHandler()
    ]
)



# Create a custom logger for the calculator
logger = logging.getLogger("Calculator")


# CALCULATOR FUNCTIONS


def add(a, b):
    """Add two numbers"""
    logger.debug(f"add() called with arguments: a={a}, b={b}")
    result = a + b
    logger.info(f"Addition: {a} + {b} = {result}")
    return result


def subtract(a, b):
    """Subtract two numbers"""
    logger.debug(f"subtract() called with arguments: a={a}, b={b}")
    result = a - b
    logger.info(f"Subtraction: {a} - {b} = {result}")
    return result


def multiply(a, b):
    """Multiply two numbers"""
    logger.debug(f"multiply() called with arguments: a={a}, b={b}")
    result = a * b
    logger.info(f"Multiplication: {a} × {b} = {result}")
    return result


def divide(a, b):
    """Divide two numbers"""
    logger.debug(f"divide() called with arguments: a={a}, b={b}")
    
    # ============================================
    # SECTION 5: Logging Exceptions
    # (Building on your notebook section 5)
    # ============================================
    
    try:
        if b == 0:
            logger.warning(f"Division by zero attempted: {a} / {b}")
            raise ZeroDivisionError("Cannot divide by zero!")
        
        result = a / b
        logger.info(f"Division: {a} ÷ {b} = {result}")
        return result
    
    except ZeroDivisionError:
        logger.exception("An error occurred during division")
        return None


def power(a, b):
    """Raise a to the power of b"""
    logger.debug(f"power() called with arguments: a={a}, b={b}")
    
    try:
        result = a ** b
        logger.info(f"Power: {a} ^ {b} = {result}")
        return result
    
    except OverflowError:
        logger.error(f"Overflow error: {a} ^ {b} is too large to calculate")
        logger.exception("Exception details:")
        return None


def square_root(a):
    """Calculate square root of a number"""
    logger.debug(f"square_root() called with argument: a={a}")
    
    try:
        if a < 0:
            logger.warning(f"Attempted square root of negative number: {a}")
            raise ValueError("Cannot calculate square root of negative number!")
        
        result = a ** 0.5
        logger.info(f"Square root: √{a} = {result}")
        return result
    
    except ValueError:
        logger.exception("An error occurred during square root calculation")
        return None



def display_menu():
    """Display calculator menu"""
    print("\n" + "="*50)
    print("          CALCULATOR APP WITH LOGGING")
    print("="*50)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Exit")
    print("="*50)


def get_number(prompt):
    """Get a number from user with error handling"""
    while True:
        try:
            value = float(input(prompt))
            logger.debug(f"User entered valid number: {value}")
            return value
        except ValueError:
            logger.warning("Invalid input received - not a number")
            print("❌ Invalid input! Please enter a valid number.")


def run_calculator():
    """Main calculator loop"""
    
    
    logger.info("="*50)
    logger.info("Calculator application started")
    logger.info("="*50)
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-7): ")
            logger.debug(f"User selected option: {choice}")
            
            if choice == '7':
                logger.info("User requested to exit")
                logger.info("Calculator application stopped")
                logger.info("="*50)
                print("\n👋 Thank you for using the calculator!")
                print(f"📝 Check 'calculator.log' for detailed operation history.")
                break
            
            elif choice in ['1', '2', '3', '4', '5']:
                # Operations requiring two numbers
                num1 = get_number("Enter first number: ")
                num2 = get_number("Enter second number: ")
                
                if choice == '1':
                    result = add(num1, num2)
                elif choice == '2':
                    result = subtract(num1, num2)
                elif choice == '3':
                    result = multiply(num1, num2)
                elif choice == '4':
                    result = divide(num1, num2)
                elif choice == '5':
                    result = power(num1, num2)
                
                if result is not None:
                    print(f"\n✅ Result: {result}")
                else:
                    print(f"\n❌ Operation failed. Check logs for details.")
            
            elif choice == '6':
                # Square root requires one number
                num = get_number("Enter number: ")
                result = square_root(num)
                
                if result is not None:
                    print(f"\n✅ Result: {result}")
                else:
                    print(f"\n❌ Operation failed. Check logs for details.")
            
            else:
                logger.warning(f"Invalid menu choice: {choice}")
                print("\n❌ Invalid choice! Please select 1-7.")
        
        except KeyboardInterrupt:
            logger.warning("Calculator interrupted by user (Ctrl+C)")
            print("\n\n⚠️  Calculator interrupted!")
            logger.info("Calculator application stopped abruptly")
            break
        
        except Exception as e:
            logger.critical(f"Unexpected error occurred: {str(e)}")
            logger.exception("Critical exception details:")
            print(f"\n❌ An unexpected error occurred: {e}")



if __name__ == "__main__":
    run_calculator()