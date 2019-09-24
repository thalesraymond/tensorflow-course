import numpy as np

number = 2

vector = [2, 3, 5]

vector = np.asarray(vector)

vector.max()
vector.argmax()
vector.min()
vector.mean()
vector.sum()

vector_2 = number * vector

np.arange(1, 50, 0.5)

np.zeros(10)
np.zeros((3, 3))
np.ones(10)
np.ones((3, 3))

np.linspace(1, 20, 5)

np.random.seed(1)
np.random.randint(0, 101, 4)

np.random.randint(0, 101, (3, 3))
