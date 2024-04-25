import os
import pyaes

def decrypt_file(encrypted_file_path, key, output_file_path):
    # Abrir o arquivo criptografado
    with open(encrypted_file_path, "rb") as encrypted_file:
        file_data = encrypted_file.read()

    # Remover o arquivo criptografado
    os.remove(encrypted_file_path)

    # Descriptografar usando AES-CTR
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypted_data = aes.decrypt(file_data)

    # Salvar o arquivo descriptografado
    with open(output_file_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    return output_file_path

# Arquivo criptografado que queremos descriptografar
encrypted_file_path = "teste.txt.encrypted"

# Chave para descriptografia (deve ser a mesma chave usada para criptografar)
key = b"testeransomwares"

# Nome do arquivo descriptografado
decrypted_file_path = "teste_decrypted.txt"

# Descriptografar o arquivo
decrypted_file_path = decrypt_file(encrypted_file_path, key, decrypted_file_path)

# Exibir mensagem ao usuário
print("Arquivo descriptografado com sucesso:", decrypted_file_path)

# Exibir mensagem personalizada após descriptografia
custom_message = "Seus arquivos foram descriptografados com sucesso!"
with open("exibir.txt", "w") as txt_file:
    txt_file.write(custom_message)
