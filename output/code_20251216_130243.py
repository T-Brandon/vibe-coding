# app.py
import logging
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "coffee_secret_key"

# 로깅 설정
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# 임시 주문 내역 저장소
orders = []


@app.route("/")
def index():
    try:
        return render_template("index.html")
    except Exception as e:
        logging.error(f"메인 페이지 로드 실패: {e}")
        return "페이지 로드 중 오류가 발생했습니다.", 500


@app.route("/order", methods=["POST"])
def order():
    try:
        customer = request.form.get("customer")
        coffee = request.form.get("coffee")
        size = request.form.get("size")
        qty = int(request.form.get("quantity", 1))

        if not (customer and coffee and size):
            flash("모든 필드를 입력해주세요.", "error")
            return redirect(url_for("index"))

        order_data = {
            "customer": customer,
            "coffee": coffee,
            "size": size,
            "quantity": qty
        }
        orders.append(order_data)
        logging.info(f"주문 접수: {order_data}")
        flash("주문이 성공적으로 접수되었습니다.", "success")
        return redirect(url_for("orders_list"))
    except Exception as e:
        logging.error(f"주문 처리 실패: {e}")
        flash("주문 처리 중 오류가 발생했습니다.", "error")
        return redirect(url_for("index"))


@app.route("/orders")
def orders_list():
    try:
        return render_template("orders.html", orders=orders)
    except Exception as e:
        logging.error(f"주문 내역 페이지 로드 실패: {e}")
        return "주문 내역 로드 중 오류가 발생했습니다.", 500


if __name__ == "__main__":
    app.run(debug=True)