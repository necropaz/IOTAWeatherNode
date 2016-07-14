# IOTA Weather Node

The IOTA Weather Node is a Weather Node built with a [Raspberry Pi](https://www.raspberrypi.org/) and the add-on board  [Sense HAT](https://www.raspberrypi.org/products/sense-hat/).
The Weather Node send and receive Data over the new [IOTA Protocol](https://www.iotatoken.com/).

requirements:

- [Raspberry Pi](https://www.raspberrypi.org/)
- microSD card with installed [Ubuntu MATE 16.04 LTS](https://ubuntu-mate.org/download/)
- Raspberry Pi [Sense HAT](https://www.raspberrypi.org/products/sense-hat/)
- [IOTA Node](https://github.com/IOTAledger/iota-gui-beta/releases)

## IOTA Weather Node

The IOTA Weather Node waiting until a client send a transaction with >0 IOTAs and a message.
With the message the client tell the node what is his request and an address on which the node can send his answer.
So can be send a command is arrived over the IOTA Protocol.
After this he read the Weather info from the Sense HAT and send them back or just show a promotion on his 8x8 LED Matrix.

### Installation:

For a step by step tutorial go to necropaz.github.io (will follow later)

## IOTA Weather Client

### Installation:

For a step by step tutorial go to necropaz.github.io (will follow later)

## Python package functions

### `sendMessage(seed, address, message, value)`

Send a message to a specified Adress.

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`seed` | string | Yes | 81-char encoded string which contains the accounts seed. The seed must be correctly encoded: only uppercase latin letters and 9’s. No other characters are allowed.
`input` |`address` | string | Yes | 81-char long address of the recipient of a transaction.
`input` |`message` | string | Yes | The message which added to the transation.
`input` |`value` | string | Yes | string the quantity of IOTA’s which should be transferred.

### `sendRequest(command)`

Send a request to the IOTA Node and return the andswer.

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`command` | string | Yes | The command which will made the request.
`return` |`jsonData` | string | Yes | The answer from the request in JSON.

### `searchNewTransaction(address)`

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`address` | string | Yes | 81-char long address of the recipient of a transaction.
`return` |`transaction` | string | Yes | Hash of the last transaction.

### `readSendersAddress(transaction)`

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`transaction` | string | Yes | Hash of the transaction from which you wanna read the sender address.
`return` |`address` | string | Yes | Sender address of the transaction.

### `getNewTransfer(seed)`

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`seed` | string | Yes | 81-char encoded string which contains the accounts seed. The seed must be correctly encoded: only uppercase latin letters and 9’s. No other characters are allowed.
`return` |`transaction` | string | Yes | Hash of the last transaction.

### `searchMessage(transaction)`


Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`transaction` | string | Yes | Hash of the transaction which include the message.
`return` |`message` | string | Yes | The message which is encoded in Trytes.

### `byteToTryte(char)`

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`char` | char | Yes | ASCII Character which will encoded to a Tryte.
`return` |`tryte` | char | Yes | The encoded character as tryte.

### `tryteToByte(char1,char2)`

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`char1` | char | Yes | First Tryte Character.
`input` |`char2` | char | Yes | Second Tryte Character.
`return` |`byte` | char | Yes | The decoded Byte as ASCII character.

### `messageEncode(message)`

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`message` | string | Yes | Message which will be encoded to tyrtes.
`return` |`trytes` | string | Yes | The encoded message in trytes

### `messageDecode(trytes)`

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`trytes` | string | Yes | Trytes which will be decoded to ASCII characters.
`return` |`message` | string | Yes | The decoded Message.
