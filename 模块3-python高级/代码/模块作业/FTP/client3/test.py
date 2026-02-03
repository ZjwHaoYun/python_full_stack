import time


def show_progress(current, total):
    bar_length = 100
    filled_length = int(bar_length * current / total)
    percent = round(100.0 * current / total, 1)

    bar = "=" * filled_length + "-" * (bar_length - filled_length)
    progress_msg = f"\r[{bar}{percent}]"
    print(progress_msg, end="")


for i in range(1, 101):
    show_progress(i, 100)
    time.sleep(1)
