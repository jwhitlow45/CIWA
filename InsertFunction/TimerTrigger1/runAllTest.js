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

// insert CIMIS data into dailyRawTable and mainDataTable
// provide startDate and endDate
async function insertRawAndMainData(startDate, endDate) {

	// dailyRawTable
	const dailyRawTable = ['dailyRaw2',
		'dailyRaw7',
		'dailyRaw39',
		'dailyRaw80',
		'dailyRaw105',
		'dailyRaw124',
		'dailyRaw142',
		'dailyRaw190',
		'dailyRaw205',
		'dailyRaw5',
		'dailyRaw54',
		'dailyRaw125',
		'dailyRaw146',
		'dailyRaw15',
		'dailyRaw188',
		'dailyRaw56',
		'dailyRaw92',
		'dailyRaw148',
		'dailyRaw70',
		'dailyRaw71',
		'dailyRaw194',
		'dailyRaw206',
		'dailyRaw86', 
		'dailyRaw169',
		'dailyRaw182'];



	// establish connection to SQL database with config.json file
	let pool = await sql.connect(config.sqlDatabase);

	try {
		for (let i = 0; i < dailyRawTable.length; i++) {
			// get CIMIS records for target and sister stations
			const records = await cimis.getCimisMeasurements(target[i], startDate, endDate);

			for (let j = 0; j < records.length; j++) {

				let DayAirTmpMax = null;
				let DayAirTmpMin = null;
				let DayRelHumMax = null;
				let DayRelHumMin = null;
				let DayWindSpdAvg = null;
				let DayDewPnt = null;
				let DayEto = null;
				let DayAsceEto = null;
				let DayPrecip = null;

				try {
					// insertRequest1 is for dailyRawTable
					let insertRequest1 = "INSERT INTO " + dailyRawTable[i] + 
						"(Date," +
						" DayAirTmpMax, DayAirTmpMaxQc," +
						" DayAirTmpMin, DayAirTmpMinQc," + 
						" DayRelHumMax, DayRelHumMaxQc," +
						" DayRelHumMin, DayRelHumMinQc," + 
						" DayWindSpdAvg, DayWindSpdAvgQc," +
						" DayDewPnt, DayDewPntQc," +
						" DayEto, DayEtoQc," +
						" DayAsceEto, DayAsceEtoQc," + 
						" DayPrecip, DayPrecipQc)" +

						" VALUES " + 
						"(@Date," +
						" @DayAirTmpMax, @DayAirTmpMaxQc," +
						" @DayAirTmpMin, @DayAirTmpMinQc," + 
						" @DayRelHumMax, @DayRelHumMaxQc," +
						" @DayRelHumMin, @DayRelHumMinQc," + 
						" @DayWindSpdAvg, @DayWindSpdAvgQc," +
						" @DayDewPnt, @DayDewPntQc," +
						" @DayEto, @DayEtoQc," +
						" @DayAsceEto, @DayAsceEtoQc," + 
						" @DayPrecip, @DayPrecipQc)";

					// send dailyRawTable insertRequest1 to SQL
					let req = await pool.request()
						// tell the request what data types are
						.input("Date", sql.Date, records[j].Date)
						.input("DayAirTmpMax", sql.Float, parseFloat(records[j].DayAirTmpMax.Value))
						.input("DayAirTmpMaxQC", sql.VarChar(), records[j].DayAirTmpMax.Qc )
						.input("DayAirTmpMin", sql.Float, parseFloat(records[j].DayAirTmpMin.Value) )
						.input("DayAirTmpMinQC", sql.VarChar(), records[j].DayAirTmpMin.Qc )
						.input("DayRelHumMax", sql.Float, parseFloat(records[j].DayRelHumMax.Value) )
						.input("DayRelHumMaxQc", sql.VarChar(), records[j].DayRelHumMax.Qc )
						.input("DayRelHumMin", sql.Float, parseFloat(records[j].DayRelHumMin.Value) )
						.input("DayRelHumMinQc", sql.VarChar(), records[j].DayRelHumMin.Qc )
						.input("DayWindSpdAvg", sql.Float, parseFloat(records[j].DayWindSpdAvg.Value) )
						.input("DayWindSpdAvgQc", sql.VarChar(), records[j].DayWindSpdAvg.Qc )
						.input("DayDewPnt", sql.Float, parseFloat(records[j].DayDewPnt.Value) )
						.input("DayDewPntQc", sql.VarChar(), records[j].DayDewPnt.Qc )
						.input("DayEto", sql.Float, parseFloat(records[j].DayEto.Value) )
						.input("DayEtoQc", sql.VarChar(), records[j].DayEto.Qc )
						.input("DayAsceEto", sql.Float, parseFloat(records[j].DayAsceEto.Value) )
						.input("DayAsceEtoQc", sql.VarChar(), records[j].DayAsceEto.Qc )
						.input("DayPrecip", sql.Float, parseFloat(records[j].DayPrecip.Value) )
						.input("DayPrecipQc", sql.VarChar(), records[j].DayPrecip.Qc )

						.query(insertRequest1);

					}

					catch (err) {
						console.log("uniqueIDraw");

						console.log(err);


						// if we get Unique Id error from SQL skip to next table
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

exports.insertRawAndMainData = insertRawAndMainData



