# 🛡️ CyberShield AI
### Multilingual AI-Powered Phishing Detection & Explainable Threat Intelligence System
*نظام ذكي متعدد اللغات لكشف التصيد الاحتيالي وتفسير المخاطر الأمنية (اللهجة المصرية، العربية الفصحى، والإنجليزية)*

---

## 📌 نظرة عامة على المشروع (Project Overview)
**CyberShield AI** هو مشروع بحثي أمني متكامل يهدف إلى حماية المستخدمين والمؤسسات من هجمات الهندسة الاجتماعية والتصيد الاحتيالي (Phishing) عبر الرسائل النصية، ورسائل البريد الإلكتروني، والروابط المشبوهة.

يتميز النظام بقدرته المتخصصة على:
1. **تحليل اللهجة المصرية العامية (Egyptian Colloquial Arabic - `arz`)**: التعرف على الأنماط الشائعة في مصر مثل احتيال المحافظ الإلكترونية (*فودافون كاش، انستاباي، فوري*)، والجوائز والمسابقات الوهمية، وانتحال البنوك الوطنية (*البنك الأهلي، بنك مصر*).
2. **تحليل اللغة العربية الفصحى (Modern Standard Arabic - `ar`) والإنجليزية (`en`)**: كشف خطابات التهديد المصرفية، وتجميد الحسابات، وتصيد بيانات الاعتماد (Credential Harvesting).
3. **فحص متقدم لخصائص الروابط (URL Inspection)**: استخراج أكثر من 20 خاصية معجمية وهيكلية (عناوين IP المباشرة، هجمات تماثل الحروف Punycode، النطاقات الرخيصة المشبوهة، خدمات تقصير الروابط، وعشوائية أسماء النطاقات DGA Entropy) دون الحاجة لفتح الرابط أو تعريض المستخدم للخطر.
4. **محرك دمج المخاطر التفسيري (Explainable Risk Fusion Engine)**: دمج درجات محرك النصوص ومحرك الروابط لإنتاج تقييم موحد وموثوق مصحوباً بتقرير تفسيري يشرح أسباب التحذير بدقة وإجراءات الحماية الموصى بها.
5. **معمارية خفيفة تناسب بيئات العمل محدودة الموارد (8GB RAM)** مع الحفاظ على الأداء الأكاديمي الصارم.

---

## 🏛️ المعمارية التقنية (Modular Technical Architecture)

```
CyberShield AI
│
├── 🌐 Presentation Layer (Web Dashboard & Mobile API)
│     ├── Bilingual UI (العربية RTL / English LTR)
│     ├── Interactive Threat Gauge & Explainability Breakdown
│     └── Fast RESTful API (FastAPI) + CORS enabled for Android
│
├── 🧠 Intelligence & Analytics Engines
│     ├── 1. Text Analysis Engine (NLP)
│     │     ├── Arabic Normalization (Tashkeel, Tatweel, Alif/Yaa variants)
│     │     ├── Egyptian Dialect & Colloquial Token Identification
│     │     ├── TF-IDF (Word N-grams 1-2 + Character N-grams 3-5)
│     │     └── Scikit-Learn Classifier with LIME/Feature Attribution
│     │
│     ├── 2. URL Feature Extraction Engine
│     │     ├── 22 Lexical, Host, & Structural Academic Features
│     │     ├── Shannon Entropy & DGA Detection
│     │     ├── Punycode / IDN Homograph & Shortener Resolution
│     │     └── Random Forest Classifier + Security Heuristics
│     │
│     └── 3. Risk Fusion Engine
│           ├── Dynamic Threat-Dominance & Synergistic Weighting
│           ├── Calibrated Risk Score (0 - 100%) & Confidence Metrics
│           └── Explainable Risk Factors (XAI) & Actionable Guidance
│
└── 🗄️ Persistence Layer (Database)
      ├── SQLite (WAL Mode for High Concurrency)
      ├── Tables: analyses, datasets, model_versions, feedback
      └── PostgreSQL-Ready Schema
```

---

## 🗄️ هيكل قاعدة البيانات (Database Schema)

| اسم الجدول | الوظيفة |
| :--- | :--- |
| `analyses` | تسجيل جميع عمليات الفحص الفورية، النصوص المدخلة، الروابط، درجات الخطورة لكل محرك، التقرير التفسيري، وزمن المعالجة. |
| `datasets` | فهرسة مجموعات البيانات المعتمدة في التدريب والاختبار، مصادرها، وعدد العينات. |
| `model_versions` | تسجيل إصدارات النماذج وتاريخ تدريبها ومقاييس الأداء الأكاديمية (Accuracy, Precision, Recall, F1, ROC-AUC) ومصفوفة الارتباك. |
| `feedback` | حلقة الملاحظات البشرية (Human-in-the-Loop) لتسجيل الإنذارات الخاطئة (False Positives/Negatives) تمهيداً للتعلم المستمر وإعادة التدريب. |

---

## 📊 النتائج والمقاييس البحثية الحالية (Benchmark Results)

تم تقييم النماذج عبر تقسيم طبقي مستقل (Stratified Train/Test Split):

### 1. محرك النصوص متعدد اللغات (Multilingual Text Classifier):
- **الخوارزمية**: TF-IDF (Word & Character N-grams) + Logistic Regression
- **الدقة (Accuracy)**: `83.3%`
- **معيار F1-Score**: `0.8750`
- **مساحة منحنى ROC-AUC**: `0.9429`
- **مصفوفة الارتباك (Confusion Matrix)**: `TN=3, FP=2, FN=0, TP=7`

### 2. محرك فحص خصائص الروابط (URL Random Forest Classifier):
- **الخوارزمية**: Random Forest (22 Features: Host, Entropy, Lexical)
- **الدقة (Accuracy)**: `88.9%`
- **معيار F1-Score**: `0.8571`
- **مساحة منحنى ROC-AUC**: `0.9500`
- **مصفوفة الارتباك (Confusion Matrix)**: `TN=5, FP=0, FN=1, TP=3`

---

## 🚀 تشغيل النظام (Running the System)

### 1. تثبيت الحزم المطلوبة
```bash
pip install -r requirements.txt
```

### 2. تدريب النماذج وبناء قاعدة البيانات
```bash
python -m app.data.train
```

### 3. تشغيل خادم الويب وواجهة المستخدم
```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```
افتح المتصفح على: `http://127.0.0.1:8000`

### 4. تشغيل حزمة الاختبارات الشاملة (Unit & Integration Tests)
```bash
python -m unittest discover tests
```

---

## 📱 جاهزية وتكامل تطبيق Android (Android Readiness)

تم تصميم الـ Backend بواجهة RESTful API مع تفعيل CORS بالكامل لسهولة الربط مع تطبيقات Android عبر Retrofit أو Ktor.

### مثال استدعاء الـ API (Android Retrofit Interface):
```kotlin
interface CyberShieldApi {
    @POST("/api/analyze")
    suspend fun analyzeThreat(@Body request: ThreatRequest): ThreatResponse

    @POST("/api/feedback")
    suspend fun submitFeedback(@Body feedback: FeedbackRequest): FeedbackResponse
}

data class ThreatRequest(val text: String)
data class ThreatResponse(
    val verdict: String,
    val risk_level: String,
    val final_risk_score: Float,
    val confidence: Float,
    val detected_language: String,
    val explanation_factors: List<ExplanationFactor>,
    val recommendations: Map<String, List<String>>
)
```

يمكن لتطبيق أندرويد لاحقاً قراءة الرسائل النصية القصيرة (SMS Listener Service) أو مشاركة الروابط من المتصفح (Android Share Sheet Intent) وإرسالها فوراً لنقطة النهاية `/api/analyze` لعرض تنبيه أمني عائم للمستخدم.
