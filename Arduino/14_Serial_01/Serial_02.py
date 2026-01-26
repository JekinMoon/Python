import serial # pyserial 라이브러리
import time
from flask import Flask, request, jsonify
from flask_cors import CORS

SERIAL_PORT = 'COM3'
BAUD = 9600

arduino = serial.Serial(SERIAL_PORT, BAUD)
time.sleep(2)

app =  Flask(__name__)
CORS(app)
state = "off"

@app.post("/led")
def led():
    global state
    data = request.get_json(force=True)
    desired = data.get("state")

    if desired == "on":
        arduino.write(b'1')     # 1을 바이트 형태로 보내라는 뜻
        state = "on"
    elif desired == "off":
        arduino.write(b'0')     # 0을 바이트 형태로 보내라는 뜻
        state = "off"
    else:
        # jsonify 메서드는 매개변수로 받은 값을 json 형태로 변환해 줌
        return jsonify({"전송": False, "에러": "state는 'on'이나 'off'만 가능합니다."}), 400
    
    # if나 elif문이 true인 경우에만 실행될 return문
    return jsonify({"전송": True, "state": state})

    # 예를 들어서 desired == "on"일 때는 jsonify({"전송": True, "state": "on"})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    