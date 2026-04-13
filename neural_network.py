import numpy as np

class NeuralNetwork:
    def __init__(self):
        self.w1 = np.random.randn(5, 8)
        self.w2 = np.random.randn(8, 1)

    def forward(self, inputs):
        x = np.array(inputs)
        x = np.dot(x, self.w1)
        x = np.tanh(x)
        x = np.dot(x, self.w2)
        return x[0]

    def mutate(self, rate):
        self.w1 += np.random.randn(5, 8) * rate
        self.w2 += np.random.randn(8, 1) * rate