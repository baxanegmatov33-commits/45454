from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

PRIVATE_KEY_FILE = "private_key.pem"
SIGNATURE_FILE = "signature.sig"

# Сообщение для подписи
message = input("Введите сообщение для подписи: ").encode()

# Загрузка приватного ключа
with open(PRIVATE_KEY_FILE, "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None
    )

# Создание подписи (RSA + SHA256)
signature = private_key.sign(
    message,
    padding.PKCS1v15(),
    hashes.SHA256()
)

# Сохранение подписи в файл
with open(SIGNATURE_FILE, "wb") as f:
    f.write(signature)

print("SIGNATURE CREATED OK")

