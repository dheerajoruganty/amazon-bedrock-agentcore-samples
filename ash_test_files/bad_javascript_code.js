// JavaScript file with various linting issues

// Missing semicolons
var x = 5
var y = 10

// Using var instead of let/const
var oldStyle = "should use const"

// Inconsistent quotes
const mixed = "double" + 'single';

// Missing JSDoc comments
function undocumented(a, b) {
  return a + b
}

// Trailing spaces and inconsistent indentation
function badFormatting()   {  
    var result = 0;  
  for(var i=0;i<10;i++)   
      {
    result+=i;  
       }
        return result  
}

// Using == instead of ===
function loosEquality(val) {
  if (val == null) {
    return true
  }
  if (val != 0) {
    return false;
  }
}

// Unused variables
function unusedVars() {
  const unused1 = 'not used';
  let unused2 = 42;
  var result = 100;
  return result;
}

// Missing error handling
function riskyOperation() {
  const data = JSON.parse(userInput); // userInput not defined
  return data.value;
}

// Global variable pollution
globalVar = 'should not use globals';

// Callback hell / deeply nested
function callbackHell(callback) {
  getData(function(a) {
    getMoreData(a, function(b) {
      getMoreData(b, function(c) {
        getMoreData(c, function(d) {
          callback(d);
        });
      });
    });
  });
}

// Arrow function without parentheses for single param (style issue)
const arrow = x => x * 2

// Missing const/let/var declaration
implicitGlobal = 100;

// Redeclaring variables
let duplicate = 1;
let duplicate = 2;

// Dead code
function deadCode() {
  return 5;
  console.log('This will never run');
}

// Empty block
if (true) {
}

// Debugger statement
function debugging() {
  debugger;
  return 'remove debugger';
}

// Alert statement
function showAlert() {
  alert('Remove alerts from production code');
}

// Console.log in production code
function logData(data) {
  console.log('Debug:', data);
  return data;
}

// Eval usage (security issue)
function dangerous(code) {
  return eval(code);
}

// With statement (deprecated)
function useWith(obj) {
  with (obj) {
    console.log(prop);
  }
}

// No return in function that should return
function shouldReturn(x) {
  if (x > 0) {
    x * 2;
  }
}

// Modifying parameters
function modifyParam(obj) {
  obj.modified = true;
  return obj;
}

// Long line
const veryLongLine = "This is a very very very very very very very very very very very very very very very very very very long line that should be broken up";

// Multiple statements on one line
function multiple() { const a = 1; const b = 2; return a + b; }

// Missing radix in parseInt
const parsed = parseInt("10");

// new Array() instead of literal
const arr = new Array(1, 2, 3);

// new Object() instead of literal
const obj = new Object();