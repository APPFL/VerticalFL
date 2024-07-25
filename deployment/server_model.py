import torch
class DiabetesServerModel(torch.nn.Module):
    """
    Model for the VFL server.
    """
    def __init__(self, input_dim, output_dim=1, hidden_dim=12):
        super(DiabetesServerModel, self).__init__()
        self.fc1 = torch.nn.Linear(input_dim, hidden_dim)
        self.fc2 = torch.nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x