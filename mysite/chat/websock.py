import websocket
import json


ws = websocket.WebSocket()
ws.connect("ws://127.0.0.1:8000/ws/chat/12368/")

pp=json.dumps({'message':"2"})
ws.send(pp)