from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    text = request.form['text']

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save('static/qrcode.png')

    return render_template('result.html')
if __name__ == "__main__":
    app.run(port=3000, debug=True)


