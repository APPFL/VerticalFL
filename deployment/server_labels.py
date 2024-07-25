import torch
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

def get_labels():
    # Load the diabetes dataset
    diabetes = load_diabetes()
    X = diabetes.data
    y = diabetes.target 

    # Split the data into training and testing sets
    y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)[2:]

    y_train = torch.tensor(y_train, dtype=torch.float32).unsqueeze(1)
    y_test = torch.tensor(y_test, dtype=torch.float32).unsqueeze(1)
    return y_train, y_test