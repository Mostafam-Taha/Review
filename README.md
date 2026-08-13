# 📚 Library Manager

مشروع بسيط لإدارة مكتبة عن طريق الـ Command Line (Console)، بيسمح للمستخدم إنه يضيف كتب، يبحث عنها، يستعيرها، يرجعها، ويشوف كل الكتب الموجودة في المكتبة.

| البيان | التفاصيل |
|---|---|
| تاريخ الإنشاء | 8 أغسطس 2026 |
| اللغة المستخدمة | Python |
| نوع المشروع | Console Application |
| صاحب المشروع | **mostafamtaha** |
| رابط الملف على GitHub | [https://github.com/Mostafam-Taha/Review/blob/main/learn.py] |

### ▶️ طريقة التشغيل

```bash
python learn.py
```

بعد التشغيل هيطلب منك البرنامج تدخل اسم المستخدم، وبعدها هتظهرلك القائمة الرئيسية للاختيار من بين العمليات المتاحة.

---

<details>
<summary><strong>💡 اضغط لعرض فكرة المشروع بالتفصيل</strong></summary>

<br>

برنامج بسيط شغال على الـ Terminal بيحاكي نظام إدارة مكتبة، حيث يقدر المستخدم يتعامل مع مجموعة كتب من خلال قائمة اختيارات (Menu) بسيطة، وكل عملية بتتم من خلالها بتعدل على بيانات الكتب المخزنة أثناء تشغيل البرنامج.

المشروع ده repo مستقل بذاته، الهدف منه تطبيق أساسيات لغة Python بشكل عملي بعد الانتهاء من تعلم المفاهيم الأساسية للغة، زي:
- المتغيرات وأنواع البيانات
- الشروط (Conditionals)
- الحلقات (Loops)
- الدوال (Functions)
- التعامل مع القوائم (Lists)
- إدخال ومعالجة بيانات المستخدم

</details>

<details>
<summary><strong>⚙️ اضغط لعرض الوظائف المتاحة (Features)</strong></summary>

<br>

| # | الوظيفة | الوصف |
|---|---|---|
| 1 | Add Book | إضافة كتاب جديد بمعلوماته (الاسم، المؤلف، السنة، الكمية، متاح أو لا) |
| 2 | Search Book | البحث عن كتاب بالاسم وعرض كل تفاصيله |
| 3 | Borrow Book | استعارة كتاب موجود وتقليل كميته المتاحة |
| 4 | Return Book | إضافة كتاب جديد للمكتبة (قيد التطوير ليصبح إرجاع فعلي) |
| 5 | Show All Books | عرض كل الكتب الموجودة بكل تفاصيلها |
| 6 | Remove Book | حذف كتاب بالكامل من المكتبة |
| 7 | Exit | الخروج من البرنامج |

</details>

<details>
<summary><strong>🧠 اضغط لعرض المفاهيم البرمجية المستخدمة</strong></summary>

<br>

- ✅ Variables & Data Types
- ✅ Conditionals (if / elif / else)
- ✅ Loops (while)
- ✅ Functions
- ✅ Lists
- ✅ Type Casting (تحويل الـ input من str لـ int)
- ⏳ Type Annotations *(قيد الإضافة)*
- ⏳ Tuples *(قيد الإضافة)*
- ⏳ Sets *(قيد الإضافة)*
- ⏳ Exception Handling *(قيد الإضافة)*

</details>

<details>
<summary><strong>🐛 اضغط لعرض حالة المشروع الحالية (Known Issues)</strong></summary>

<br>

المشروع لسه تحت التطوير، وفيه نقط شغالة بشكل كامل، ونقط لسه محتاجة تعديل:

- **Borrow Book**: فيها مشكلة في تحديث الكمية بعد الاستعارة، محتاجة مراجعة.
- **Return Book**: حاليًا الدالة بتضيف كتاب جديد بدل ما تزود كمية كتاب موجود، محتاجة إعادة بناء.
- **Error Handling**: مفيش تعامل مع الأخطاء لو المستخدم دخل بيانات غلط (زي حروف بدل أرقام).

</details>

<details>
<summary><strong>🚀 اضغط لعرض الخطوات القادمة (To-Do)</strong></summary>

<br>

- [ ] إصلاح دالة Borrow Book
- [ ] إعادة بناء دالة Return Book لتعمل كإرجاع فعلي
- [ ] إضافة Exception Handling لكل عمليات الإدخال
- [ ] إضافة Type Annotations لكل الدوال
- [ ] إضافة سجل عمليات (History Log) باستخدام Tuples
- [ ] إضافة دالة لعرض المؤلفين بدون تكرار باستخدام Sets
- [ ] (اختياري) تحويل تخزين البيانات من قوائم منفصلة إلى Dictionary لكل كتاب

</details>

---

# 🏧 ATM Simulator

برنامج بسيط بيحاكي ماكينة صراف آلي (ATM) عن طريق الـ Command Line، بيدخل المستخدم PIN أول حاجة، وبعدين يقدر يعرض رصيده، يودع، أو يسحب فلوس.

| البيان | التفاصيل |
|---|---|
| تاريخ الإنشاء | 12 أغسطس 2026 |
| اللغة المستخدمة | Python |
| نوع المشروع | Console Application |
| صاحب المشروع | **mostafamtaha** |

### ▶️ طريقة التشغيل

```bash
python ATM_Simulator.py
```

بعد التشغيل هيطلب منك البرنامج تدخل الـ PIN (عندك 3 محاولات)، ولو صح هتظهرلك القائمة الرئيسية للاختيار من بين العمليات المتاحة.

<details>
<summary><strong>⚙️ اضغط لعرض الوظائف المتاحة (Features)</strong></summary>

<br>

| # | الوظيفة | الوصف |
|---|---|---|
| 1 | Show Balance | عرض الرصيد الحالي |
| 2 | Deposit | إيداع مبلغ (مرفوض لو المبلغ سالب) |
| 3 | Withdraw | سحب مبلغ (مرفوض لو أكبر من الرصيد أو سالب) |
| 0 | Exit | الخروج من البرنامج |

**PIN Protection**: نظام دخول بـ PIN محدد بـ 3 محاولات، ولو فشلت كلها البرنامج بيقفل.

</details>

<details>
<summary><strong>🧠 اضغط لعرض المفاهيم البرمجية المستخدمة</strong></summary>

<br>

- ✅ Variables & Data Types
- ✅ Conditionals (if / elif / else)
- ✅ Loops (while)
- ✅ Functions
- ✅ Type Casting (تحويل الـ input من str لـ int)
- ⏳ Exception Handling *(قيد الإضافة)*

</details>

<details>
<summary><strong>🐛 اضغط لعرض حالة المشروع الحالية (Known Issues)</strong></summary>

<br>

- **Error Handling**: مفيش تعامل مع الأخطاء لو المستخدم دخل حروف بدل أرقام.
- الدوال بتعتمد على `global balance` بدل إنها تاخد وترجع القيمة كـ parameter.

</details>

<details>
<summary><strong>🚀 اضغط لعرض الخطوات القادمة (To-Do)</strong></summary>

<br>

- [ ] إضافة Exception Handling (try/except) لكل عمليات الإدخال
- [ ] إزالة الاعتماد على `global balance` واستخدام parameters بدل منها
- [ ] تحسين أسامي المتغيرات (زي `user_Experins`)

</details>

---

# 💰 Wallet Tracker

برنامج بسيط بيحاكي متابعة رصيد ومعاملات مالية شخصية عن طريق الـ Command Line، بيدخل المستخدم باسورد أول حاجة، وبعدين يقدر يعرض رصيده، يضيف معاملة جديدة، أو يعدّل معاملة موجودة.

| البيان | التفاصيل |
|---|---|
| تاريخ الإنشاء | 13 أغسطس 2026 |
| اللغة المستخدمة | Python |
| نوع المشروع | Console Application |
| صاحب المشروع | **mostafamtaha** |

### ▶️ طريقة التشغيل

```bash
python wallet_tracker.py
```

بعد التشغيل هيطلب منك البرنامج تدخل الباسورد (لازم يكون 8 أرقام)، وعندك 5 محاولات. لو المحاولات خلصت من غير ما تدخل الباسورد صح، البرنامج بيقفل من غير أي رسالة تنبيه (سلوك مقصود).

<details>
<summary><strong>⚙️ اضغط لعرض الوظائف المتاحة (Features)</strong></summary>

<br>

| # | الوظيفة | الوصف |
|---|---|---|
| 1 | Show Balance | عرض الرصيد الحالي وكل المعاملات المسجلة |
| 2 | Add Balance | إضافة معاملة جديدة (اسم، مبلغ، تاريخ) - مرفوضة لو المبلغ سالب أو صفر |
| 3 | Update Balance | تعديل معاملة موجودة بالاسم (تغيير الاسم، المبلغ، والتاريخ) |
| 0 | Exit | الخروج من البرنامج |

**Password Protection**: نظام دخول بباسورد من 8 أرقام، محدد بـ 5 محاولات، ولو فشلت كلها البرنامج بيقفل بصمت.

</details>

<details>
<summary><strong>🧠 اضغط لعرض المفاهيم البرمجية المستخدمة</strong></summary>

<br>

- ✅ Variables & Data Types
- ✅ Conditionals (if / elif / else)
- ✅ Loops (while / for)
- ✅ Functions
- ✅ Lists
- ✅ Global Variables
- ✅ Type Casting (تحويل الـ input من str لـ int/float)
- ⏳ Exception Handling *(قيد الإضافة)*
- ⏳ Dictionaries لتخزين المعاملات *(قيد الإضافة)*

</details>

<details>
<summary><strong>🐛 اضغط لعرض حالة المشروع الحالية (Known Issues)</strong></summary>

<br>

- **Error Handling**: مفيش تعامل مع الأخطاء لو المستخدم دخل حروف بدل أرقام.
- **Update Balance**: تعديل معاملة موجودة مش بيحدّث الـ balance الكلي معاها (يفضل الرصيد زي ما كان قبل التعديل).
- البيانات متخزنة في 3 لستات منفصلة (اسم/مبلغ/تاريخ) بدل Dictionary واحد لكل معاملة، وده بيخلي البحث بالـ `.index()` عرضة للأخطاء لو فيه أسامي متكررة.
- أسامي بعض المتغيرات والدوال فيها أخطاء إملائية بسيطة (زي `attemy`, `Updata`, `degits`, `defound`).

</details>

<details>
<summary><strong>🚀 اضغط لعرض الخطوات القادمة (To-Do)</strong></summary>

<br>

- [ ] إضافة Exception Handling (try/except) لكل عمليات الإدخال
- [ ] تحويل تخزين البيانات من 3 لستات منفصلة إلى Dictionary لكل معاملة
- [ ] تحديث الـ balance تلقائيًا عند تعديل معاملة موجودة
- [ ] تصحيح أسامي المتغيرات والدوال (زي `attempts`, `update`, `digits`)
- [ ] إضافة رسالة تنبيه واضحة بعد انتهاء محاولات الباسورد (اختياري)

</details>
