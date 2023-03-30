from flask_cors import CORS
from flask import Flask, request, jsonify
import Service.ValidateCodeService as ValidateCodeService

app = Flask(__name__)
CORS(app)  # 使用默认的配置允许所有来源的跨域请求

@app.route('/getValidateCodeImage', methods=['POST'])
def validate():
    
    code = request.args.get('code')
    response = {
        "status": "200",
        "data": ValidateCodeService.generateValidateCodeImage(code),
        "message": "test"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0")