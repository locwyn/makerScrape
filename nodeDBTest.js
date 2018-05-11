var credentials = require('./credentials');
var mysql = require('mysql');

var con = mysql.createConnection({
  host: credentials.dbHost,
  user: credentials.dbUser,
  password: credentials.dbPassword,
//  database: "makerTweets"
});

con.connect(function(err) {
    console.log(typeof(err));
//  if (err) throw err;
//  con.query("SELECT tweetID FROM tweets ORDER BY id DESC LIMIT 10",
//            function (err, result, fields) {
  //  if (err) throw err;
    console.log("Success!");
//  });
});
