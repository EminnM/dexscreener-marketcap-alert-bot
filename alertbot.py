import asyncio
import websockets
import json
import os
import time

async def subscribe_to_websocket(token,value,file):
    uri = f"wss://io.dexscreener.com/dex/screener/pair/solana/{token}"
    #fill the headers part according to your headers. Use the header of the wss.
    headers = {
        "Accept-Encoding": ,
        "Accept-Language": ,
        "Cache-Control": ,
        "Connection": ,
        "Host": ,
        "Origin": ,
        "Pragma": ,
        "Sec-Websocket-Extensions": ,
        "Sec-Websocket-Key": ,
        "Sec-Websocket-Version": ,
        "Upgrade": ,
        "User-Agent": 
    }
    async with websockets.connect(uri, extra_headers=headers) as websocket:
        print("Connected to WebSocket")
        try:
            while True:
                message = await websocket.recv()
                if message == "ping":
                    #print(message)
                    await websocket.ping()
                else:
                    try:
                        parsed_message = json.loads(message)
                        marketCap = parsed_message["pair"]["marketCap"]
                        print("Market Cap:", marketCap)
                        if int(marketCap) > value:
                            print(f"Market Cap exceeds {value}. Alerting...")
                            os.startfile(file)
                            quit()
                    except:
                        print(message)


        except websockets.exceptions.ConnectionClosed:
            print("WebSocket connection closed")

asyncio.run(subscribe_to_websocket(token,marketcap,file))
