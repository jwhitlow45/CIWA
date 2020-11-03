const fetch = require('node-fetch'); // allows use to call the CIMIS API using node-fetch Library


async function getCimisMeasurements(target, startDate, endDate) {

	//cimis api url Configuration
	const appKey = 'f26aa7d0-7103-4f8a-9c3f-e24723ebca0a';
	const dataItems = 'hly-air-tmp,hly-dew-pnt,hly-precip,hly-rel-hum,hly-soil-tmp,hly-wind-dir,hly-wind-spd,hly-sol-rad,hly-eto,hly-asce-eto';
	const cimisURL = 'http://et.water.ca.gov/api/data?appKey=' + appKey + '&targets=' + target + '&startDate=' + startDate + '&endDate=' + endDate + '&dataItems=' + dataItems + '&unitOfMeasure=M';
	

	// "try" becomes aware of errors. If it sees an error it sends it to "catch"
	try{

		// fetch cimis api data using url
		const response = await fetch(cimisURL);

		 // convert cimis api data into a json object
		const cimisJson = await response.json();

		const records = await cimisJson.Data.Providers[0].Records;

		//console.log(records);

		return await records;
	}

	catch(err){

		console.log(err);
		console.log(cimisURL);

		return"ERROR";
	}


}

exports.getCimisMeasurements = getCimisMeasurements;  

