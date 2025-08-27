/**
 * JavaScript file with security vulnerabilities for testing
 */

// SQL Injection vulnerability
function getUserData(userId) {
  // Never concatenate user input into SQL queries
  const query = `SELECT * FROM users WHERE id = ${userId}`;
  // db.query(query); // Would execute unsafe query
  return query;
}

// Command injection vulnerability
function runCommand(filename) {
  const { exec } = require('child_process');
  // Never pass user input directly to exec
  exec(`cat ${filename}`, (error, stdout, stderr) => {
    console.log(stdout);
  });
}

// Hardcoded credentials
const config = {
  databasePassword: 'admin123',  // Never hardcode passwords
  apiKey: 'sk-1234567890abcdefghijklmnop',  // Never hardcode API keys
  secretToken: 'secret_token_12345',  // Never hardcode tokens
  awsAccessKey: 'AKIAIOSFODNN7EXAMPLE',  // AWS credentials
  awsSecretKey: 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
};

// Eval with user input (code injection)
function evaluateExpression(expr) {
  // eval executes arbitrary JavaScript code
  return eval(expr);
}

// Unsafe regex (ReDoS vulnerability)
function validateEmail(email) {
  // Catastrophic backtracking possible
  const regex = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  return regex.test(email);
}

// XSS vulnerability - direct HTML injection
function displayUserContent(userInput) {
  // Never insert user input directly into HTML
  document.getElementById('content').innerHTML = userInput;
}

// Insecure random number generation
function generateToken() {
  // Math.random() is not cryptographically secure
  return Math.floor(Math.random() * 1000000);
}

// Path traversal vulnerability
function readFile(filename) {
  const fs = require('fs');
  // No validation allows ../../etc/passwd
  const path = `/var/data/${filename}`;
  return fs.readFileSync(path, 'utf8');
}

// Prototype pollution vulnerability
function mergeObjects(target, source) {
  // Vulnerable to prototype pollution
  for (const key in source) {
    if (typeof source[key] === 'object') {
      target[key] = mergeObjects(target[key] || {}, source[key]);
    } else {
      target[key] = source[key];
    }
  }
  return target;
}

// Using deprecated/vulnerable functions
function hashPassword(password) {
  const crypto = require('crypto');
  // MD5 is cryptographically broken
  return crypto.createHash('md5').update(password).digest('hex');
}

// Open redirect vulnerability
function redirectUser(url) {
  // No validation allows redirect to malicious sites
  window.location.href = url;
}

// localStorage with sensitive data
function storeSensitiveData(creditCard, ssn) {
  // Never store sensitive data in localStorage
  localStorage.setItem('creditCard', creditCard);
  localStorage.setItem('ssn', ssn);
}

// CORS misconfiguration
function setupCORS(req, res) {
  // Allows any origin - security risk
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Credentials', 'true');
}

// Timing attack vulnerability
function comparePasswords(input, actual) {
  // Early return creates timing differences
  if (input.length !== actual.length) {
    return false;
  }
  
  for (let i = 0; i < input.length; i++) {
    if (input[i] !== actual[i]) {
      return false;  // Early return leaks information
    }
  }
  return true;
}

// Unsafe deserialization
function deserializeData(data) {
  // Function constructor can execute arbitrary code
  return new Function('return ' + data)();
}

// Information disclosure in error messages
function loginUser(username, password) {
  if (username === 'admin' && password !== 'correct') {
    // Reveals that 'admin' is a valid username
    throw new Error('Invalid password for admin user');
  }
}

// Client-side authentication
function checkAuth() {
  // Never do authentication on client side only
  const isAdmin = document.cookie.includes('admin=true');
  if (isAdmin) {
    showAdminPanel();
  }
}

// Weak session management
function createSession(userId) {
  // Predictable session ID
  const sessionId = userId + '_' + Date.now();
  document.cookie = `session=${sessionId}`;
}

// NoSQL injection
function findUser(username) {
  // Vulnerable to NoSQL injection with MongoDB
  const query = { username: username };
  // db.users.find(query);
  return query;
}

// XXE in XML parsing
function parseXML(xmlString) {
  const parser = new DOMParser();
  // Default parser may be vulnerable to XXE
  const xmlDoc = parser.parseFromString(xmlString, "text/xml");
  return xmlDoc;
}

// Export for testing
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    getUserData,
    evaluateExpression,
    generateToken,
    config
  };
}