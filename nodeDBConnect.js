
var credentials = require('./credentials');
var mysql = require('mysql');

var con = mysql.createConnection({
  host: credentials.dbHost,
  user: credentials.dbUser,
  password: credentials.dbPassword,
  database: "makerTweets"
});

//con.connect(function(err) {
//  if (err) throw err;
//  console.log("Connected!");
//});

con.connect(function(err) {
  if (err) throw err;
  con.query("SELECT * FROM hashtags", function (err, result, fields) {
    if (err) throw err;
    console.log(result);
  });
});

//con.end(function(err) {
//  if (err) throw err;
//  console.log("Ended!");
//});




