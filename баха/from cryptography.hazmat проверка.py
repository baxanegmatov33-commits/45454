from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature

PUBLIC_KEY_FILE = "public_key.pem"
SIGNATURE_FILE = "signature.sig"

# Сообщение для проверки
message = input("Введите сообщение для проверки подписи: ").encode()

# Загрузка публичного ключа
with open(PUBLIC_KEY_FILE, "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

# Загрузка подписи
with open(SIGNATURE_FILE, "rb") as f:
    signature = f.read()

# Проверка подписи
try:
    public_key.verify(
        signature,
        message,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    print("SIGNATURE VALID ✅")
except InvalidSignature:
    print("SIGNATURE INVALID ❌")
