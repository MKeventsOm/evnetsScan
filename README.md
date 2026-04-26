# InkFlow v3

## Project Structure
```
inkflow_v3/
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html           ← Main menu (Sign + Welcome buttons)
│   ├── ipad.html            ← iPad: horizontal signature pad
│   ├── screen_sign.html     ← Screen: live signature display
│   ├── ipad_welcome.html    ← iPad: welcome trigger button
│   └── screen_welcome.html  ← Screen: video → photo sequence
└── static/
    ├── images/
    │   ├── bg_menu.jpg
    │   ├── bg_sign.jpg
    │   ├── bg_welcome.jpg
    │   ├── bg_ipad_sign.jpg
    │   ├── bg_ipad_welcome.jpg
    │   └── welcome_photo.jpg
    └── videos/
        └── welcome.mp4
```

## Install & Run
```bash
pip install flask flask-socketio
python app.py
```

## URL Guide

| Device  | Mode    | URL                              |
|---------|---------|----------------------------------|
| Browser | Menu    | http://[IP]:5000                 |
| iPad    | Sign    | http://[IP]:5000/ipad            |
| Screen  | Sign    | http://[IP]:5000/screen          |
| iPad    | Welcome | http://[IP]:5000/ipad-welcome    |
| Screen  | Welcome | http://[IP]:5000/screen-welcome  |

## How It Works
1. Open main menu → choose Sign or Welcome Page
2. **Sign mode**: iPad draws → screen shows live
3. **Welcome mode**: iPad presses button → screen plays video → shows photo + confetti
