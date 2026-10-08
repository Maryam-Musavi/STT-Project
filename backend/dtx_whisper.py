"""
Dariush Tasdighi Custom 'openai-whisper' Package Module
"""

from typing import Final

import os
import time
import torch
import logging
import whisper
import dt_utility as utility

VERSION: Final[str] = "1.0.1"

TEMP_AUDIO_FILE_PATH: Final[str] = "./temp.mp3"

STT_TEMPRETURE: Final[float] = 0.0
STT_VALID_AUDIO_FILE_EXTENSIONS: Final[list[str]] = [
    "mp3".replace(" ", "").lower(),
    "wav".replace(" ", "").lower(),
]

STT_LANGUAGE: Final[str] = "en".replace(" ", "").lower()
STT_MODEL_NAME: Final[str] = "tiny".replace(" ", "").lower()

# STT_LANGUAGE: Final[str] = "fa".replace(" ", "").lower()
# STT_MODEL_NAME: Final[str] = "turbo".replace(" ", "").lower()

logger = logging.getLogger(name=__name__)
logger.addHandler(hdlr=logging.NullHandler())


def transcribe(
    language: str = STT_LANGUAGE,
    model_name: str = STT_MODEL_NAME,
    tempreture: float = STT_TEMPRETURE,
    audio_file_path: str = TEMP_AUDIO_FILE_PATH,
) -> tuple[str, float]:
    """
    Offline transcribe speech to text
    """

    logger.debug(msg=f"Whisper Model: '{model_name}' - Transcribe started...")

    start_time: float = time.perf_counter()

    # ********************
    message: str

    if not os.path.exists(path=audio_file_path):
        message = f"File '{audio_file_path}' not found"
        raise Exception(message)

    if not os.path.isfile(path=audio_file_path):
        message = f"File '{audio_file_path}' not found"
        raise Exception(message)

    file_extension: str = audio_file_path.split(sep=".")[-1].lower()
    if file_extension not in STT_VALID_AUDIO_FILE_EXTENSIONS:
        message: str = f"The '{audio_file_path}' file format is not valid"
        raise Exception(message)
    # ********************

    device: str = "cuda" if torch.cuda.is_available() else "cpu"
    fp16_enabled: bool = True if device == "cuda" else False

    model = whisper.load_model(
        device=device,
        name=model_name,
    )

    response: dict = model.transcribe(
        fp16=fp16_enabled,
        language=language,
        audio=audio_file_path,
        temperature=tempreture,
    )

    text: str = str(response.get("text", "")).strip()

    end_time: float = time.perf_counter()
    elapsed_time: float = end_time - start_time

    logger.debug(msg=f"Whisper Model: '{model_name}' - Transcribe finished.")

    return text, elapsed_time


if __name__ == "__main__":
    utility.display_just_one_error_message(
        message=utility.ERROR_MESSAGE_MODULE_IS_NOT_EXECUTED_DIRECTLY,
    )
