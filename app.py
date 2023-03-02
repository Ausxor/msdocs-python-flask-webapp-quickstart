from datetime import datetime
import logging
import sys
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)

# Acquire the logger for a library (azure.mgmt.resource in this example)
logger = logging.getLogger('mylog')

# Set the desired logging level
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)

@app.route('/')
def index():
   return redirect("/home")

@app.route('/home')
def home():
   logger.debug("debug 0")
   logger.info("info 1")
   logger.warning("warning 1")
   logger.error("[ERROR] error 1")
   logger.critical("critical 1")
   logger.info("info 2")
   logger.debug("debug 1")
   logger.debug("debug 2")
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()