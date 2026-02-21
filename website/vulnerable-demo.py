"""
INTENTIONALLY VULNERABLE CODE FOR CODEQL TESTING
DO NOT USE IN PRODUCTION

This file contains security vulnerabilities to demonstrate
GitHub CodeQL code scanning capabilities.
"""

import os
import pickle
import subprocess
import sqlite3
from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

# ============================================================
# VULNERABILITY 1: SQL Injection
# CodeQL should detect: py/sql-injection
# ============================================================
@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABLE: User input directly concatenated into SQL query
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    cursor.execute(query)
    
    return str(cursor.fetchall())


# ============================================================
# VULNERABILITY 2: Command Injection
# CodeQL should detect: py/command-line-injection
# ============================================================
@app.route('/ping')
def ping_host():
    host = request.args.get('host')
    
    # VULNERABLE: User input passed directly to shell command
    result = os.popen('ping -c 4 ' + host).read()
    return result


# ============================================================
# VULNERABILITY 3: Command Injection (subprocess)
# CodeQL should detect: py/command-line-injection
# ============================================================
@app.route('/execute')
def execute_command():
    cmd = request.args.get('cmd')
    
    # VULNERABLE: User input in shell command
    result = subprocess.run(cmd, shell=True, capture_output=True)
    return result.stdout.decode()


# ============================================================
# VULNERABILITY 4: Server-Side Template Injection (SSTI)
# CodeQL should detect: py/template-injection
# ============================================================
@app.route('/greet')
def greet():
    name = request.args.get('name', 'World')
    
    # VULNERABLE: User input in template without sanitization
    template = f"<h1>Hello, {name}!</h1>"
    return render_template_string(template)


# ============================================================
# VULNERABILITY 5: Cross-Site Scripting (XSS)
# CodeQL should detect: py/reflective-xss
# ============================================================
@app.route('/search')
def search():
    query = request.args.get('q', '')
    
    # VULNERABLE: User input reflected in response
    return f"""
    <html>
        <body>
            <h1>Search Results</h1>
            <p>You searched for: {query}</p>
        </body>
    </html>
    """


# ============================================================
# VULNERABILITY 6: Path Traversal
# CodeQL should detect: py/path-injection
# ============================================================
@app.route('/file')
def read_file():
    filename = request.args.get('name')
    
    # VULNERABLE: User input used directly in file path
    filepath = os.path.join('./uploads/', filename)
    with open(filepath, 'r') as f:
        return f.read()


# ============================================================
# VULNERABILITY 7: Insecure Deserialization
# CodeQL should detect: py/unsafe-deserialization
# ============================================================
@app.route('/load', methods=['POST'])
def load_data():
    data = request.data
    
    # VULNERABLE: Deserializing untrusted data with pickle
    obj = pickle.loads(data)
    return str(obj)


# ============================================================
# VULNERABILITY 8: Hardcoded Credentials
# CodeQL should detect: py/hardcoded-credentials
# ============================================================
DATABASE_CONFIG = {
    'host': 'database.example.com',
    'username': 'admin',
    'password': 'SuperSecret123!',  # VULNERABLE: Hardcoded password
    'database': 'production'
}

API_KEY = "sk-1234567890abcdef"  # VULNERABLE: Hardcoded API key


# ============================================================
# VULNERABILITY 9: Open Redirect
# CodeQL should detect: py/url-redirection
# ============================================================
@app.route('/redirect')
def unsafe_redirect():
    url = request.args.get('url')
    
    # VULNERABLE: Redirecting to user-controlled URL
    return redirect(url)


# ============================================================
# VULNERABILITY 10: Weak Cryptography
# CodeQL should detect: py/weak-cryptographic-algorithm
# ============================================================
import hashlib

@app.route('/hash')
def hash_password():
    password = request.args.get('password')
    
    # VULNERABLE: Using MD5 for password hashing
    hashed = hashlib.md5(password.encode()).hexdigest()
    return {'hash': hashed}


# ============================================================
# VULNERABILITY 11: XML External Entity (XXE)
# CodeQL should detect: py/xxe
# ============================================================
from xml.etree.ElementTree import parse

@app.route('/parse-xml', methods=['POST'])
def parse_xml():
    # VULNERABLE: Parsing XML without disabling external entities
    tree = parse(request.stream)
    return str(tree.getroot().text)


# ============================================================
# VULNERABILITY 12: LDAP Injection
# CodeQL should detect: py/ldap-injection
# ============================================================
import ldap

@app.route('/ldap-search')
def ldap_search():
    username = request.args.get('username')
    
    # VULNERABLE: User input in LDAP filter
    conn = ldap.initialize('ldap://localhost')
    filter_str = f"(uid={username})"
    results = conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, filter_str)
    return str(results)


# ============================================================
# Start Flask server
# ============================================================
if __name__ == '__main__':
    # VULNERABLE: Debug mode enabled in production
    app.run(debug=True, host='0.0.0.0')
