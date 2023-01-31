import asyncio, json
from flask import Flask, render_template, request
from core.utils import Config, Termux
from pyrogram import Client, types
from core.create_app import create
from dialog import Dialog
from threading import Thread

if Config.created:
	app = Client(Config.session_name, api_id=int(Config.api_id), api_hash=Config.api_hash, phone_number=Config.phone)
else:	
	d = Dialog(dialog="dialog")
	phone=d.inputbox('Input number')[1]
	create=create(phone)
	create.send_code()
	while not create.login(d.inputbox('Input password')):pass
	tmp=create.get_api()
	if not tmp['status']:tmp=create.get_api()
	tmp['phone']=phone
	del tmp['status']
	api=json.dumps(tmp)
	with open('settings.json', 'w') as f:
		f.write(f"{api}\n")
	exit()

web = Flask(__name__)

@web.route('/')
def index():
	try:app.download_media([t for t in app.get_chat_photos("me")][0].file_id, file_name="static/img/profile.png")
	except:pass
	return render_template('index.html', user=app.get_me())

@web.route('/chats')
def chats():
	data=''
	for dialog in app.get_dialogs():
  		data+=f'''
			<div class="chat">
				<span id="name">{dialog.chat.title or dialog.chat.first_name}</span>
				<span id="type" onclick="location.href='/chat?id={dialog.chat.id}'">Open</span>
 			</div>
			\n
		'''
	return render_template('chat-list.html', data=data)

@web.route('/chat')
def spam():
	chat=app.get_chat(request.args.get('id'))
	return render_template('spam.html', chat=chat)

@web.route('/spam')
def command():
	print(request.args.get('count'))
	for i in range(int(request.args.get('count'))):
		app.send_message(int(request.args.get('chat_id')), str(request.args.get('msg')))

Thread(target=web.run, kwargs={'port': 8080}, daemon=True).start()
app.run()
