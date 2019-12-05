from flask import flask, render templates
app = flask(__name__)

@app.route("/home")
	def home:
		return render_templates("inicio.html")

@app.route("/nutricao")
	def nutri:
		return render_templates("nutricao.html")

@app.route("/tipoalimentos")
	def alimentos:
		return render_templates("alimentos.html")

app.run(debug=True)
