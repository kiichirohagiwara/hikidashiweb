from flask import *
import math
import pandas

# Flaskオブジェクトの生成
app = Flask(__name__)

# ルート( / )へアクセスがあった時 --- (*1)
@app.route("/")
def root():
    # HTMLでWebフォームを記述 --- (*2)
    return """
    <html><body>
    <form action="/kekka" method="post">
        <label for="name">想定年利:</label>
        <input type="text" name="ry">
        <br>
        <label for="name">元本:</label>
        <input type="text" name="ganpon">
        <br>
        <label for="name">運用年数:</label>
        <input type="text" name="year">
        <br>
        <label for="name">毎月引き出したい金額:</label>
        <input type="text" name="hikidashi">
        <br>
        <input type="submit" value="計算">
        
    </form>
    """

# フォームの値を受け取って結果を表示 --- (*3)
@app.route("/kekka", methods=["post"])

def kekka():
    ry = float(request.form.get("ry"))
    ganpon = int(request.form.get("ganpon"))
    year = int(request.form.get("year"))
    hikidashi = int(request.form.get("hikidashi"))
    rm = ((1 + ry / 100) ** (1 / 12) - 1)
    month = year * 12
    zandaka = ganpon
    export_l = []
    while zandaka >0:
        zougen = (ganpon *(rm) - hikidashi)
        for i in range(month):
            zandaka = zandaka + zougen
        zandaka = math.floor(zandaka)
        export_l.append("元本" +str(ganpon) +"円を" + "年利" +str(ry) + "%で運用した場合" +"毎月" + str(hikidashi) + "円引き出すと" +str(year)+ "年後に" +str(zandaka) +"円の残高です<br>")
        if zandaka > 0:
            zandaka = ganpon
            hikidashi = hikidashi + 1000
    export_html = ''.join(export_l)
    return export_html

# サーバーを起動
if __name__ == "__main__":
    app.run(debug=True, port=8888)