# IOTA Weather Node

## Python package functions
***
### `sendMessage(seed, address, message, value)`


Parameters | Type | Required | Description
------------ | ------------- | ------------- | -------------
`seed` | string | Yes | 81-char encoded string which contains the accounts seed. The seed must be correctly encoded: only uppercase latin letters and 9’s. No other characters are allowed.
`address` | string | Yes | 81-char long address of the recipient of a transaction.
`message` | string | Yes | The message which added to the transation.
`value` | string | Yes | string the quantity of IOTA’s which should be transferred.

### `sendRequest(command)`

Parameters | Type | Required | Description
------------ | ------------- | ------------- | -------------
`command` | string | Yes | The command which will made the request.

### `searchNewTransaction(address)`

Parameters | Type | Required | Description
------------ | ------------- | ------------- | -------------
`address` | string | Yes | 81-char long address of the recipient of a transaction.

### `readSendersAddress(transaction)`

Parameters | Type | Required | Description
------------ | ------------- | ------------- | -------------
`transaction` | string | Yes | Hash of the transaction from which you wanna read the sender address.

### `getNewTransfer(seed)`

Parameters | Type | Required | Description
------------ | ------------- | ------------- | -------------
`seed` | string | Yes | 81-char encoded string which contains the accounts seed. The seed must be correctly encoded: only uppercase latin letters and 9’s. No other characters are allowed.


### `searchMessage(transaction)`

Parameters | Type | Required | Description
------------ | ------------- | ------------- | -------------
`transaction` | string | Yes | Hash of the transaction which include the message.

### `byteToTryte(char)`

Parameters | Type | Required | Description
------------ | ------------- | ------------- | -------------
`char` | char | Yes | ASCII Character which will encoded to a Tryte.

### `tryteToByte(char1,char2)`

Parameters | Type | Required | Description
------------ | ------------- | ------------- | -------------
`char1` | char | Yes | First Tryte Character.
`char2` | char | Yes | Second Tryte Character.

### `messageEncode(message)`

Parameters | Type | Required | Description
------------ | ------------- | ------------- | -------------
`message` | string | Yes | Message which will be encoded to tyrtes.

### `messageDecode(trytes)`

Parameters | Type | Required | Description
------------ | ------------- | ------------- | -------------
`trytes` | string | Yes | Trytes which will be decoded to ASCII characters.

***
