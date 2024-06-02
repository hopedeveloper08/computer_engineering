from django.db import models
from .coinmarketcap_token import token
import requests
import yfinance as yf
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
import os
from ta.trend import SMAIndicator, EMAIndicator, MACD, ADXIndicator, IchimokuIndicator
from ta.momentum import RSIIndicator, StochasticOscillator
from ta.volatility import BollingerBands, AverageTrueRange
from ta.volume import OnBalanceVolumeIndicator, ChaikinMoneyFlowIndicator


class Currency(models.Model):
    symbol = models.CharField(max_length=4)

    def __str__(self):
        return self.symbol

    @classmethod
    def supported_currencies(cls):
        return list(map(lambda x: x.symbol, cls.objects.all()))

    def current_price(self):
        return yf.download(f'{self.symbol}-USD', period='1D')['Adj Close'].values[0]

    @staticmethod
    def draw_chart(symbol):
        flag = True
        while flag:
            try:
                df = yf.download(f'{symbol}-USD', period='6mo', interval='1d')
                df.reset_index(inplace=True)
                df['Date'] = df['Date'].map(mdates.date2num)
                ohlc = df[['Date', 'Open', 'High', 'Low', 'Close']]
                plt.style.use('ggplot')
                fig, ax = plt.subplots(figsize=(6, 4))
                candlestick_ohlc(ax, ohlc.values, width=0.8, colorup='g', colordown='r')

                ax.xaxis_date()
                ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
                plt.xticks(rotation=45)
                plt.grid(True)
                plt.tight_layout()

                fig.savefig(os.path.join(os.getcwd(), 'static/chart.png'), dpi=100)
                plt.close(fig)

                flag = False
            except Exception as e:
                print(e)
                continue

    @classmethod
    def get_all_data(cls):
        all_currencies = cls.objects.all()
        symbols = ''

        for currency in all_currencies:
            symbols += currency.symbol + ','

        if symbols == '':
            return None

        url = f'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest?symbol={symbols}&convert=USD'
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': token,
        }

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return None

        data = response.json()['data']

        filter_data = Currency.__filter_data(data)

        return filter_data

    @staticmethod
    def __filter_data(data):
        filtered_data = []
        for symbol, item in data.items():
            require_data = dict()
            item = item[0]

            require_data['name'] = item['name']
            require_data['symbol'] = symbol
            require_data['logo_url'] = Currency.__get_logo_url(item['id'])

            item = item['quote']['USD']
            require_data['price'] = item['price']
            require_data['volume_change_24h'] = item['volume_change_24h']
            require_data['percent_change_1h'] = item['percent_change_1h']
            require_data['percent_change_24h'] = item['percent_change_24h']
            require_data['percent_change_7d'] = item['percent_change_7d']
            require_data['percent_change_30d'] = item['percent_change_30d']
            require_data['market_cap'] = item['market_cap']
            require_data['market_cap_dominance'] = item['market_cap_dominance']

            filtered_data.append(require_data)

        filtered_data = sorted(filtered_data, key=lambda x: x['market_cap_dominance'], reverse=True)
        return filtered_data

    @staticmethod
    def __get_logo_url(id_):
        return f'https://s2.coinmarketcap.com/static/img/coins/32x32/{id_}.png'

    @staticmethod
    def signal(symbol):
        df = yf.download(f'{symbol}-USD', period='6mo', interval='1d')

        sma = SMAIndicator(close=df['Close'], window=20)
        df['SMA'] = sma.sma_indicator()
        sma_is_buy = df['Close'].iloc[-1] > df['SMA'].iloc[-1]
        sma_is_sell = df['Close'].iloc[-1] < df['SMA'].iloc[-1]

        ema = EMAIndicator(close=df['Close'], window=20)
        df['EMA'] = ema.ema_indicator()
        ema_is_buy = df['Close'].iloc[-1] > df['EMA'].iloc[-1]
        ema_is_sell = df['Close'].iloc[-1] < df['EMA'].iloc[-1]

        macd = MACD(close=df['Close'])
        df['MACD'] = macd.macd()
        df['MACD_Signal'] = macd.macd_signal()
        macd_is_buy = df['MACD'].iloc[-1] > df['MACD_Signal'].iloc[-1]
        macd_is_sell = df['MACD'].iloc[-1] < df['MACD_Signal'].iloc[-1]

        adx = ADXIndicator(high=df['High'], low=df['Low'], close=df['Close'], window=14)
        df['ADX'] = adx.adx()
        adx_is_buy = df['ADX'].iloc[-1] > 25 and df['Close'].iloc[-1] > df['Close'].iloc[-2]
        adx_is_sell = df['ADX'].iloc[-1] > 25 and df['Close'].iloc[-1] < df['Close'].iloc[-2]

        # محاسبه RSI
        rsi = RSIIndicator(close=df['Close'], window=14)
        df['RSI'] = rsi.rsi()
        rsi_is_buy = df['RSI'].iloc[-1] < 30
        rsi_is_sell = df['RSI'].iloc[-1] > 70

        stochastic = StochasticOscillator(high=df['High'], low=df['Low'], close=df['Close'], window=14, smooth_window=3)
        df['Stochastic'] = stochastic.stoch()
        df['Stochastic_Signal'] = stochastic.stoch_signal()
        stochastic_is_buy = df['Stochastic'].iloc[-1] < 20 and df['Stochastic'].iloc[-1] > df['Stochastic_Signal'].iloc[
            -1]
        stochastic_is_sell = df['Stochastic'].iloc[-1] > 80 and df['Stochastic'].iloc[-1] < \
                             df['Stochastic_Signal'].iloc[-1]

        bb = BollingerBands(close=df['Close'], window=20, window_dev=2)
        df['BB_High'] = bb.bollinger_hband()
        df['BB_Low'] = bb.bollinger_lband()
        bb_is_buy = df['Close'].iloc[-1] < df['BB_Low'].iloc[-1]
        bb_is_sell = df['Close'].iloc[-1] > df['BB_High'].iloc[-1]

        atr = AverageTrueRange(high=df['High'], low=df['Low'], close=df['Close'], window=14)
        df['ATR'] = atr.average_true_range()
        atr_is_buy = df['Close'].iloc[-1] < df['Close'].iloc[-1] - df['ATR'].iloc[-1]
        atr_is_sell = df['Close'].iloc[-1] > df['Close'].iloc[-1] + df['ATR'].iloc[-1]

        obv = OnBalanceVolumeIndicator(close=df['Close'], volume=df['Volume'])
        df['OBV'] = obv.on_balance_volume()
        obv_is_buy = df['OBV'].iloc[-1] > df['OBV'].iloc[-2]
        obv_is_sell = df['OBV'].iloc[-1] < df['OBV'].iloc[-2]

        cmf = ChaikinMoneyFlowIndicator(high=df['High'], low=df['Low'], close=df['Close'], volume=df['Volume'],
                                        window=20)
        df['CMF'] = cmf.chaikin_money_flow()
        cmf_is_buy = df['CMF'].iloc[-1] > 0
        cmf_is_sell = df['CMF'].iloc[-1] < 0

        ichimoku = IchimokuIndicator(high=df['High'], low=df['Low'], window1=9, window2=26, window3=52, visual=False)
        df['tenkan_sen'] = ichimoku.ichimoku_conversion_line()
        df['kijun_sen'] = ichimoku.ichimoku_base_line()
        df['senkou_span_a'] = ichimoku.ichimoku_a()
        df['senkou_span_b'] = ichimoku.ichimoku_b()
        ichimoku_is_buy = df['senkou_span_a'].iloc[-1] > df['senkou_span_b'].iloc[-1] and df['Close'].iloc[-1] > max(
            df['senkou_span_a'].iloc[-1], df['senkou_span_b'].iloc[-1])
        ichimoku_is_sell = df['senkou_span_a'].iloc[-1] < df['senkou_span_b'].iloc[-1] and df['Close'].iloc[-1] < min(
            df['senkou_span_a'].iloc[-1], df['senkou_span_b'].iloc[-1])

        signals = {
            'SMA': {'is_buy': sma_is_buy, 'is_sell': sma_is_sell},
            'EMA': {'is_buy': ema_is_buy, 'is_sell': ema_is_sell},
            'MACD': {'is_buy': macd_is_buy, 'is_sell': macd_is_sell},
            'ADX': {'is_buy': adx_is_buy, 'is_sell': adx_is_sell},
            'RSI': {'is_buy': rsi_is_buy, 'is_sell': rsi_is_sell},
            'Stochastic': {'is_buy': stochastic_is_buy, 'is_sell': stochastic_is_sell},
            'BollingerBands': {'is_buy': bb_is_buy, 'is_sell': bb_is_sell},
            'ATR': {'is_buy': atr_is_buy, 'is_sell': atr_is_sell},
            'OBV': {'is_buy': obv_is_buy, 'is_sell': obv_is_sell},
            'CMF': {'is_buy': cmf_is_buy, 'is_sell': cmf_is_sell},
            'Ichimoku': {'is_buy': ichimoku_is_buy, 'is_sell': ichimoku_is_sell}
        }

        return signals
