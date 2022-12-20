from flask import Flask
import logging
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
  </script>
  <button type="button">Click Me!</button></html>
"""
  return prefix_google


# tp2: log part
@app.route('/loggs')
def loggs():
    app.logger.warning('testing warning log')
    script="""
    <script>console.log("loggy loggy where am I ?")</script>
    """
    return "Check your console "+ script

