# scanner.py
import requests
from config import SEARCH_TERMS, MIN_VOLUME, MIN_LIQUIDITY
from telegram_bot import send_message
from filters import score_coin, rating
from history import should_alert
from modules.pipeline import process_coin
def scan():
    all_pairs=[]
    for term in SEARCH_TERMS:
        try:
            r=requests.get(f"https://api.dexscreener.com/latest/dex/search?q={term}",timeout=10)
            if r.status_code==200:
                all_pairs.extend(r.json().get("pairs",[]))
        except requests.exceptions.RequestException as e:
            print(f"Error searching {term}: {e}")
    print(f"\nFound {len(all_pairs)} pairs before filtering.")
    coins=[]; seen=set()
    for pair in all_pairs:
        try:
            if pair.get("chainId")!="solana": continue
            addr=pair["baseToken"]["address"]
            if addr in seen: continue
            seen.add(addr)
            vol=float(pair["volume"]["h24"]); liq=float(pair["liquidity"]["usd"])
            if vol<MIN_VOLUME or liq<MIN_LIQUIDITY: continue
            pc=pair.get("priceChange",{})
            m5=float(pc.get("m5",0) or 0); h1=float(pc.get("h1",0) or 0); h24=float(pc.get("h24",0) or 0)
            score,notes=score_coin(vol,liq,pair["dexId"],m5,h1,h24)
            coins.append({"address":addr,"name":pair["baseToken"]["name"],"symbol":pair["baseToken"]["symbol"],"price":pair["priceUsd"],"volume":vol,"liquidity":liq,"dex":pair["dexId"],"m5":m5,"h1":h1,"h24":h24,"score":score,"rating":rating(score),"notes":notes})
        except Exception:
            continue
    if not coins:
        print("No matching Solana coins found."); return
    coins.sort(key=lambda c:c["score"],reverse=True)
    for coin in coins:
        alert,reason=should_alert(coin["address"],coin["score"],coin["volume"],coin["liquidity"])
        if not alert:
            print(f"Skipping: {coin['name']}"); continue
        link=f"https://dexscreener.com/solana/{coin['address']}"
        msg=(f"🚀 MEME COIN RADAR\n\n🪙 {coin['name']} ({coin['symbol']})\n\n⭐ Score: {coin['score']}/100\n{coin['rating']}\n\n📢 Trigger:\n{reason}\n\n💰 Price: ${coin['price']}\n📈 Volume: ${coin['volume']:,.0f}\n💧 Liquidity: ${coin['liquidity']:,.0f}\n⚡ 5m: {coin['m5']:.2f}%\n🔥 1h: {coin['h1']:.2f}%\n🚀 24h: {coin['h24']:.2f}%\n🏦 DEX: {coin['dex']}\n\n📋 Signals:\n" + "\n".join(coin["notes"]) + f"\n\n📋 Contract:\n{coin['address']}\n\n🔗 {link}")
        print(msg)
        send_message(msg)
