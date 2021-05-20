#!/usr/bin/python3
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]


@app.route("/jinja2/")
def jinja2():
    try:
        qparams = {}
        qparams["ip"] = request.args.get("ip", groups[0]["ip"])


        return render_template("jinja2.conf.j2", **qparms)

    except Exception as err:
        return "Uh-oh! " + err

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
