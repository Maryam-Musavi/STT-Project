# Learning STT (Speech to Text) with 'openai-whisper' package

## Tips and Tricks about Raw Models

## This program was developed by

- **Dariush Tasdighi**
  - Mobile Number: +98 912 108 7461
  - Email Address: <DariushT@GMail.com>
  - Telegram ID: <https://t.me/Dariush_Tasdighi>
  - Virgool: <https://virgool.io/@dariush-tasdighi>
  - Aparat: <https://www.aparat.com/IranianExperts>
  - LinkedIn: <https://www.linkedin.com/in/tasdighi>
  - Instagram: <https://www.instagram.com/dariushtasdighi>
  - Telegram Channels:
    - <https://t.me/IranianExperts>
    - <https://t.me/DT_PYTHON_LEARNING>

## Used Packages

### 'rich' package

- <https://pypi.org/project/rich>
- <https://github.com/Textualize/rich>
- **More:**
  - <https://rich.readthedocs.io/en/latest>
  - <https://rich.readthedocs.io/en/latest/appendix/colors.html>

### 'PyAudio' package

- <https://pypi.org/project/PyAudio>
- <https://github.com/CristiFati/pyaudio>
- **More:**
  - <https://people.csail.mit.edu/hubert/pyaudio>
  - <https://people.csail.mit.edu/hubert/pyaudio/docs>

### 'readchar' package

- <https://pypi.org/project/readchar>
- <https://github.com/magmax/python-readchar>

### 'playsound3' package

- <https://pypi.org/project/playsound3>
- <https://github.com/szmikler/playsound3>
- **More:**
  - <https://github.com/szmikler/playsound3/blob/main/README.md>

### 'openai-whisper' package

- <https://pypi.org/project/openai-whisper>
- <https://github.com/openai/whisper>

### 'SpeechRecognition' package

- <https://pypi.org/project/SpeechRecognition>
- <https://github.com/Uberi/speech_recognition>
- **More:**
  - <https://realpython.com/python-speech-recognition>
  - <https://dev.to/abhinowww/how-to-record-audio-in-python-automatically-detect-speech-and-silence-4951>

## Setup Environment

```bash
# python -m venv .venv
# .\.venv\Scripts\activate

# python -m pip list
# python -m pip install -r .\requirements.txt -U
# python -m pip list

# deactivate
```

```bash
py -3.13 -m venv .venv.3.13
.\.venv.3.13\Scripts\activate

python -m pip list
python -m pip install -r .\requirements.3.13.txt -U
python -m pip list

deactivate
```

- **Note:** Two packages ('openai-whisper' and 'SpeechRecognition') does not work with Python 3.14!

```bash
# py -3.14 -m venv .venv.3.14
# .\.venv.3.14\Scripts\activate

# python -m pip list
# python -m pip install -r .\requirements.3.14.txt -U
# python -m pip list

# deactivate
```

## Solving Install Python Package Problems in Windows

- <https://vrgl.ir/T3JLR>
  - Linux / Mac Built-in Compiler: cmake

## Install 'ffmpeg'

- <https://ffmpeg.org/download.html>
  - <https://ffmpeg.org/download.html#build-windows>
    - <https://www.gyan.dev/ffmpeg/builds>
    - <https://github.com/BtbN/FFmpeg-Builds/releases>  # به روزتر است
      - Download: '**ffmpeg-master-latest-win64-gpl-shared.zip**' file

- **Note:** In Windows Command Prompt (CMD)! Not in Windows PowerShell

```shell
where ffmpeg

ffmpeg -h
ffmpeg --help

ffmpeg -version
```

- **Note:** Set 'Path' in System Environment Variables
- **Note:** After running 'ffmpeg -version' command -> See the version in '--extra-version'

## For using 'GPU' / 'CUDA'

- Not OK! Python / Python Module         -> GPU ('NVIDIA')
- OK!     Python / Python Module -> CUDA -> GPU ('NVIDIA')

### Check your 'GPU' card

- Must be 'NVIDIA'

### Check your 'NVIDIA' compatible with 'CUDA'

- 10x
- 20x
- ...
- 50x -> 5090 (Desktop: 32GB VRAM / Laptop: 24GB VRAM)

### Update 'NVIDIA' Driver

- <https://www.nvidia.com/en-us/software/nvidia-app>

### Check your max version of 'CUDA' that supports by your 'NVIDIA'

- **Note:** You do not need to install 'CUDA'!

- Check 'CUDA' Version

- نسخه برنامه ذیل ملاک است

```shell
nvidia-smi
```

- نسخه برنامه ذیل اصلا ملاک نیست

```shell
nvcc --version
```

### PyTorch

- <https://pytorch.org>
  - Click: Previous versions of PyTorch

- **Note:** نیز نصب می‌شود 'torch' کتابخانه ،'openai-whisper' در زمان نصب کتابخانه
- **Note:** The installed 'torch' is just for 'CPU' not for 'GPU' / 'CUDA'!

```shell
python -m pip uninstall torch torchvision torchaudio -y
```

- **Note:** The below packages size is about 3 GB!

```shell
# Note: The below code does not work!
# python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu129 -U

# python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128 -U

python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126 -U
python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126 -Uv  --retries 200 --timeout 30
```

---
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu134