# aKountable
![aKountable](https://img.shields.io/badge/aKountable-True-brightgreen.svg)  

Safe, accountable AI in the Blockchain!  
by [saferAI](http://www.saferai.com)

## Installation
```bash
pip install aKountable
```

## Usage
First, say STOP! to people cheating on AI audits.

Start getting [Tierion](https://tierion.com) credentials for free. You will need a username, password and [api keys](https://tierion.com/docs/dataapi). This is what we use to talk with the Blockchain.

Create a [Keras](https://keras.io) model and an aKountable object
```python
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,)))
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(10, activation='softmax'))

aK = aKountable(model, username, password, api_key)
aK.model.summary()
aK.model.compile(loss='categorical_crossentropy',
                 optimizer=RMSprop(),
                 metrics=['accuracy'])
```

Train your model to solve hard AI problems

```python
history = aK.model.fit(x_train, y_train,
                       batch_size=batch_size,
                       epochs=epochs,
                       verbose=1,
                       validation_data=(x_test, y_test))
```

Stamp your model using the Blockchain and get a receipt
```python
aK.stamp()
aK.receipt()
```

Be **aKountable**!
```python
aK.validate()
```

If successful, get yourself [saferAI](http://www.saferai.com) **aKountable** badge! See full example [here]('https://github.com/safer41/aKountable/tree/master/examples/Hello\ World\ Peace!.ipynb').

## Documentation
[CisD]('https://github.com/safer41/aKountable/blob/master/aKountable/aKountable.py')

## ToDO
* Add functionality to save **aKountable** receipt together with Keras model
* Use `logging` instead of `print`.
* Extend **aKountable**. For all AI, Machine Learning and Neural Network library, add model description AND model weights to a hash and use an API that can talk with the Blockchain.
* aKountable as a Service: aKaaS
* Work with regulators to make bring **aKountable** and safer AI to everyone.
