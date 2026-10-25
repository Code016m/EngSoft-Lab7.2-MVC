"""Aplicação web da livraria."""

from flask import Flask, jsonify, render_template, request

from livraria import (
	consultar_horario,
	consultar_livro,
	consultar_localizacao,
	consultar_disponibilidade_loja,
	listar_livros,
	pesquisar_livros,
	recomendar_livros,
)

app = Flask(__name__)


@app.get("/")
def pagina_inicial():
	return render_template("index.html")


@app.get("/api/livros")
def api_livros():
	busca = request.args.get("q", "")
	livros = pesquisar_livros(busca) if busca.strip() else listar_livros()
	return jsonify({"livros": livros})


@app.get("/api/livros/<path:titulo>")
def api_livro(titulo):
	livro = consultar_livro(titulo)
	if livro is None:
		return jsonify({"erro": "Livro não encontrado."}), 404
	return jsonify(livro)


@app.get("/api/livros/<path:titulo>/disponibilidade")
def api_disponibilidade(titulo):
	livro = consultar_livro(titulo)
	if livro is None:
		return jsonify({"erro": "Livro não encontrado."}), 404

	loja = request.args.get("loja")
	if loja:
		disponivel = consultar_disponibilidade_loja(titulo, loja)
	else:
		disponivel = livro["disponivel"]
	return jsonify({"disponivel": disponivel, "loja": loja})


@app.get("/api/horario")
def api_horario():
	return jsonify({"horario": consultar_horario()})


@app.get("/api/localizacao")
def api_localizacao():
	return jsonify({"localizacao": consultar_localizacao()})


@app.get("/api/recomendacoes")
def api_recomendacoes():
	return jsonify({"livros": recomendar_livros()})


if __name__ == "__main__":
	app.run(debug=True)
