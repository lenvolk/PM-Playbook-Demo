/**
 * INTENTIONALLY VULNERABLE CODE FOR CODEQL TESTING
 * DO NOT USE IN PRODUCTION
 * 
 * This file contains security vulnerabilities to demonstrate
 * GitHub CodeQL code scanning capabilities.
 */

const express = require('express');
const { exec } = require('child_process');
const fs = require('fs');
const mysql = require('mysql');

const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// ============================================================
// VULNERABILITY 1: SQL Injection
// CodeQL should detect: js/sql-injection
// ============================================================
app.get('/user', (req, res) => {
    const userId = req.query.id;
    const connection = mysql.createConnection({
        host: 'localhost',
        user: 'root',
        password: 'password',
        database: 'users'
    });
    
    // VULNERABLE: User input directly concatenated into SQL query
    const query = "SELECT * FROM users WHERE id = '" + userId + "'";
    connection.query(query, (error, results) => {
        if (error) throw error;
        res.json(results);
    });
});

// ============================================================
// VULNERABILITY 2: Command Injection
// CodeQL should detect: js/command-line-injection
// ============================================================
app.get('/ping', (req, res) => {
    const host = req.query.host;
    
    // VULNERABLE: User input passed directly to shell command
    exec('ping -c 4 ' + host, (error, stdout, stderr) => {
        res.send(stdout || stderr);
    });
});

// ============================================================
// VULNERABILITY 3: Cross-Site Scripting (XSS)
// CodeQL should detect: js/xss, js/reflected-xss
// ============================================================
app.get('/search', (req, res) => {
    const searchTerm = req.query.q;
    
    // VULNERABLE: User input reflected in response without sanitization
    res.send(`<html><body>
        <h1>Search Results</h1>
        <p>You searched for: ${searchTerm}</p>
    </body></html>`);
});

// ============================================================
// VULNERABILITY 4: Path Traversal
// CodeQL should detect: js/path-injection
// ============================================================
app.get('/file', (req, res) => {
    const filename = req.query.name;
    
    // VULNERABLE: User input used directly in file path
    const filepath = './uploads/' + filename;
    fs.readFile(filepath, (err, data) => {
        if (err) {
            res.status(404).send('File not found');
        } else {
            res.send(data);
        }
    });
});

// ============================================================
// VULNERABILITY 5: Hardcoded Credentials
// CodeQL should detect: js/hardcoded-credentials
// ============================================================
const dbConfig = {
    host: 'database.example.com',
    username: 'admin',
    password: 'SuperSecret123!',  // VULNERABLE: Hardcoded password
    database: 'production'
};

// ============================================================
// VULNERABILITY 6: Insecure Randomness
// CodeQL should detect: js/insecure-randomness
// ============================================================
app.get('/token', (req, res) => {
    // VULNERABLE: Math.random() is not cryptographically secure
    const token = Math.random().toString(36).substring(2);
    res.json({ token: token });
});

// ============================================================
// VULNERABILITY 7: Missing Rate Limiting (Logic Issue)
// ============================================================
app.post('/login', (req, res) => {
    const { username, password } = req.body;
    // No rate limiting - allows brute force attacks
    authenticateUser(username, password)
        .then(user => res.json({ success: true, user }))
        .catch(err => res.status(401).json({ error: 'Invalid credentials' }));
});

// ============================================================
// VULNERABILITY 8: Prototype Pollution
// CodeQL should detect: js/prototype-polluting-assignment
// ============================================================
app.post('/config', (req, res) => {
    const userConfig = req.body;
    const config = {};
    
    // VULNERABLE: Merging user-controlled object without validation
    for (const key in userConfig) {
        config[key] = userConfig[key];
    }
    
    res.json({ message: 'Config updated', config });
});

// ============================================================
// VULNERABILITY 9: Regex DoS (ReDoS)
// CodeQL should detect: js/redos
// ============================================================
app.get('/validate-email', (req, res) => {
    const email = req.query.email;
    
    // VULNERABLE: Exponential backtracking regex
    const emailRegex = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    
    if (emailRegex.test(email)) {
        res.json({ valid: true });
    } else {
        res.json({ valid: false });
    }
});

// ============================================================
// VULNERABILITY 10: Server-Side Request Forgery (SSRF)
// CodeQL should detect: js/request-forgery
// ============================================================
const axios = require('axios');

app.get('/fetch', async (req, res) => {
    const url = req.query.url;
    
    // VULNERABLE: Fetching user-controlled URL without validation
    try {
        const response = await axios.get(url);
        res.send(response.data);
    } catch (error) {
        res.status(500).send('Error fetching URL');
    }
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

function authenticateUser(username, password) {
    // Dummy function
    return Promise.reject(new Error('Not implemented'));
}

module.exports = app;
