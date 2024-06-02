from django.shortcuts import render
from .models import Currency


LAST_DATA = None


def overview(request):
    global LAST_DATA

    # data = Currency.get_all_data()
    # LAST_DATA = data
    # context = {
    #     'data': data,
    # }

    context = {'data': [{'name': 'Bitcoin', 'symbol': 'BTC', 'logo_url': 'https://s2.coinmarketcap.com/static/img/coins/32x32/1.png', 'price': 67712.22618373127, 'volume_change_24h': -53.8125, 'percent_change_1h': 0.07076707, 'percent_change_24h': 0.22159051, 'percent_change_7d': -2.14597332, 'percent_change_30d': 14.04367342, 'market_cap': 1334372678095.3547, 'market_cap_dominance': 53.1785}, {'name': 'Ethereum', 'symbol': 'ETH', 'logo_url': 'https://s2.coinmarketcap.com/static/img/coins/32x32/1027.png', 'price': 3801.151979652443, 'volume_change_24h': -39.0803, 'percent_change_1h': 0.08516496, 'percent_change_24h': 0.72570967, 'percent_change_7d': 1.21858504, 'percent_change_30d': 26.69161468, 'market_cap': 456678346030.4799, 'market_cap_dominance': 18.0294}, {'name': 'Tether USDt', 'symbol': 'USDT', 'logo_url': 'https://s2.coinmarketcap.com/static/img/coins/32x32/825.png', 'price': 0.9992776954370063, 'volume_change_24h': -40.1946, 'percent_change_1h': 0.01323949, 'percent_change_24h': 0.04457851, 'percent_change_7d': -0.06022357, 'percent_change_30d': -0.08943894, 'market_cap': 112060340532.61472, 'market_cap_dominance': 4.4241}, {'name': 'BNB', 'symbol': 'BNB', 'logo_url': 'https://s2.coinmarketcap.com/static/img/coins/32x32/1839.png', 'price': 597.2736143361624, 'volume_change_24h': -13.3271, 'percent_change_1h': 0.18158299, 'percent_change_24h': 0.62575837, 'percent_change_7d': -0.82828825, 'percent_change_30d': 6.0594405, 'market_cap': 88148781971.58064, 'market_cap_dominance': 3.4801}, {'name': 'Solana', 'symbol': 'SOL', 'logo_url': 'https://s2.coinmarketcap.com/static/img/coins/32x32/5426.png', 'price': 167.47191993815076, 'volume_change_24h': -55.7132, 'percent_change_1h': 0.15003661, 'percent_change_24h': 0.87080584, 'percent_change_7d': 0.10120957, 'percent_change_30d': 21.26674175, 'market_cap': 76986104265.87823, 'market_cap_dominance': 3.0394}, {'name': 'XRP', 'symbol': 'XRP', 'logo_url': 'https://s2.coinmarketcap.com/static/img/coins/32x32/52.png', 'price': 0.5194854619438914, 'volume_change_24h': -52.9838, 'percent_change_1h': 0.17794214, 'percent_change_24h': 0.44773759, 'percent_change_7d': -3.78348077, 'percent_change_30d': -0.9096239, 'market_cap': 28805655332.53689, 'market_cap_dominance': 1.1372}, {'name': 'Dogecoin', 'symbol': 'DOGE', 'logo_url': 'https://s2.coinmarketcap.com/static/img/coins/32x32/74.png', 'price': 0.16079614350641333, 'volume_change_24h': -44.2684, 'percent_change_1h': 0.13582928, 'percent_change_24h': 1.17152432, 'percent_change_7d': -5.79865151, 'percent_change_30d': 20.89234689, 'market_cap': 23240489928.532475, 'market_cap_dominance': 0.9175}, {'name': 'Cardano', 'symbol': 'ADA', 'logo_url': 'https://s2.coinmarketcap.com/static/img/coins/32x32/2010.png', 'price': 0.4493437040142221, 'volume_change_24h': -40.898, 'percent_change_1h': 0.12195974, 'percent_change_24h': 0.1310274, 'percent_change_7d': -2.34679445, 'percent_change_30d': -1.47964061, 'market_cap': 16042116479.849434, 'market_cap_dominance': 0.6333}, {'name': 'Shiba Inu', 'symbol': 'SHIB', 'logo_url': 'https://s2.coinmarketcap.com/static/img/coins/32x32/5994.png', 'price': 2.531918580303857e-05, 'volume_change_24h': -56.9959, 'percent_change_1h': 0.02370018, 'percent_change_24h': -0.69398785, 'percent_change_7d': 1.72496883, 'percent_change_30d': 9.62294115, 'market_cap': 14919882852.91832, 'market_cap_dominance': 0.589}, {'name': 'Avalanche', 'symbol': 'AVAX', 'logo_url': 'https://s2.coinmarketcap.com/static/img/coins/32x32/5805.png', 'price': 35.96005469465213, 'volume_change_24h': -46.6812, 'percent_change_1h': 0.14736007, 'percent_change_24h': -0.33932457, 'percent_change_7d': -5.48616939, 'percent_change_30d': 6.47681037, 'market_cap': 14136368248.141579, 'market_cap_dominance': 0.5581}, {'name': 'Chainlink', 'symbol': 'LINK', 'logo_url': 'https://s2.coinmarketcap.com/static/img/coins/32x32/1975.png', 'price': 18.472828496724528, 'volume_change_24h': -19.8741, 'percent_change_1h': -0.45834137, 'percent_change_24h': 1.17162107, 'percent_change_7d': 6.43172821, 'percent_change_30d': 34.91332425, 'market_cap': 10845397064.606367, 'market_cap_dominance': 0.4282}, {'name': 'Polkadot', 'symbol': 'DOT', 'logo_url': 'https://s2.coinmarketcap.com/static/img/coins/32x32/6636.png', 'price': 7.076654320377951, 'volume_change_24h': -28.5976, 'percent_change_1h': 0.12238001, 'percent_change_24h': 1.41567027, 'percent_change_7d': -3.95002851, 'percent_change_30d': -2.92234554, 'market_cap': 10175899362.593748, 'market_cap_dominance': 0.4017}, {'name': 'TRON', 'symbol': 'TRX', 'logo_url': 'https://s2.coinmarketcap.com/static/img/coins/32x32/1958.png', 'price': 0.11276426650781576, 'volume_change_24h': -29.3598, 'percent_change_1h': 0.10243077, 'percent_change_24h': 0.5828691, 'percent_change_7d': -0.67236857, 'percent_change_30d': -8.26439769, 'market_cap': 9852103222.800037, 'market_cap_dominance': 0.389}, {'name': 'Litecoin', 'symbol': 'LTC', 'logo_url': 'https://s2.coinmarketcap.com/static/img/coins/32x32/2.png', 'price': 83.30757857583656, 'volume_change_24h': -33.9619, 'percent_change_1h': 0.08690105, 'percent_change_24h': -0.30584249, 'percent_change_7d': -1.93200985, 'percent_change_30d': 3.20409542, 'market_cap': 6214353283.594813, 'market_cap_dominance': 0.2453}, {'name': 'Internet Computer', 'symbol': 'ICP', 'logo_url': 'https://s2.coinmarketcap.com/static/img/coins/32x32/8916.png', 'price': 12.066599465095985, 'volume_change_24h': -30.1723, 'percent_change_1h': 0.05274672, 'percent_change_24h': 1.75285265, 'percent_change_7d': -1.99800107, 'percent_change_30d': -9.5036104, 'market_cap': 5603640448.142826, 'market_cap_dominance': 0.2212}, {'name': 'Cosmos', 'symbol': 'ATOM', 'logo_url': 'https://s2.coinmarketcap.com/static/img/coins/32x32/3794.png', 'price': 8.331617514108567, 'volume_change_24h': -31.5902, 'percent_change_1h': 0.03702594, 'percent_change_24h': -0.34128889, 'percent_change_7d': -1.7642406, 'percent_change_30d': -3.86590018, 'market_cap': 3257084825.305814, 'market_cap_dominance': 0.1286}, {'name': 'Filecoin', 'symbol': 'FIL', 'logo_url': 'https://s2.coinmarketcap.com/static/img/coins/32x32/2280.png', 'price': 5.778153139384097, 'volume_change_24h': -37.514, 'percent_change_1h': 0.13123373, 'percent_change_24h': 0.82702721, 'percent_change_7d': -3.58414103, 'percent_change_30d': -2.86559491, 'market_cap': 3230137039.512201, 'market_cap_dominance': 0.1275}, {'name': 'Fantom', 'symbol': 'FTM', 'logo_url': 'https://s2.coinmarketcap.com/static/img/coins/32x32/3513.png', 'price': 0.7854013669386066, 'volume_change_24h': -53.2486, 'percent_change_1h': 0.37045026, 'percent_change_24h': -0.25460372, 'percent_change_7d': -3.5218896, 'percent_change_30d': 16.08915816, 'market_cap': 2201978632.2192817, 'market_cap_dominance': 0.0869}]}
    LAST_DATA = context['data']
    return render(request, 'overview.html', context)


def currency_info(request, symbol):
    global LAST_DATA
    if LAST_DATA is None:
        LAST_DATA = Currency.get_all_data()

    data = list(filter(lambda x: x['symbol'] == symbol, LAST_DATA))
    Currency.draw_chart(symbol)
    return render(request, 'currency_info.html', data[0])


def signal(request):
    global LAST_DATA
    context = None

    if request.method == 'POST':
        symbol = request.POST.get('symbol')
        symbol = symbol.upper()
        if LAST_DATA is None:
            LAST_DATA = Currency.get_all_data()

        data = list(filter(lambda x: x['symbol'] == symbol, LAST_DATA))[0]
        signals = Currency.signal(symbol)
        context = {
            'symbol': symbol,
            'signals': signals,
            'name': data['name'],
            'logo_url': data['logo_url'],
        }

    return render(request, 'signal.html', context)
