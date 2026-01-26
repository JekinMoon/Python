import serial # pyserial 라이브러리
import time

# COM3 : 아두이노 시리얼 연결 포트 (노트북, 환경마다 숫자 다름)
arduino = serial.Serial("COM3", 9600)
time.sleep(1) # 안정적인 통신을 위한 1초 딜레이 

print("'1'을 입력하면 LED ON / '0'을 입력하면 LED OFF ")
print("다른 값을 입력하면 프로그램 종료")

while 1:
    var = input() # 터미널에서 문자열 입력받음

    if var == "1":
        var = var.encode("utf-8")
        arduino.write(var)  # 입력받은 var 값을 아두이노로 보냄
        print("LED ON")
        time.sleep(1)
    elif var == "0":
        var = var.encode("utf-8")
        arduino.write(var)  # 입력받은 var 값을 아두이노로 보냄
        print("LED OFF")
        time.sleep(1)
    else:
        break
    