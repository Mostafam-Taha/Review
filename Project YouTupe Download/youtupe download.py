"""
YouTube Video Downloader
يعتمد على مكتبة pytubefix (نسخة محدّثة ومدعومة من pytube)
تثبيت المتطلبات:
    pip install pytubefix
"""

import os
import threading
from tkinter import *
from tkinter import filedialog, messagebox, ttk

from pytubefix import YouTube


# ---------------------------------------------------------------------------
# المتغيرات العامة
# ---------------------------------------------------------------------------
save_path = os.path.join(os.path.expanduser("~"), "Downloads")
current_yt = None
current_streams = {}  # resolution -> stream object


# ---------------------------------------------------------------------------
# الدوال
# ---------------------------------------------------------------------------
def fetch_video_info():
    """يجيب معلومات الفيديو والجودات المتاحة بعد لصق الرابط"""
    url = link_var.get().strip()
    if not url:
        messagebox.showerror("خطأ", "من فضلك الصق رابط الفيديو أولاً")
        return

    def worker():
        global current_yt, current_streams
        try:
            set_status("جاري جلب بيانات الفيديو...")
            fetch_button.config(state=DISABLED)

            current_yt = YouTube(url, on_progress_callback=on_progress)
            title_var.set(current_yt.title)

            # نجمع أعلى ستريم لكل دقة (فيديو + صوت مدموجين progressive)
            current_streams = {}
            for stream in current_yt.streams.filter(progressive=True, file_extension="mp4"):
                current_streams[stream.resolution] = stream

            resolutions = sorted(
                current_streams.keys(),
                key=lambda r: int(r.replace("p", "")),
                reverse=True,
            )

            if not resolutions:
                set_status("لا توجد جودات متاحة لهذا الفيديو ❌")
                return

            quality_menu["values"] = resolutions
            quality_var.set(resolutions[0])
            set_status("تم جلب البيانات بنجاح ✅ اختر الجودة واضغط تحميل")

        except Exception as e:
            set_status("حدث خطأ أثناء جلب البيانات ❌")
            messagebox.showerror("خطأ", f"تعذّر جلب بيانات الفيديو:\n{e}")
        finally:
            fetch_button.config(state=NORMAL)

    threading.Thread(target=worker, daemon=True).start()


def on_progress(stream, chunk, bytes_remaining):
    """Callback بيحدّث شريط التقدم أثناء التحميل"""
    total = stream.filesize
    downloaded = total - bytes_remaining
    percentage = int(downloaded / total * 100)
    progress_bar["value"] = percentage
    set_status(f"جاري التحميل... {percentage}%")
    root.update_idletasks()


def choose_folder():
    """يسمح للمستخدم يختار مكان حفظ الفيديو"""
    global save_path
    folder = filedialog.askdirectory()
    if folder:
        save_path = folder
        path_var.set(save_path)


def download_video():
    """يحمل الفيديو بالجودة المختارة"""
    if current_yt is None or not current_streams:
        messagebox.showerror("خطأ", "من فضلك اجلب بيانات الفيديو أولاً (زرار Fetch)")
        return

    resolution = quality_var.get()
    stream = current_streams.get(resolution)
    if stream is None:
        messagebox.showerror("خطأ", "من فضلك اختر جودة صحيحة")
        return

    def worker():
        try:
            download_button.config(state=DISABLED)
            progress_bar["value"] = 0
            set_status("جاري بدء التحميل...")

            stream.download(output_path=save_path)

            progress_bar["value"] = 100
            set_status("تم التحميل بنجاح ✅")
            messagebox.showinfo("تم", f"تم حفظ الفيديو في:\n{save_path}")
        except Exception as e:
            set_status("حدث خطأ أثناء التحميل ❌")
            messagebox.showerror("خطأ", f"حدث خطأ أثناء التحميل:\n{e}")
        finally:
            download_button.config(state=NORMAL)

    threading.Thread(target=worker, daemon=True).start()


def set_status(text):
    status_var.set(text)


# ---------------------------------------------------------------------------
# الواجهة
# ---------------------------------------------------------------------------
root = Tk()
root.title("YouTube Video Downloader")
root.geometry("560x420")
root.resizable(False, False)
root.configure(bg="#1e1e2f")

link_var = StringVar()
title_var = StringVar()
quality_var = StringVar()
status_var = StringVar(value="أدخل رابط الفيديو وابدأ")
path_var = StringVar(value=save_path)

# العنوان
Label(
    root, text="YouTube Video Downloader",
    font="arial 20 bold", bg="#1e1e2f", fg="white"
).pack(pady=15)

# رابط الفيديو
Label(root, text="رابط الفيديو:", font="arial 12 bold", bg="#1e1e2f", fg="white").pack(anchor="w", padx=30)
link_frame = Frame(root, bg="#1e1e2f")
link_frame.pack(pady=5, padx=30, fill="x")

link_entry = Entry(link_frame, textvariable=link_var, font="arial 11")
link_entry.pack(side=LEFT, fill="x", expand=True, ipady=4)

fetch_button = Button(
    link_frame, text="جلب البيانات", font="arial 10 bold",
    bg="#3a86ff", fg="white", command=fetch_video_info
)
fetch_button.pack(side=LEFT, padx=(8, 0))

# عنوان الفيديو
Label(root, textvariable=title_var, font="arial 11", bg="#1e1e2f", fg="#8ecae6",
      wraplength=500, justify="right").pack(pady=(10, 5))

# اختيار الجودة
quality_frame = Frame(root, bg="#1e1e2f")
quality_frame.pack(pady=10)

Label(quality_frame, text="الجودة:", font="arial 12 bold", bg="#1e1e2f", fg="white").pack(side=LEFT, padx=5)
quality_menu = ttk.Combobox(quality_frame, textvariable=quality_var, state="readonly", width=10)
quality_menu.pack(side=LEFT)

# مكان الحفظ
path_frame = Frame(root, bg="#1e1e2f")
path_frame.pack(pady=10, padx=30, fill="x")

Label(path_frame, text="مكان الحفظ:", font="arial 11 bold", bg="#1e1e2f", fg="white").pack(side=LEFT)
Label(path_frame, textvariable=path_var, font="arial 9", bg="#1e1e2f", fg="#aaaaaa").pack(side=LEFT, padx=5)
Button(path_frame, text="تغيير", font="arial 9", command=choose_folder).pack(side=RIGHT)

# زرار التحميل
download_button = Button(
    root, text="⬇  تحميل الفيديو", font="arial 14 bold",
    bg="#e63946", fg="white", command=download_video, width=20
)
download_button.pack(pady=20)

# شريط التقدم
progress_bar = ttk.Progressbar(root, length=460, mode="determinate")
progress_bar.pack(pady=5)

# رسالة الحالة
Label(root, textvariable=status_var, font="arial 10", bg="#1e1e2f", fg="#ffb703").pack(pady=10)

root.mainloop()