const fetch = require('node-fetch'); // allows use to call the CIMIS API using node-fetch Library


async function getCimisMeasurements(target, startDate, endDate) {

	//cimis api url Configuration
	const appKey = 'c2336dfa-e93a-4024-bdfe-641c9c80e78c';
	const dataItems = 'day-air-tmp-max,day-air-tmp-min,day-rel-hum-max,day-rel-hum-min,day-wind-spd-avg,day-dew-pnt,day-eto,day-asce-eto,day-precip';
	const cimisURL = 'http://et.water.ca.gov/api/data?appKey=' + appKey + '&targets=' + target + '&startDate=' + startDate + '&endDate=' + endDate + '&dataItems=' + dataItems + '&unitOfMeasure=M';
	

	// "try" becomes aware of errors. If it sees an error it sends it to "catch"
	try{

		// fetch cimis api data using url
		const response = await fetch(cimisURL);

		 // convert cimis api data into a json object
		const cimisJson = await response.json();

		const records = await cimisJson.Data.Providers[0].Records;

		console.log(records);

		return await records;
	}

	catch(err){

		console.log(err);
		console.log(cimisURL);

		return"ERROR";
	}


}

exports.getCimisMeasurements = getCimisMeasurements;

