from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("D:/chatbot_project3/chatbot-deployment-main/templates/base.html")

@app.route("/send", methods=["POST"])
def send():
  user_input = request.form["user_input"]
  response = chatbot_response(user_input)
  return render_template("D:/chatbot_project3/chatbot-deployment-main/templates/base.html", response=response)

if __name__ == "__main__":
  app.run()