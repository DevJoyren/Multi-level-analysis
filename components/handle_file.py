# Imports >>>
from pathlib import Path
import re


class HandleFile:

    def handle_text(self, file_path :str) -> str:
        """
        Handles the text input from the user.
        :param file_path:
        :return: text
        """
        text = Path(file_path).read_text(encoding='utf-8', errors='ignore').lower()

        # normalize whitespace
        text = re.sub(r"\s", " ", text)

        # Remove most punctuation,
        # keep ? . ! for sentence splitting
        # Important: replace with space, then squeeze spaces
        text = re.sub(r"[\",:;()\[\]{}“”‘’`~@#$%^&*+=/\\|<>]", " ", text)

        return text

