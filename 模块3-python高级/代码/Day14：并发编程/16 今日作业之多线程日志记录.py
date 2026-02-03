import threading
import time


def log_worker(file, level, interval):
    while 1:
        timestamp = time.time()
        msg = f"Log Message with level {level}"
        log_entry = f"{timestamp} - [{level}:{msg}]"
        with open(file, "a") as f:
            f.write(log_entry)
        time.sleep(interval)


def main():
    path = "logs.log"
    info_thread = threading.Thread(target=log_worker, args=(path, "INFO", 1))
    warning_thread = threading.Thread(target=log_worker, args=(path, "WARNING", 3))
    error_thread = threading.Thread(target=log_worker, args=(path, "ERROR", 5))
    info_thread.start()
    warning_thread.start()
    error_thread.start()

    info_thread.join()
    warning_thread.join()
    error_thread.join()


if __name__ == '__main__':
    main()
