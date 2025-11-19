import time
import requests
import sys

def keep_alive(url):
    print(f"Starting keep-alive for {url}...")
    while True:
        try:
            response = requests.get(url)
            print(f"[{time.ctime()}] Pinged {url}: {response.status_code}")
        except Exception as e:
            print(f"[{time.ctime()}] Error pinging {url}: {e}")
        
        # Sleep for 14 minutes (14 * 60 seconds)
        time.sleep(14 * 60)

if __name__ == "__main__":
    # Default to localhost if no URL provided
    url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000/health"
    keep_alive(url)
