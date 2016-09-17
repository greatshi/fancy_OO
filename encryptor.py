import zlib
from Crypto.PublicKey import RSA
from  Crypto.Cipher import PKCS1_OAEP

public_key = b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAydwyQGmN1vClcXTlA2VdUuYEqYJkHnLhcW/pWYh5b9grkXs2tdmZ0X9n4ivpiGfMmpRpe2/dJe0vfRtCJyUTKwkEA77joeAVX6Ef8gV4/ZVojhtnNxtkMnVJbVub+PZVzTT6uGIO+RdkxyEG0wFnDl8KCNxUHWeBSbEbBsHkY3zXoDjIAjXvNvCeGsE5pddBgKbziYe7qJWVIQh1/nmPEBQ5Pf0vxs3Zhad/s9YJx12nL3zLd1cIbP/0nx9tbvkNqFLxYA+LMhTxExenyc3UVSEEO/2DMMUyY1NWUCo1ZDOYZsnk/rbwKeVZ5LjqvgK42QVGJ0Ec5V+EFXma/gt0kQIDAQAB\n-----END PUBLIC KEY-----'



plaintext = "HaHa!"

chunk_size = 256
print "Compressing: %d bytes" % len(plaintext)
plaintext = zlib.compress(plaintext)
print "Encrypting %d bytes" % len(plaintext)

rsakey = RSA.importKey(public_key)
rsakey = PKCS1_OAEP.new(rsakey)

encrypted = ""
offset = 0

while offset < len(plaintext):

    chunk = plaintext[offset:offset+chunk_size]

    if len(chunk) % chunk_size != 0:
        chunk += b'' * (chunk_size - len(chunk))

    encrypted += rsakey.encrypt(chunk)
    offset    += chunk_size

encrypted = encrypted.encode("base64")
print "Base64 encoded crypto: %d" % len(encrypted)

print encrypted
