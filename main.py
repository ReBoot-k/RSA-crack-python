import RSA


rsa = RSA.RSA(P = 23, Q = 29, E = 493)
print(rsa.get_decrypt_message([298,107,16,271,237,420,298,34,271,298,107,16]))
