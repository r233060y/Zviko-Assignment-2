import pandas as pd
import matplotlib.pyplot as plt


def plot_data():
    """
    Creates a scatter plot using coordinates from a text file.

    Returns:
    - A matplotlib figure object containing the scatter plot.
    """

    # Define the path to the coordinates file
    file_path = r"C:\Users\USER\PycharmProjects\Assignment 2\x_y_coordinates.txt"

    # Read the coordinates from the text file
    try:
        data = pd.read_csv(file_path, header=None, names=['X', 'Y'], delim_whitespace=True)
    except Exception as e:
        raise ValueError(f"Error reading the file: {e}")

    # Check if the data has at least two columns
    if data.shape[1] < 2:
        raise ValueError("The input data must contain at least two columns for plotting.")

    # Extract the two columns for the scatter plot
    x = data['X']  # First column
    y = data['Y']  # Second column

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, alpha=0.7)
    plt.title('Scatter Plot of Data')
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.grid(True)

    # Show the plot
    plt.show()

    # Return the figure object
    return plt.gcf()


# Call the function to display the plot
plot_data()