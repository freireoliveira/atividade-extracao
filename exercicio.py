#%%
import numpy as np

def chars(string):
    return np.array(list(string))

print(chars('oi tudo bem?'))

#%%
def cripto(string):
    original = np.array([ord(c) for c in string])
    encripted = original * 33/2
    return encripted

def decrypt(encripted):
    decrypted = encripted * 2/33
    original = ''.join([chr(int(c)) for c in decrypted])
    return original

teste = cripto('oi tudo bem?')
dep = decrypt(teste)
print(teste, dep)

#%%
import matplotlib.pyplot as plt

