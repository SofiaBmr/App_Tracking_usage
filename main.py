from flask import Flask,render_template,make_response,request
import logging
import requests
app=Flask(__name__)
@app.route('/')

# tp1 : adding cookies to our app
def hello_world():

  prefix_google="""
	<!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=UA-250382412-1"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'UA-250382412-1');
    req =requests.get("https://www.google.com/");
    return req.cookies.get_dict()
  </script>
  <input type="button" onclick="window.location.href = './loggs';" value="Click here to see the log page"/>
  </html>
"""
  return prefix_google


# tp2: log part and text box
@app.route('/loggs')
def loggs():
    app.logger.warning('testing warning log')
    script="""
    <script>console.log("loggy loggy where am I ?")</script>

    <form action="/setcookies" method="POST">
      <label for="uname">Username :</label>
      <input type="text" id="uname" name="uname" placeholder="Sofia"required><br><br>
      <label for="pwd">Password :</label>
      <input type="text" id="pwd" name="pwd" placeholder="viveladata"required><br><br>
      <input type="submit" value="Submit">
    </form>

    """
    return "Check your console to see the logs"+ "<br><br>" +script

#set the cookie of the username
@app.route('/setcookies', methods = ['POST', 'GET'])
def setcookie():
  if request.method == 'POST':
    username = request.form['uname']
    password= request.form['pwd']
  script="""
  <input type="button" onclick="window.location.href = './getcook';" value="Click here to see the cookie page"/>
  <input type="button" onclick="window.location.href = './getcook2';" value="Click here to see the analytic page"/>
  """
  return "Welcome " + username + " !" + script

#request https://www.google.com/
@app.route('/cookie_test')
def cookie_test():
  req =requests.get("https://www.google.com/")
  return req.status_code


@app.route('/getcook')
def get_cookies():
  req =requests.get("https://analytics.google.com/analytics/web/#/report-home/a250382412w344211401p280829293")
  return req.cookies.get_dict()

@app.route('/getcook2')
def get_cookies2():
  req =requests.get("https://analytics.google.com/analytics/web/#/report-home/a250382412w344211401p280829293")
  return req.text