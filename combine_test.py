#coding=utf-8

import zlib
import base64

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def create_key():
    new_key = RSA.generate(2048, e=65537)

    public_key = new_key.publickey().exportKey("PEM")
    private_key = new_key.exportKey("PEM")

    return public_key, private_key

def decryptor():
    private_key = b'-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAydwyQGmN1vClcXTlA2VdUuYEqYJkHnLhcW/pWYh5b9grkXs2tdmZ0X9n4ivpiGfMmpRpe2/dJe0vfRtCJyUTKwkEA77joeAVX6Ef8gV4/ZVojhtnNxtkMnVJbVub+PZVzTT6uGIO+RdkxyEG0wFnDl8KCNxUHWeBSbEbBsHkY3zXoDjIAjXvNvCeGsE5pddBgKbziYe7qJWVIQh1/nmPEBQ5Pf0vxs3Zhad/s9YJx12nL3zLd1cIbP/0nx9tbvkNqFLxYA+LMhTxExenyc3UVSEEO/2DMMUyY1NWUCo1ZDOYZsnk/rbwKeVZ5LjqvgK42QVGJ0Ec5V+EFXma/gt0kQIDAQABAoIBAAIefaiPcx2+iP4X7A+NEN297G6bH9HyAsveEOUPubai3lI4qOpfzm2UmNKXA2ybKlq1FCZnljq/sq/tiVQ/32OkRJaFen5Ii/DlECDKTerblq1nPD4n23VsJckwHQMQEvaEh91HqkCTLkuo3Rl5+kr8VG6jYX6th33ujgoUHwGsWQw01nqdQRN8cSv9TBnDsfX90OsdQJbN2+XpbEozciuxEAsnSdxDKCoqcYtREcDjPbFBUPfxI4ASIxK4MQAYRVOmupvLiyPmk9/8iuylTxOTIvUmLe7eYfmpwLuY6tNxzeK1tNSjIgCyF4flYwWwajpxyfoz+hXLzrPR/+UinAECgYEAz4ermOe/HXBzHBkPKKY1v7zIZlwSrERIrLcdGLqFf2fpg6RKpgZB6PCVqPE8CVY6mCdhhEiCqMQLwpWh2rF/oh2/4cPRjkWU0r5YCH47IU01CEJ/uL+g/IFzT+zXk81L+DEDOgYeNAPmCy1t1nUpWIvd0wzNPGVVGIvlKJHQVDkCgYEA+QGGOzbXrcdp6gg3/IKvASM1SF3EDeHmsW3kl3Ot+CnwwupRaqnXsBcTb2hTpmlTNwh5tNqyWUGloVil3Q1flrurhb2shg+VCgcyodRqnd1sh8Z2sL/oXJAdpSQyeUTPUSKUO/WiK9cUD3bzqvQ4qafwOQ9Oj3flBnd1TAwLExkCgYEApqfHuInaYvTLq7PABZ+8KBadQ/4KjMZlKjX+qr4WuKKk1q9Xtw3tXffd54aZ9NGHSmrNl+J28rpEy2VITgwed/y1+8I6BauBAOAUZ/We3HZY8SId2SoiSMRX6sZCtJG3wT7y3WTOWm0LDszTmNYLdu0THQn5wteJR6YIR9UY3JkCgYBH6pjKIVzJY/7DCPyigVvqCDErZWlqWQQ32nVbCJ4GPpa6tNIu7D7PLNsAIjGGroTKMDh2c3NvM/aSUvgUj/g7oJg5WD6ruXRiIRIOizr/vSPLUxaUldiWY0ksmPe67pSx6jrF1nuwDb5NeR2HEmILHeXTlQgrh4UuCPJntFK+gQKBgEjAjcgABKtU+eghe63M62R1GaVgiML959zGbK6aND1tSEDSUru0CGk+lSTkvLBE42J8XOoLghAn51jAa7Hw9f3bWJg6CJc2f5mfKNyFJOjdUVwbRN2oZHC7NQH1zeF7vU7Ldh9Rr9w/8CLK+Gy1IkNgDJaiyWtMWfw847gR5ijm\n-----END RSA PRIVATE KEY-----'

    encrypted = raw_input("要解密的: ")

    rsakey = RSA.importKey(private_key)
    rsakey = PKCS1_OAEP.new(rsakey)

    chunk_size = 256
    offset = 0
    decrypted = ""
    encrypted = base64.b64decode(encrypted)

    while offset < len(encrypted):
        decrypted += rsakey.decrypt(encrypted[offset:offset + chunk_size])
        offset += chunk_size

    plaintext = zlib.decompress(decrypted)
    print plaintext

def encryptor():

    public_key = b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAydwyQGmN1vClcXTlA2VdUuYEqYJkHnLhcW/pWYh5b9grkXs2tdmZ0X9n4ivpiGfMmpRpe2/dJe0vfRtCJyUTKwkEA77joeAVX6Ef8gV4/ZVojhtnNxtkMnVJbVub+PZVzTT6uGIO+RdkxyEG0wFnDl8KCNxUHWeBSbEbBsHkY3zXoDjIAjXvNvCeGsE5pddBgKbziYe7qJWVIQh1/nmPEBQ5Pf0vxs3Zhad/s9YJx12nL3zLd1cIbP/0nx9tbvkNqFLxYA+LMhTxExenyc3UVSEEO/2DMMUyY1NWUCo1ZDOYZsnk/rbwKeVZ5LjqvgK42QVGJ0Ec5V+EFXma/gt0kQIDAQAB\n-----END PUBLIC KEY-----'

    # plaintext = "HaHa!"
    plaintext = raw_input("要加密的：")

    chunk_size = 214

    print "Compressing: %d bytes" % len(plaintext)
    plaintext = zlib.compress(plaintext)
    print "Encrypting %d bytes" % len(plaintext)

    rsakey = RSA.importKey(public_key)
    rsakey = PKCS1_OAEP.new(rsakey)

    encrypted = ""
    offset = 0

    while offset < len(plaintext):

        chunk = plaintext[offset:offset + chunk_size]

        if len(chunk) % chunk_size != 0:
            chunk += " " * (chunk_size - len(chunk))

        encrypted += rsakey.encrypt(chunk)
        offset += chunk_size

    encrypted = encrypted.encode("base64")
    print "Base64 encoded crypto: %d" % len(encrypted)
    print encrypted


def main():
    option = raw_input("加密(e) or 解密(d): ")
    if option == 'e':
        encryptor()
    elif option == 'd':
        decryptor()


if __name__ == "__main__":
    while True:
        main()
