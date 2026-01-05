from flask import Flask, request, render_template_string
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# HTML 템플릿 (간단한 주문 폼)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>커피 주문</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .container { max-width: 400px; margin: auto; padding: 20px; border: 1px solid #ccc; }
        label { display: block; margin: 10px 0 5px; }
        input, select, button { padding: 8px; margin: 5px 0; width: 100%; }
        button { background: #4CAF50; color: white; border: none; cursor: pointer; }
        button:hover { background: #45a049; }
    </style>
</head>
<body>
    <div class="container">
        <h2>☕ 커피 주문하기</h2>
        <form method="POST" action="/order">
            <label for="name">이름:</label>
            <input type="text" id="name" name="name" required>

            <label for="coffee">커피 종류:</label>
            <select id="coffee" name="coffee" required>
                <option value="아메리카노">아메리카노</option>
                <option value="카페라떼">카페라떼</option>
                <option value="카푸치노">카푸치노</option>
                <option value="에스프레소">에스프레소</option>
            </select>

            <label for="size">사이즈:</label>
            <select id="size" name="size" required>
                <option value="S">S</option>
                <option value="M">M</option>
                <option value="L">L</option>
            </select>

            <label for="sugar">설탕:</label>
            <select id="sugar" name="sugar" required>
                <option value="없음">없음</option>
                <option value="1스푼">1스푼</option>
                <option value="2스푼">2스푼</option>
            </select>

            <button type="submit">주문하기</button>
        </form>
    </div>
</body>
</html>
"""

ORDER_CONFIRMATION_TEMPLATE = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>주문 완료</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; text-align: center; }
        .container { max-width: 400px; margin: auto; padding: 20px; border: 1px solid #ccc; }
        h2 { color: #4CAF50; }
        p { font-size: 16px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>✅ 주문이 완료되었습니다!</h2>
        <p><strong>이름:</strong> {{ name }}</p>
        <p><strong>메뉴:</strong> {{ coffee }} ({{ size }})</p>
        <p><strong>설탕:</strong> {{ sugar }}</p>
        <p>주문해 주셔서 감사합니다. 곧 준비해 드리겠습니다!</p>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    """주문 폼 페이지"""
    logger.info("주문 폼 페이지 요청")
    return render_template_string(HTML_TEMPLATE)

@app.route('/order', methods=['POST'])
def order():
    """주문 처리"""
    try:
        name = request.form.get('name', '').strip()
        coffee = request.form.get('coffee', '')
        size = request.form.get('size', '')
        sugar = request.form.get('sugar', '')

        if not name or not coffee or not size or not sugar:
            logger.warning("주문 정보 누락: %s, %s, %s, %s", name, coffee, size, sugar)
            return "모든 항목을 입력해 주세요.", 400

        logger.info("주문 접수: %s, %s, %s, %s", name, coffee, size, sugar)

        return render_template_string(
            ORDER_CONFIRMATION_TEMPLATE,
            name=name,
            coffee=coffee,
            size=size,
            sugar=sugar
        )

    except Exception as e:
        logger.error("주문 처리 중 오류 발생: %s", str(e))
        return "주문 처리 중 오류가 발생했습니다.", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)