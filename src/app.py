# Webserver microframework
from flask import Flask

# Waitress is a production-quality pure-Python WSGI server with acceptable performance.
from waitress import serve

# Importing GraphQLView
from graphql_server.flask import GraphQLView
from models.schema import schema

app = Flask(__name__)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True,
))


@app.route("/")
def root():
    return "Hello World!"


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8080)
