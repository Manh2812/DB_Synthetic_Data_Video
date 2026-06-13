# Project

## Cài môi trường ảo

```bash
py -3.11 -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

## Cài thư viện

```bash
pip install -r requirements.txt
```


## Chạy chương trình

Chạy tất cả scene với chất lượng thấp mặc định:

```bash
python main.py
```

Chọn chế độ render:

```bash
python main.py -q l  # thấp, nhanh
python main.py -q m  # trung bình
python main.py -q h  # cao
python main.py -q k  # 4K
```

Chỉ chạy một vài scene:

```bash
python main.py Scene1Intro Scene3Text
```

chạy scene1_intro.py
python main.py -q l Scene1Intro
python main.py -q h Scene1Intro

ghép video với audio của scene1
python combine_audio_scene1.py