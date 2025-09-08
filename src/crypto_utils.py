from cryptography.fernet import Fernet, InvalidToken
from typing import Any, Dict

class JSONKeyEncryptor:
    """
    Encrypt and decrypt JSON/dict keys using Fernet symmetric encryption.

    :param key: A Fernet key to use, defaults to None
    :type key: bytes, optional

    :ivar fernet: Fernet instance used for encryption/decryption
    :vartype fernet: cryptography.fernet.Fernet
    :ivar key: Encryption key used for the Fernet instance
    :vartype key: bytes
    """

    def __init__(self, key: bytes = None):
        if key is None:
            key = Fernet.generate_key()
        self.fernet = Fernet(key)
        self.key = key

    def encrypt_dict_values(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Encrypt all dictionary keys.

        :param data: Dictionary with plaintext keys
        :type data: dict
        """
        return {k: self.encrypt_value(v) for k, v in data.items()}

    def decrypt_dict_values(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Decrypt only encrypted dictionary values and keep the rest unchanged.

        :param data: Dictionary with possibly encrypted values
        :type data: dict
        """
        decrypted = {}
        for k, v in data.items():
            try:
                decrypted[k] = self.decrypt_value(value=v)
            except (ValueError, InvalidToken, AttributeError):
                decrypted[k] = v

        return decrypted

    def encrypt_value(self, value: str) -> str:
        """
        Encrypt a single value string.

        :param value: Plaintext value to encrypt
        :type value: str
        """
        return self.fernet.encrypt(value.encode()).decode()

    def decrypt_value(self, value: str) -> str:
        """
        Decrypt a single encrypted value.

        :param value: Encrypted value string
        :type value: str
        :raises cryptography.fernet.InvalidToken: If the value cannot be decrypted
        """
        return self.fernet.decrypt(value.encode()).decode()