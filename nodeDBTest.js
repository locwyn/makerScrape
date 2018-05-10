var credentials = require('./credentials');
var mysql = require('mysql');

var con = mysql.createConnection({
  host: credentials.dbHost(),
  user: credentials.dbUser(),
  password: credentials.dbPassword()
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
});
