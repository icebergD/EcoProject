from flask import render_template
from flask import Flask, redirect, url_for, request
import requests as rq
import json
from contracs import NFTGame
from database import save_to_file, read_from_file
app = Flask(__name__)

@app.route('/')
def index():
   # return 'Hello World'
   nft_game = NFTGame()
   balance = nft_game.balance()
   last_nft_id = nft_game.get_my_nfts()[-1]
   uri = nft_game.nft_url(last_nft_id)

   image_url = rq.get(uri)
   context = {
   	'balance': balance,
   	'url': json.loads(image_url.text)['image']
   }
   return render_template('index.html', context = context)


@app.route('/video')
def video():
   # return 'Hello World'
   nft_game = NFTGame()
   balance = nft_game.balance()

   # print('balance',balance)
   context = {'balance': balance}
   return render_template('video.html', context = context)


@app.route('/tasks')
def tasks():
   # return 'Hello World'
   nft_game = NFTGame()
   balance = nft_game.balance()

   context = {
      'balance': balance,
      'tasks': read_from_file('db.txt')
   }
   return render_template('tasks.html', context=context)


@app.route('/game')
def game():
   # return 'Hello World'
   nft_game = NFTGame()
   balance = nft_game.balance()

   # print('balance',balance)
   context = {'balance': balance}
   return render_template('game.html', context = context)

@app.route('/add-task', methods=['POST', 'GET'])
def add_task():
   if request.method == 'POST':
      title = request.form['fname']
      description = request.form['lname']
      price = request.form['mname']
      print(title, description, price)
      save_to_file('db.txt', [title, description, price])
      return redirect(url_for('tasks'))
   else:
      nft_game = NFTGame()
      balance = nft_game.balance()

      # print('balance',balance)
      context = {'balance': balance}
      return render_template('addTask.html', context=context)


if __name__ == '__main__':
   app.run(debug = True)


#
# from create_db import Database, Task
#
# db = Database('sqlite:///tasks.db')
#
# # create a session to interact with the database
# Session = sessionmaker(bind=db.engine)
# session = Session()
#
# # create a new task and add it to the database
# new_task = Task(name='Task 1', description='This is task 1', price=10.50)
# session.add(new_task)
# session.commit()
#
# # query the tasks table and print the results
# tasks = session.query(Task).all()
# for task in tasks:
#     print(task.id, task.name, task.description, task.price)