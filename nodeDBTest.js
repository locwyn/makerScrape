var credentials = require('./credentials');
var mysql = require('mysql');

var con = mysql.createConnection({
  host: credentials.dbHost,
  user: credentials.dbUser,
  password: credentials.dbPassword,
  database: "makerTweets"
});

con.connect(function(err) {
  if (err) throw err;
  con.query("SELECT TOP 10 tweetID FROM tweets ORDER BY id DESC",
            function (err, results, fields) {
    if (err) throw err;
    console.log(result);
  });
});
