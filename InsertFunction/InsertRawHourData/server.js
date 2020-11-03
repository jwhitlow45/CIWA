var http = require('http');
var fs = require('fs');
const auto1 = require('./insertRawOnly');
const sql = require('mssql');




function expServer() {

var date = new Date();
date.setDate(date.getDate() - 1);
var d = date.toISOString();

var yesDate = d[0] + d[1] + d[2] + d[3] + d[4]+ d[5] + d[6] + d[7] + d[8] + d[9]; 

console.log(yesDate);
console.log(date); 


// calling the runAll file to run the insertAll/ insertOne function whichever you choose

	auto1.insertRawDataOnly(yesDate,yesDate);
		console.log("i should be running");


}

exports.expServer = expServer




