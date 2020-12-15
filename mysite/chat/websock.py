import websocket
import json


ws = websocket.WebSocket()
ws.connect("ws://localhost:8000/ws/chat/lobby/")
# pp=json.dumps({'message':"godfokp"})
# ws.send(pp)
pp=json.dumps({'message':"1"})
ws.send(pp)