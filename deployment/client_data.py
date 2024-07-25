import torch
from sklearn.datasets import load_diabetes
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


def get_vfl_data(
    client_id: int,
):
    # Load the diabetes dataset
    diabetes = load_diabetes()
    X = diabetes.data
    y = diabetes.target 

    # Split the data into training and testing sets
    X_train, X_test = train_test_split(X, y, test_size=0.2, random_state=42)[:2]

    # Standardize the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Convert to PyTorch tensors
    X_train = torch.tensor(X_train, dtype=torch.float32)
    X_test = torch.tensor(X_test, dtype=torch.float32)
    
    if client_id == 0:
        return X_train[:, :3], X_test[:, :3]
    elif client_id == 1:
        return X_train[:, 3:6], X_test[:, 3:6]
    elif client_id == 2:
        return X_train[:, 6:], X_test[:, 6:]
    else:
        raise ValueError(f"Client ID {client_id} is not supported")