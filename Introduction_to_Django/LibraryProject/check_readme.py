import os

# تحديد مسار ملف README.md
file_path = "E:/Alx_DjangoLearnLab/LibraryProject/README.md"

# التحقق من وجود الملف والتأكد من أنه غير فارغ
if os.path.exists(file_path):
    if os.path.getsize(file_path) > 0:
        print("README.md file exists and is not empty.")
    else:
        print("README.md file exists but is empty.")
else:
    print("README.md file does not exist.")
