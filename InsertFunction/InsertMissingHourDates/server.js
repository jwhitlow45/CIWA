var http = require('http');
var fs = require('fs');
const auto1 = require('./insertHourlyDates');
const sql = require('mssql');



function expServer() {

	auto1.insertHourlyMissingDates();

}

exports.expServer = expServer


	

