var http = require('http');
var fs = require('fs');
const auto = require('./insertMainData');
const sql = require('mssql');


function expServer() {

	auto.insertAllMainData();
	
		
}

exports.expServer = expServer