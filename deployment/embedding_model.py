import torch

class DiabetesClientEmbeddingModel(torch.nn.Module):
    """
    Embedding model for the VFL clients.
    """
    def __init__(self, input_dim, output_dim=8, hidden_dim=24):
        super(DiabetesClientEmbeddingModel, self).__init__()
        self.fc1 = torch.nn.Linear(input_dim, hidden_dim)
        self.fc2 = torch.nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return x