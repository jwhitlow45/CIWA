var http = require('http');
var fs = require('fs');
const auto = require('./insertMainData');
const sql = require('mssql');


function expServer() {

	// calling the runAll file to run the insertAll/ insertOne function whichever you choose

	auto.insertMainData();
	

}

exports.expServer = expServer 

		

