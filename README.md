# TelcoGuard AI — Customer Churn Intelligence Platform

هذا المشروع منظّم الآن كتطبيق Streamlit كامل وقابل للتشغيل مباشرة.

## هيكل الملفات

```
telcoguard/
├── app.py                  # نقطة التشغيل الرئيسية (شغّل هذا الملف)
├── config.py                # الإعدادات والثوابت
├── styles.py                # الـ CSS المخصص للواجهة
├── loader.py                 # تحميل الموديل / الـ scaler / الأعمدة
├── preprocessing.py          # معالجة بيانات العميل قبل التنبؤ
├── predictor.py              # منطق التنبؤ
├── charts.py                 # الرسوم البيانية (Plotly)
├── components.py             # عناصر واجهة قابلة لإعادة الاستخدام
├── financial.py              # حسابات التقرير المالي
├── ai_engine.py               # التحليل الذكي/التوصيات
├── simulator.py               # محاكي السيناريوهات (What-If)
├── report.py                  # توليد تقرير العميل القابل للتحميل
├── train.py                   # سكريبت تدريب الموديل (اختياري، لإعادة التدريب)
├── requirements.txt
├── WA_Fn-UseC_-Telco-Customer-Churn.csv   # بيانات التدريب الأصلية
└── models/
    ├── xgb_model.pkl
    ├── scaler.pkl
    └── model_columns.pkl
```

## طريقة التشغيل

1. ثبّت المتطلبات:
   ```
   pip install -r requirements.txt
   ```
2. شغّل التطبيق من داخل مجلد `telcoguard`:
   ```
   streamlit run app.py
   ```
3. هيفتحلك المتصفح تلقائيًا على `http://localhost:8501`

## إعادة تدريب الموديل (اختياري)

لو حبيت تعيد تدريب الموديل من جديد على نفس بيانات الـ CSV:
```
python train.py
```
هيولّد نسخة جديدة من `xgb_model.pkl` و`scaler.pkl` و`model_columns.pkl` — تأكد إنك تحطهم في مجلد `models/` بعد كده.

## الإصلاحات اللي اتعملت على الكود الأصلي

1. **تقسيم `app.py`** كان ملف واحد فيه كل المشروع ملزوق جواه، رغم إن فيه `import` statements بتحاول تستورد ملفات منفصلة (config, styles, loader...) مش موجودة فعليًا. اتقسم دلوقتي لملفات حقيقية مطابقة للـ imports.
2. **مسارات الموديل**: كانت بتشاور على مجلد `models/` غير موجود — دلوقتي الملفات فعليًا داخل `models/`.
3. **CSS مكسور في `styles.py`**: الـ `st.markdown("""...""")` كان بيتقفل في نص الـ CSS، والباقي (حوالي 330 سطر) كان طايح برا الـ string كـ Python code خام، وده كان هيسبب `SyntaxError` عند التشغيل. اتصلح بضم كل الـ CSS جوه string واحد مقفول صح.
4. **متغيرات خارج نطاقها**: قسم "Scenario Simulator" و"Download Report" كانوا بيستخدموا `customer_data`/`prediction_result`/`model`/`scaler`/`model_columns` من غير ما يكونوا متأكدين إنهم موجودين، فكان ممكن يحصل `NameError` لو المستخدم يضغط عليهم قبل ما يعمل أول تنبؤ. اتعملهم إزاحة (indent) صح جوه نفس الشرط `if "prediction" in st.session_state:`.
5. **كود config مكرر ومتضارب** كان في آخر الملف الأصلي (نسخة تانية بقيم مختلفة) — اتشال.

تم اختبار التطبيق فعليًا وشغال بدون أخطاء (`streamlit run app.py` اشتغل ورجع الرابط بنجاح).
