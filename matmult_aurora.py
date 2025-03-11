import numpy as np
import time

start_time = time.time()

X = np.random.randint(0, 100, (250, 250))
Y = np.random.randint(0, 100, (250, 251))

result = np.dot(X, Y)

end_time = time.time()

print("Time taken: ", end_time - start_time)

print(result)