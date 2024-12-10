from flask import Flask, request, jsonify
import json
import random  # Thêm thư viện random để chọn câu trả lời ngẫu nhiên

app = Flask(__name__)

# Đảm bảo nội dung JSON được mã hóa chính xác
app.config['JSON_AS_ASCII'] = False

# Load intents từ file JSON
def load_intents():
    with open('intents.json', 'r', encoding='utf-8') as file:
        return json.load(file)

intents = load_intents()

# Hàm để xử lý message của người dùng
def get_response(user_message):
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in user_message.lower():  # So khớp không phân biệt hoa/thường
                # Random chọn một câu trả lời từ responses
                return random.choice(intent['responses'])
    return "Xin lỗi, tôi không hiểu bạn đang nói gì."

# Route chính để xử lý API
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()  # Lấy dữ liệu JSON từ request
    user_message = data.get('message', '').strip()  # Lấy thông điệp người dùng

    if not user_message:  # Nếu không có thông điệp
        return jsonify({"response": "Bạn chưa nhập tin nhắn."}), 400

    response = get_response(user_message)
    return jsonify({"response": response})

# Chạy server
if __name__ == '__main__':
    app.run(debug=True)
