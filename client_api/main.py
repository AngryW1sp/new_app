from pyrogram import Client

api_id = 27397869
api_hash = 'b5c75d8801606caf5570bff7470f1999'

app = Client('my_account', api_id, api_hash)

app.start()
app.send_message('me', 'Привет, это я!')
app.stop()
