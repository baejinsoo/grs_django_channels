import websocket
import json


ws = websocket.WebSocket()
ws.connect("ws://52.73.45.94:8000/ws/chat/1234/")

pp=json.dumps({'message':"hello"})
ws.send(pp)