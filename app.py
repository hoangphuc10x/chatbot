from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS để xử lý cross-origin requests
import json
import random  # Dùng để chọn câu trả lời ngẫu nhiên

# Khởi tạo Flask app
app = Flask(__name__)
CORS(app)  # Bật CORS cho toàn bộ ứng dụng

# Đảm bảo JSON hiển thị tiếng Việt đúng định dạng
app.config['JSON_AS_ASCII'] = False

# Load dữ liệu intents từ file JSON
def load_intents():
    try:
        with open('intents.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print("Lỗi khi đọc file intents.json:", e)
        return {"intents": []}

# Load intents lúc khởi động server
intents = load_intents()

# Hàm tìm câu trả lời dựa trên input người dùng
def get_response(user_message):
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in user_message.lower():  # So khớp không phân biệt hoa/thường
                return random.choice(intent['responses'])  # Trả về câu trả lời ngẫu nhiên
    return "Xin lỗi, tôi không hiểu bạn đang nói gì."

# Route chính để xử lý API chat
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()  # Nhận dữ liệu JSON từ frontend
        print("Request từ client:", data)  # Log request gửi đến server

        user_message = data.get('message', '').strip()
        if not user_message:  # Kiểm tra input trống
            return jsonify({"response": "Bạn chưa nhập tin nhắn."}), 400

        # Lấy response từ hàm xử lý
        response = get_response(user_message)
        print("Response gửi lại client:", response)  # Log response trả về

        return jsonify({"response": response})  # Trả về JSON

    except Exception as e:
        print("Lỗi xử lý request:", e)  # Log lỗi
        return jsonify({"response": "Đã xảy ra lỗi trên server. Vui lòng thử lại sau."}), 500

# Chạy server Flask
if __name__ == '__main__':
    print("Server đang chạy tại http://127.0.0.1:5000/")
    app.run(debug=True)
