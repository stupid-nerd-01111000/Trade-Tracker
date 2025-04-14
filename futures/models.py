from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Entry
    entry_time = db.Column(db.String(20))
    entry_date = db.Column(db.String(20))
    exchange = db.Column(db.String(50))
    entry_type = db.Column(db.String(20))
    symbol = db.Column(db.String(20))
    strategy = db.Column(db.String(50))
    side = db.Column(db.String(10))
    entry_price = db.Column(db.Float)
    margin = db.Column(db.Float)
    leverage = db.Column(db.Integer)
    order_type = db.Column(db.String(20))
    time_frame = db.Column(db.String(20))
    entry_fee_rate = db.Column(db.Float)
    entry_mental_state = db.Column(db.Text)
    entry_screenshot_link = db.Column(db.String(255))
    check_list = db.Column(db.Text)

    stop_loss_price = db.Column(db.Float)
    take_profit_price = db.Column(db.Float)

    # Exit
    actual_exit_price = db.Column(db.Float)
    percent_margin_close = db.Column(db.Float)
    exit_type = db.Column(db.String(10))
    exit_fee_rate = db.Column(db.Float)
    exit_time = db.Column(db.String(20))
    exit_date = db.Column(db.String(20))
    exit_mental_state = db.Column(db.Text)
    exit_screenshot_link = db.Column(db.String(255))
