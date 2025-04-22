import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\n""tante...", 0.08),
        ("sudah terbiasa terjadi tante", 0.09),
        ("teman datang ketika lagi butuh saja", 0.08),
        ("coba kalau lagi susah", 0.15),
        ("mereka semua menghilaaaaang""\n", 0.15),   
    ]
    delays = [0.3, 2.5, 5.8, 9.5, 13.5]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()
        
if __name__ == "__main__":
    sing_song()