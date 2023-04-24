import torch

x = torch.tensor([1., 2., 3.])  # Create a tensor
print(x)  # Tensor [1. 2. 3.]

# Construct a 5 * 3 matrix
x = torch.rand(5, 3)

# Addition
y = torch.rand(5, 3)
z = x + y

# Define a network
import torch.nn as nn
model = nn.Sequential(nn.Linear(3, 2))

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc = nn.Linear(3, 2)  # 3 inputs, 2 outputs
        
    def forward(self, x):
        x = self.fc(x)
        return F.softmax(x, dim=1)

# Define an optimizer and loss function
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
criterion = nn.CrossEntropyLoss()

# Train the network
for epoch in range(100):
    optimizer.zero_grad()  # Zero grad
    inputs = torch.rand(5, 3)  # Define model input
    outputs = model(inputs)  # Get model predictions，模型输出,批大小为5
    targets = torch.LongTensor([1, 0, 1, 1, 0])  # Define target labels，目标标签,批大小也为5
    loss = criterion(outputs, targets)  # Calculate loss
    loss.backward()  # Backpropagate
    optimizer.step() # Update weights
