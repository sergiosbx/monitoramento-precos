from flask import Flask

from app import main

app = Flask(__name__, static_folder="./client", static_url_path="/")


@app.route("/")
def principal():
    main()
    return app.send_static_file("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=80)
