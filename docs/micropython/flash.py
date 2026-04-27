import sys
import esptool
import serial.tools.list_ports

# Download the current .bin file for your board from
# https://micropython.org/download/
FIRMWARE_PATH = "esp32s3-firmware.bin"
BAUD_RATE = "460800"

def find_esp32_s3_port():
    print("Searching for ESP32-S3...")
    ports = serial.tools.list_ports.comports()
        for port in ports:
        if port.vid == 0x303a or "Espressif" in (port.manufacturer or ""):
            print(f"Detected {port.manufacturer} device on {port.device}")
            return port.device            
    return None

def run_flash_sequence():
    port = find_esp32_s3_port()
    if not port:
        print("Error: No ESP32-S3 detected. Check your USB cable!")
        return
    try:
        print(f"\n>>> Erasing flash on {port}...")
        esptool.main(['--chip', 'esp32s3', '--port', port,'erase_flash'])
        print(f"\n>>> Flashing {FIRMWARE_PATH} to {port}...")
        esptool.main(['--chip', 'esp32s3', '--port', port, '--baud', BAUD_RATE, 'write_flash', '-z', '0x0', FIRMWARE_PATH])
        print("SUCCESS: ESP32-S3 is ready!")
    except Exception as e:
        print(f"\nFLASH FAILED: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_flash_sequence()
