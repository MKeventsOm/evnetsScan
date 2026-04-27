# InkFlow — لوحة الكتابة التفاعلية

## هيكل المشروع
```
inkflow/
├── app.py                    ← السيرفر الرئيسي
├── requirements.txt          ← المكتبات المطلوبة
├── templates/
│   ├── draw.html             ← صفحة الكتابة (الآيباد)
│   └── view.html             ← صفحة العرض (الشاشة)
└── static/
    └── images/
        ├── bg_welcome.jpg    ← خلفية شاشة الترحيب
        ├── bg_draw.jpg       ← خلفية لوحة الكتابة
        └── bg_view.jpg       ← خلفية شاشة العرض
```

## التثبيت
```
pip install flask flask-socketio
```

## التشغيل
```
python app.py
```

## الاستخدام
- **الآيباد**: افتح http://[IP]:5000
- **الشاشة**: افتح http://[IP]:5000/view
