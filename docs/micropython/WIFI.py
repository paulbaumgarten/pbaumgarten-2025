import machine
import network
import utime
import ntptime
import ubinascii

class WIFI:
    def __init__(self, networks):
        self._networks = networks

    def scan(self, max_attempts=5):
        # Scan and prioritize visible networks
        all_networks = []
        print("[WIFI.scan] Scanning all SSID within range")
        for i in range(max_attempts):
            scan = self._wifi.scan()
            if scan:
                all_networks.extend(scan)
            utime.sleep(0.2)
        print(f"[WIFI.scan] Found {len(all_networks)} networks")
        return all_networks

    def connect(self):
        print("[WIFI.connect] Activating")
        self._wifi = network.WLAN(network.STA_IF)
        while not self._wifi.active():
            self._wifi.active(True)
            utime.sleep(0.1)
        # scan() returns (ssid, bssid, channel, RSSI, security, hidden)
        all_networks = self.scan()
        available = {ssid.decode('utf-8'): RSSI for ssid, bssid, channel, RSSI, security, hidden in all_networks}
        for ssid, password in self._networks:
            if ssid in available:
                print(f"[WIFI.connect] Found {ssid} (signal: {available[ssid]} dBm)")
                self._wifi.connect(ssid, password)
                for _ in range(10):  # 5-second timeout
                    if self._wifi.isconnected():
                        print(f"[WIFI.connect] Connected to {ssid}")
                        self._ip = self._wifi.ifconfig()[0]
                        self._ssid = ssid
                        self._password = password
                        return self._wifi.ifconfig()[0]
                    utime.sleep(0.5)
                print(f"[WIFI.connect] Failed to connect to {ssid}")
                self._wifi.disconnect()
        print("[WIFI.connect] No available networks - using offline mode")
        return False
    
    def reconnect(self):
        print("[WIFI.reconnect]")
        while not self._wifi.active():
            self._wifi.active(True)
            utime.sleep(0.1)
        if hasattr(self, '_ssid') and hasattr(self, '_password'):
            self._wifi.connect(self._ssid, self._password)
            for _ in range(10):  # 5-second timeout
                if self._wifi.isconnected():
                    print(f"[WIFI.reconnect] Connected to {self._ssid}")
                    self._ip = self._wifi.ifconfig()[0]
                    return self._wifi.ifconfig()[0]
                utime.sleep(0.5)
            print(f"[WIFI.reconnect] Failed to connect to {self._ssid}")
        # Fallback, perhaps we have changed location and need to switch networks
        print("[WIFI.reconnect] Handballing to connect()")
        return self.connect()

    def ntptime(self, timezone_offset=8, max_attempts=5):
        """Sync time via NTP and update RTC with timezone adjustment"""
        # Check WiFi connection state
        if not self._wifi.isconnected():
            print("[WIFI.ntptime] WiFi not connected")
            return False
        ip = self._wifi.ifconfig()[0]
        if ip == '0.0.0.0':
            print("[WIFI.ntptime] No valid IP address")
            return False
        # Try NTP sync
        for attempt in range(1, max_attempts+1):
            try:
                print(f"[WIFI.ntptime] attempt {attempt}/{max_attempts} to {ntptime.host}")
                ntptime.settime()
                break
            except Exception as e:
                print(f"[WIFI.ntptime] attempt {attempt}/{max_attempts} failed: {e}")
                if attempt == max_attempts:
                    return False
            utime.sleep(1)
        # Apply timezone and update RTC
        epoch = utime.time() + (timezone_offset * 3600)
        year, month, day, hour, min, sec, weekday, _ = utime.localtime(epoch)
        machine.RTC().datetime((
            year, month, day,
            (weekday + 1) % 7,  # RTC weekday (Sunday=0)
            hour, min, sec, 0
        ))
        print(f"[WIFI.ntptime] Time: {year:04}-{month:02}-{day:02} {hour:02}:{min:02}:{sec:02} UTC+{timezone_offset}")
        return True

    def _mac_to_str(self, mac_bytes):
        return ":".join("{:02X}".format(b) for b in mac_bytes)
    
    def status(self):
        print("[WIFI.status]")
        print("WiFi active:", self._wifi.active())  # Should be True
        print("WiFi channel:", self._wifi.config("channel"))  # Should show a number (1-14)
        print("ifconfig:", self._wifi.ifconfig())
        mac_bytes = self._wifi.config('mac')
        mac_address = ubinascii.hexlify(mac_bytes, ':').decode()
        print(f"MAC Address: {mac_address}")
        print(f"IP address: ",self._wifi.ifconfig()[0])
