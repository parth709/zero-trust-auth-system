from flask import Flask, jsonify, request
from datetime import timedelta
from flask import render_template

from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
    get_jwt
)

app = Flask(__name__)

# 🔐 JWT CONFIG
app.config["JWT_SECRET_KEY"] = "zerotrust-secret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=1)

jwt = JWTManager(app)

# 👥 Fake users with roles
users = {
    "admin": {
        "password": "admin123",
        "role": "admin"
    },
    "user": {
        "password": "user123",
        "role": "user"
    }
}

@app.route("/")
def home():
    return jsonify(message="Zero Trust System Running")

# 🔑 LOGIN
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users and users[username]["password"] == password:
        token = create_access_token(
            identity=username,
            additional_claims={"role": users[username]["role"]}
        )
        return jsonify(access_token=token)

    return jsonify(message="Invalid credentials"), 401

# 🔒 PROFILE (Any logged-in user)
@app.route("/profile")
@jwt_required()
def profile():
    user = get_jwt_identity()
    return jsonify(message=f"Hello {user}, this is protected data")

# 🛑 ADMIN ONLY
@app.route("/admin")
@jwt_required()
def admin_panel():
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify(message="Admins only"), 403

    return jsonify(message="Welcome Admin, Zero Trust access granted")

# 🚨 JWT ERROR HANDLERS
@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify(
        error="Authorization token missing",
        message="Access denied. Token required."
    ), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify(
        error="Invalid token",
        message="Token is malformed or tampered"
    ), 422

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify(
        status="error",
        code="TOKEN_EXPIRED",
        title="Session Expired",
        message="Your session has expired for security reasons. Please log in again."
    ), 401


@app.route("/login-ui")
def login_ui():
    return render_template("login.html")


# 🚀 START SERVER (LAST LINE ONLY)
if __name__ == "__main__":
    app.run(debug=True)
