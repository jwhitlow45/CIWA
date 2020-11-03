const sql = require('mssql');
const config = require('./config');
const cimis = require('./getCIMIS');

// station targets
const target = ['2',
	'7',
	'39',
	'80',
	'105',
	'124',
	'142',
	'190',
	'205',
	'5',
	'54',
	'125',
	'146',
	'15',
	'188',
	'56',
	'92',
	'148',
	'70',
	'71',
	'194',
	'206',
	'86',
	'169',
	'182']; 

// insert CIMIS data into rawDataTable 
// provide startDate and endDate
async function insertRawDataOnly(startDate, endDate) {

	// rawDataTable all 25 tables we are using
	const hourlyRawTable = ['hourlyRaw2',
		'hourlyRaw7',
		'hourlyRaw39',
		'hourlyRaw80',
		'hourlyRaw105',
		'hourlyRaw124',
		'hourlyRaw142',
		'hourlyRaw190',
		'hourlyRaw205',
		'hourlyRaw5',
		'hourlyRaw54',
		'hourlyRaw125',
		'hourlyRaw146',
		'hourlyRaw15',
		'hourlyRaw188',
		'hourlyRaw56',
		'hourlyRaw92',
		'hourlyRaw148',
		'hourlyRaw70',
		'hourlyRaw71',
		'hourlyRaw194',
		'hourlyRaw206',
		'hourlyRaw86',
		'hourlyRaw169',
		'hourlyRaw182'];



	// establish connection to SQL database with config.json file
	let pool = await sql.connect(config.sqlDatabase);

	try {

		for (let i = 0; i < hourlyRawTable.length; i++) {

			// get CIMIS records for target and sister stations
			const records = await cimis.getCimisMeasurements(target[i], startDate, endDate);

			for (let j = 0; j < records.length; j++) {

				let d = null
				//console.log(records[j].Hour);

				if(records[j].Hour == '2400'){
					d = records[j].Date + "0000" ;
				}

				else {
					d = records[j].Date + records[j].Hour ;	
				}


				let dateHour = d[0] + d[1] + d[2] + d[3] + d[4] + d[5] + d[6] + d[7] + d[8] + d[9] + " " + d[10] + d[11] + ":00:00"
				//console.log(dateHour);

				try {

					// insertRequest1 is for rawDataTable, sending a SQL Script to insert data into SQL Database Tables
					let insertRequest1 = "INSERT INTO " + hourlyRawTable[i] + 
						"(Date," +
						" HlyAirTmp, HlyAirTmpQc," +
						" HlyDewPnt, HlyDewPntQc," + 
						" HlyPrecip, HlyPrecipQc," +
						" HlyRelHum, HlyRelHumQc," + 
						" HlySoilTmp, HlySoilTmpQc," +
						" HlyWindDir, HlyWindDirQc," +
						" HlyWindSpd, HlyWindSpdQc," +
						" HlySolRad, HlySolRadQc," +
						" HlyEto, HlyEtoQc," +
						" HlyAsceEto, HlyAsceEtoQc)" +

						" VALUES " + 
						"(@Date," +
						" @HlyAirTmp, @HlyAirTmpQc," +
						" @HlyDewPnt, @HlyDewPntQc," + 
						" @HlyPrecip, @HlyPrecipQc," +
						" @HlyRelHum, @HlyRelHumQc," + 
						" @HlySoilTmp, @HlySoilTmpQc," +
						" @HlyWindDir, @HlyWindDirQc," +
						" @HlyWindSpd, @HlyWindSpdQc," +
						" @HlySolRad, @HlySolRadQc," +
						" @HlyEto, @HlyEtoQc," +
						" @HlyAsceEto, @HlyAsceEtoQc)";

					// send rawDataTable insertRequest1 to SQL
					let req = await pool.request()

						// tell the request what data types are
						.input("Date", sql.VarChar(), dateHour)
						.input("HlyAirTmp", sql.Float, parseFloat(records[j].HlyAirTmp.Value))
						.input("HlyAirTmpQC", sql.VarChar(), records[j].HlyAirTmp.Qc )
						.input("HlyDewPnt", sql.Float, parseFloat(records[j].HlyDewPnt.Value) )
						.input("HlyDewPntQC", sql.VarChar(), records[j].HlyDewPnt.Qc )
						.input("HlyPrecip", sql.Float, parseFloat(records[j].HlyPrecip.Value) )
						.input("HlyPrecipQc", sql.VarChar(), records[j].HlyPrecip.Qc )
						.input("HlyRelHum", sql.Float, parseFloat(records[j].HlyRelHum.Value) )
						.input("HlyRelHumQc", sql.VarChar(), records[j].HlyRelHum.Qc )
						.input("HlySoilTmp", sql.Float, parseFloat(records[j].HlySoilTmp.Value) )
						.input("HlySoilTmpQc", sql.VarChar(), records[j].HlySoilTmp.Qc )
						.input("HlyWindDir", sql.Float, parseFloat(records[j].HlyWindDir.Value) )
						.input("HlyWindDirQc", sql.VarChar(), records[j].HlyWindDir.Qc )
						.input("HlyWindSpd", sql.Float, parseFloat(records[j].HlyWindSpd.Value) )
						.input("HlyWindSpdQc", sql.VarChar(), records[j].HlyWindSpd.Qc )
						.input("HlySolRad", sql.Float, parseFloat(records[j].HlySolRad.Value) )
						.input("HlySolRadQc", sql.VarChar(), records[j].HlySolRad.Qc )
						.input("HlyEto", sql.Float, parseFloat(records[j].HlyEto.Value) )
						.input("HlyEtoQc", sql.VarChar(), records[j].HlyEto.Qc )
						.input("HlyAsceEto", sql.Float, parseFloat(records[j].HlyAsceEto.Value) )
						.input("HlyAsceEtoQc", sql.VarChar(), records[j].HlyAsceEto.Qc )

						.query(insertRequest1);

						console.log("Inserted records" + j + " into " + hourlyRawTable[i] + " and it is on " + dateHour );

					}

					catch (err) {
						console.log(err);


						// if we get Unique Id error from SQL skip to next date/ table.
						// avoids the code from stopping if there is a Unique id error
						continue;
					}



				}
			
			}
		}

	catch (err) {
		console.log(err);
	}

	finally {
		//pool.close();
		sql.close();
		console.log("Finally Finished runAll Function");
	}
}

exports.insertRawDataOnly = insertRawDataOnly



