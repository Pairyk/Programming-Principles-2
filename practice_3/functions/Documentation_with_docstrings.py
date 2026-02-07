# Example 1: Simple one-line docstring
def square(n):
    """Return the square of a number."""
    return n ** 2

print(f"square(5) = {square(5)}")
print(f"Docstring: {square.__doc__}")


# Example 2: Multi-line docstring with description
def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI).
    
    BMI is calculated as weight (kg) divided by height (m) squared.
    """
    return weight / (height ** 2)

print(f"BMI: {calculate_bmi(70, 1.75):.2f}")
print(f"Docstring:\n{calculate_bmi.__doc__}")


# Example 3: Docstring with parameters and return value
def find_max(numbers):
    """
    Find the maximum value in a list.
    
    Parameters:
        numbers (list): List of numeric values
    
    Returns:
        int/float: The maximum value in the list
    """
    return max(numbers)

print(f"Max of [1,5,3,9,2]: {find_max([1,5,3,9,2])}")


# Example 4: Google-style docstring
def convert_temperature(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature in Fahrenheit
    
    Examples:
        >>> convert_temperature(0)
        32.0
        >>> convert_temperature(100)
        212.0
    """
    return (celsius * 9/5) + 32

print(f"0°C = {convert_temperature(0)}°F")
print(f"100°C = {convert_temperature(100)}°F")


# Example 5: NumPy-style docstring
def calculate_distance(x1, y1, x2, y2):
    """
    Calculate Euclidean distance between two points.
    
    Parameters
    ----------
    x1 : float
        X coordinate of first point
    y1 : float
        Y coordinate of first point
    x2 : float
        X coordinate of second point
    y2 : float
        Y coordinate of second point
    
    Returns
    -------
    float
        Distance between the two points
    """
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

distance = calculate_distance(0, 0, 3, 4)
print(f"Distance from (0,0) to (3,4): {distance}")


# Example 6: Accessing docstrings with help()
def complex_function(data, threshold=0.5, verbose=False):
    """
    Process data with configurable threshold.
    
    This function demonstrates how to write comprehensive
    documentation for complex functions.
    
    Parameters:
        data (list): Input data to process
        threshold (float, optional): Filtering threshold. Default is 0.5
        verbose (bool, optional): Print detailed output. Default is False
    
    Returns:
        list: Filtered data above threshold
    
    Raises:
        ValueError: If threshold is not between 0 and 1
    """
    if not 0 <= threshold <= 1:
        raise ValueError("Threshold must be between 0 and 1")
    
    result = [x for x in data if x > threshold]
    
    if verbose:
        print(f"Filtered {len(data)} items to {len(result)} items")
    
    return result

result = complex_function([0.3, 0.7, 0.9, 0.2, 0.8], threshold=0.5, verbose=True)
print(f"Result: {result}")
print("\nUse help(complex_function) to see full documentation")


# Example 7: Docstring best practices summary
def best_practice_example(param1, param2, optional_param=None):
    """
    Brief one-line summary of what the function does.
    
    More detailed explanation can go here. Explain the purpose,
    any important algorithms, or special considerations.
    
    Parameters:
        param1 (type): Description of first parameter
        param2 (type): Description of second parameter
        optional_param (type, optional): Description. Defaults to None.
    
    Returns:
        type: Description of return value
    
    Raises:
        ExceptionType: When this exception occurs
    
    Examples:
        >>> best_practice_example(1, 2)
        Expected output
    
    Note:
        Any additional notes or warnings
    """
    pass

print("Check the source code for docstring template")
print(best_practice_example.__doc__)
