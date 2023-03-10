#kidus berhanu
# Importing necessary libraries
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Helper function for training an RBM
def train_rbm(rbm, X, n_epochs, learning_rate):
    for epoch in range(1, n_epochs + 1):
        # Perform contrastive divergence to update the weights
        rbm.contrastive_divergence(X, learning_rate=learning_rate)

# Initialize the DBN with the desired architecture (number of layers and number of neurons per layer)
dbn = DBN(architecture=[784, 500, 500, 10],
          learning_rate=0.1,
          n_iter_backprop=100,
          l2_regularization=0.1,
          n_iter_pretrain=10,
          batch_size=32)

# Load the data and preprocess it
data = np.load("your_data.npy")
scaler = MinMaxScaler()
data = scaler.fit_transform(data)
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2)

# Pretrain the DBN using unsupervised learning
dbn.pretrain(X_train, n_epochs=10, batch_size=32)

# Fine-tune the DBN using supervised learning
dbn.fit(X_train, y_train)

# Make predictions on the test set
y_pred = dbn.predict(X_test)

# Print the accuracy of the DBN
print("Accuracy:", accuracy_score(y_test, y_pred))
