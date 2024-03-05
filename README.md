Problems faced:

1. Unable to run tf-encrypted package in python which can be used to train ml models on encrypted data
Reason: tf-encrypted library works on tensorflow==2.9.1 version, and I can't install tensorflow 2.9.1 due to denial from the system (System error)

2. Encrypted iris dataset in Untitled.ipynb but I'm unable to load the dataset into json file or any other file (joblib or txt)


Status so far:
In Untitled.ipynb, I encrypted a list using tenseal library and I stored the encrypted list in demo_encrypted_objects. After that I fetched the same encrypted list and decrypted in receiver.ipynb

After this, I encrypted iris dataset, but I'm unable to load the encrypted data into any other file (file such as .json or .joblib or .txt)

Trained a Logistic Regression model using encrypted data (tested with plain data)
