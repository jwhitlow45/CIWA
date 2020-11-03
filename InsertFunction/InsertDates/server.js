var http = require('http');
var fs = require('fs');
var SERVER_PORT = 8080;
const auto = require('./insertDates');
const sql = require('mssql');


function expServer() {

	auto.insertMissingDates();
	

}

exports.expServer = expServer

