Python
import socket
from concurrent.futures import ThreadPoolExecutor
import urllib3

proxies_list = [
// there but the proxy + port 
//made by Sulaiman alnathir
//ig:s_k518
"111.111.11.11:111"
]

valid_proxies = []

def check_proxy(proxy):
    proxy = proxy.strip()
    protocols = ['socks5', 'socks4', 'http']
    for proto in protocols:
        try:
            if proto in ['socks5', 'socks4']:
                from urllib3.contrib.socks import SOCKSProxyManager
                pm = SOCKSProxyManager(f"{proto}://{proxy}", timeout=4.0)
            else:
                pm = urllib3.ProxyManager(f"http://{proxy}", timeout=4.0)
            
            response = pm.request('GET', 'https://httpbin.org/ip', retries=False)
            if response.status == 200:
                print(proxy)
                valid_proxies.append(proxy)
                return
        except Exception:
            pass

def main():
    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(check_proxy, proxies_list)
        
    with open("live_proxies.txt", "w") as f:
        for proxy in valid_proxies:
            f.write(f"{proxy}\n")

if __name__ == "__main__":
    main()
