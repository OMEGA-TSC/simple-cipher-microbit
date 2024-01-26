
# micro:bit simple cipher
### simple cipher library for BBC micro:bit
### Current library version v1.1.1

## Classes
Library has 2 main classes `encript` and `decrypt`.

## Ciphers available
+ hex
+ caesar

## Example
```python
import simplecipher
enc = simplecipher.encript()
encrypted_text = enc.hex("Hello, World!")
print("Encrypted text:", encrypted_text)

dec = simplecipher.decrypt()
decrypted_text = dec.hex(encrypted_text)
print("Decrypted text:", decrypted_text)
```
