from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models import db, Trade, Status

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/form')
def form():
    return render_template("form.html")


@app.route('/submit', methods=["POST"])
def submit():
    data = request.form

    trade = Trade(
        entry_time=data.get("entry_time"),
        entry_date=data.get("entry_date"),
        exchange=data.get("exchange"),
        entry_type=data.get("entry_type"),
        symbol=data.get("symbol"),
        strategy=data.get("strategy"),
        side=data.get("side"),
        entry_price=data.get("entry_price"),
        margin=data.get("margin"),
        leverage=data.get("leverage"),
        order_type=data.get("order_type"),
        time_frame=data.get("time_frame"),
        entry_fee_rate=data.get("entry_fee_rate"),
        entry_mental_state=data.get("entry_mental_state"),
        entry_screenshot_link=data.get("entry_screenshot_link"),
        check_list=data.get("check_list"),
        stop_loss_price=data.get("stop_loss_price"),
        take_profit_price=data.get("take_profit_price"),
        actual_exit_price=data.get("actual_exit_price"),
        percent_margin_close=data.get("percent_margin_close"),
        exit_type=data.get("exit_type"),
        exit_fee_rate=data.get("exit_fee_rate"),
        exit_time=data.get("exit_time"),
        exit_date=data.get("exit_date"),
        exit_mental_state=data.get("exit_mental_state"),
        exit_screenshot_link=data.get("exit_screenshot_link")
    )

    db.session.add(trade)
    db.session.commit()
    return redirect(url_for('logs'))


@app.route("/logs")
def logs():
    trades = Trade.query.all()
    return render_template("logs.html", trades=trades)


@app.route("/status", methods=['GET', 'POST'])
def create_status():
    if request.method == 'POST':
        new_status = Status(
            pair=request.form['pair'].lower(),
            exchange=request.form['exchange'].lower(),
            fee_percent=float(request.form['fee_percent']),
            year=int(request.form['year']),
            mental_state=request.form['mental_state'].lower(),
            strategy=request.form['strategy'].lower(),
            mistake=request.form['mistake'].lower(),
            tracking=request.form['tracking'].lower(),
            check_item=request.form['check_item'].lower(),
            time_frame=request.form['time_frame'].lower()
        )
        db.session.add(new_status)
        db.session.commit()

    # Fetching status data from the database (you can adjust this query as needed)
    status_data = {
        'pair': ['btc_usdt', 'eth_usdt'],  # Example, replace with dynamic data fetching
        'exchange': ['binance', 'coinbase'],
        'fee_percent': [0.1, 0.2],
        'year': [2025, 2026],
        'mental_state': ['focused', 'stressed'],
        'strategy': ['long', 'short'],
        'mistake': ['none', 'emotional'],
        'tracking': ['manual', 'automatic'],
        'check_item': ['verified', 'unchecked'],
        'time_frame': ['1h', '4h']
    }

    return render_template('status.html', data=status_data)


if __name__ == '__main__':
    app.run(debug=True)
