
var credentials = require('./credentials');
var mysql = require('mysql');

var con = mysql.createConnection({
  host: credentials.dbHost,
  user: credentials.dbUser,
  password: credentials.dbPassword,
  database: "makerTweets"
});

con.connect(function(err) {
  if (err) console.log(typeof(err));
  console.log("Success!");
}); 

//console.log("Success!");

//con.end(function(err) {
//  if (err) console.log("End broke!");
//  console.log("Ended!");
//});

//console.log("Ended!");
