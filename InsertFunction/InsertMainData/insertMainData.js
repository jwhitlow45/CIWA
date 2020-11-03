const sql = require('mssql');
const config = require('./config');




async function insertAlldailyMain() {

var date1 = new Date();
date1.setDate(date1.getDate()-1);
var a = date1.toISOString();
var startDate = a[0] + a[1] + a[2] + a[3] + a[4]+ a[5] + a[6] + a[7] + a[8] + a[9];
console.log(startDate);


var date2 = new Date();
date2.setDate(date2.getDate()-1);
var b = date2.toISOString();
var endDate = b[0] + b[1] + b[2] + b[3] + b[4]+ b[5] + b[6] + b[7] + b[8] + b[9];
console.log(endDate);




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


	const conTable = ['dailyHist2',
		'dailyHist7',
		'dailyHist39',
		'dailyHist80',
		'dailyHist105',
		'dailyHist124',
		'dailyHist142',
		'dailyHist190',
		'dailyHist205',
		'dailyHist5',
		'dailyHist54',
		'dailyHist125',
		'dailyHist146',
		'dailyHist15',
		'dailyHist188',
		'dailyHist56',
		'dailyHist92',
		'dailyHist148',
		'dailyHist70',
		'dailyHist71',
		'dailyHist194',
		'dailyHist206',
		'dailyHist86', 
		'dailyHist169',
		'dailyHist182'];



	const dailyMainTable = ['dailyMain2',
		'dailyMain7',
		'dailyMain39',
		'dailyMain80',
		'dailyMain105',
		'dailyMain124',
		'dailyMain142',
		'dailyMain190',
		'dailyMain205',
		'dailyMain5',
		'dailyMain54', 
		'dailyMain125', 
		'dailyMain146',
		'dailyMain15',
		'dailyMain188',
		'dailyMain56',
		'dailyMain92',
		'dailyMain148',
		'dailyMain70',
		'dailyMain71',
		'dailyMain194',
		'dailyMain206',
		'dailyMain86', 
		'dailyMain169',
		'dailyMain182'];


	const sister1Data = ['dailyRaw15',
		'dailyRaw124',
		'dailyRaw80',
		'dailyRaw39',
		'dailyRaw7',
		'dailyRaw7',
		'dailyRaw39',
		'dailyRaw2',
		'dailyRaw2',
		'dailyRaw146',
		'dailyRaw146', 
		'dailyRaw5', 
		'dailyRaw5',
		'dailyRaw2',
		'dailyRaw80',
		'dailyRaw124',
		'dailyRaw56',
		'dailyRaw188',
		'dailyRaw71',
		'dailyRaw70',
		'dailyRaw206',
		'dailyRaw194',
		'dailyRaw142', 
		'dailyRaw182',
		'dailyRaw5'];

	// sister2 is used to check with dailyMain
	const sister2Data = ['dailyRaw190',
		'dailyRaw56',
		'dailyRaw142',
		'dailyRaw188',
		'dailyRaw190',
		'dailyRaw56',
		'dailyRaw86',
		'dailyRaw15',
		'dailyRaw15',
		'dailyRaw54',
		'dailyRaw5', 
		'dailyRaw146', 
		'dailyRaw54',
		'dailyRaw54',
		'dailyRaw148',
		'dailyRaw7',
		'dailyRaw148',
		'dailyRaw206',
		'dailyRaw194',
		'dailyRaw194',
		'dailyRaw71',
		'dailyRaw71',
		'dailyRaw169', 
		'dailyRaw86',
		'dailyRaw169'];


	let pool = await sql.connect(config.sqlDatabase);

	try{

		console.log("im in the Function");

		for (let i = 0; i < dailyMainTable.length; i++) {



				let mainRequest = "SELECT * FROM " + dailyRawTable[i] + " Where Date >= @input_parameter And Date <= '"+ endDate +"' ORDER BY Date ASC";
				let sister1Request = "SELECT * FROM " + sister1Data[i] + " Where Date >= @input_parameter2 And Date <= '"+ endDate +"' ORDER BY Date ASC";
				let sister2Request = "SELECT * FROM " + sister2Data[i] + " Where Date >= @input_parameter3 And Date <= '"+ endDate +"' ORDER BY Date ASC";
				let tableRequest = "SELECT * FROM " + conTable[i] +   " Where Month >=  @input_parameter4";

				let mainTable = await pool.request()
					.input("input_parameter", sql.Date, startDate)
					.query(mainRequest);


				let sister1Table = await pool.request()
					.input("input_parameter2", sql.Date, startDate)
					.query(sister1Request);

				let sister2Table = await pool.request()
					.input("input_parameter3", sql.Date, startDate)
					.query(sister2Request);


				let result1 = await pool.request()
					.input("input_parameter4", sql.Float, 1 )
					.query(tableRequest);


			

				console.log(mainTable);
				console.log(sister1Table);
				console.log(sister2Table);
				console.log(mainTable.recordset.length);
			



			for (let j = 0; j < mainTable.recordset.length; j++) {


				let rawDate = mainTable.recordset[j].Date;
				let DayAirTmpMax = null;
				let DayAirTmpMin = null;
				let DayRelHumMax = null;
				let DayRelHumMin = null;
				let DayWindSpdAvg = null;
				let DayDewPnt = null;
				let DayEto = null;
				let DayAsceEto = null;
				let DayPrecip = null;
				let mCD = null;

				 

				h = rawDate.toISOString();
				contDate =  h[5] + h[6] + '/' + h[8] + h[9];



				for (let k = 0; k < result1.recordset.length; k++){

					//console.log(result1.recordset[i].Date);

					if (result1.recordset[k].Date == contDate){
						mCD = result1.recordset[k];
						console.log("im in");
						break;
					}
				}

				

				if (mainTable.recordset[j].DayAirTmpMax == null || mainTable.recordset[j].DayAirTmpMax == undefined || mainTable.recordset[j].DayAirTmpMax > 48 || mainTable.recordset[j].DayAirTmpMax < 0 ){

					// if sister1records is null or undefined, check sister2records
					if (sister1Table.recordset[j].DayAirTmpMax == null || sister1Table.recordset[j].DayAirTmpMax == undefined || sister1Table.recordset[j].DayAirTmpMax > 48 || sister1Table.recordset[j].DayAirTmpMax < 0 ){

						// if siter2records is null or undefined, just use the main record (nothing else to do)
						if(sister2Table.recordset[j].DayAirTmpMax == null || sister2Table.recordset[j].DayAirTmpMax == undefined || sister2Table.recordset[j].DayAirTmpMax > 48 || sister2Table.recordset[j].DayAirTmpMax < 0 ){
							DayAirTmpMax = parseFloat(mCD.Tmax);
						}

						// else, sister2Records is NOT NULL, set the variable to sister2records
						else {
							DayAirTmpMax = parseFloat(sister2Table.recordset[j].DayAirTmpMax);
						}

					}

					// else, sister1records is NOT NULL, set the variable to sister1records
					else {
						DayAirTmpMax = parseFloat(sister1Table.recordset[j].DayAirTmpMax);
					}
				}

				else {
					DayAirTmpMax = parseFloat(mainTable.recordset[j].DayAirTmpMax);

				}




				if (mainTable.recordset[j].DayAirTmpMin == null || mainTable.recordset[j].DayAirTmpMin == undefined || mainTable.recordset[j].DayAirTmpMin > 30 || mainTable.recordset[j].DayAirTmpMin < -12 ){

					// if sister1records is null or undefined, check sister2records
					if (sister1Table.recordset[j].DayAirTmpMin == null || sister1Table.recordset[j].DayAirTmpMin == undefined || sister1Table.recordset[j].DayAirTmpMin > 30 || sister1Table.recordset[j].DayAirTmpMin < -12 ){

						// if siter2records is null or undefined, just use the main record (nothing else to do)
						if(sister2Table.recordset[j].DayAirTmpMin == null || sister2Table.recordset[j].DayAirTmpMin == undefined || sister2Table.recordset[j].DayAirTmpMin > 30 || sister2Table.recordset[j].DayAirTmpMin < -12 ){
							DayAirTmpMin = parseFloat(mCD.Tmin);
						}

						// else, sister2Records is NOT NULL, set the variable to sister2records
						else {
							DayAirTmpMin = parseFloat(sister2Table.recordset[j].DayAirTmpMin);
						}

					}

					// else, sister1records is NOT NULL, set the variable to sister1records
					else {
						DayAirTmpMin = parseFloat(sister1Table.recordset[j].DayAirTmpMin);
					}
				}

				else {
					DayAirTmpMin = parseFloat(mainTable.recordset[j].DayAirTmpMin);

				}




				if (mainTable.recordset[j].DayRelHumMax == null || mainTable.recordset[j].DayRelHumMax == undefined || mainTable.recordset[j].DayRelHumMax > 100 || mainTable.recordset[j].DayRelHumMax < 30 ){

					// if sister1records is null or undefined, check sister2records
					if (sister1Table.recordset[j].DayRelHumMax == null || sister1Table.recordset[j].DayRelHumMax == undefined || sister1Table.recordset[j].DayRelHumMax > 100 || sister1Table.recordset[j].DayRelHumMax < 30 ){

						// if siter2records is null or undefined, just use the main record (nothing else to do)
						if(sister2Table.recordset[j].DayRelHumMax == null || sister2Table.recordset[j].DayRelHumMax == undefined || sister2Table.recordset[j].DayRelHumMax > 100 || sister2Table.recordset[j].DayRelHumMax < 30 ){
							DayRelHumMax = parseFloat(mCD.Rhmax);
						}

						// else, sister2Records is NOT NULL, set the variable to sister2records
						else {
							DayRelHumMax = parseFloat(sister2Table.recordset[j].DayRelHumMax);
						}

					}

					// else, sister1records is NOT NULL, set the variable to sister1records
					else {
						DayRelHumMax = parseFloat(sister1Table.recordset[j].DayRelHumMax);
					}
				}

				else {
					DayRelHumMax = parseFloat(mainTable.recordset[j].DayRelHumMax);

				}




				if (mainTable.recordset[j].DayRelHumMin == null || mainTable.recordset[j].DayRelHumMin == undefined || mainTable.recordset[j].DayRelHumMin > 100 || mainTable.recordset[j].DayRelHumMin < 7 ){

					// if sister1records is null or undefined, check sister2records
					if (sister1Table.recordset[j].DayRelHumMin == null || sister1Table.recordset[j].DayRelHumMin == undefined || sister1Table.recordset[j].DayRelHumMin > 100 || sister1Table.recordset[j].DayRelHumMin < 7 ){

						// if siter2records is null or undefined, just use the main record (nothing else to do)
						if(sister2Table.recordset[j].DayRelHumMin == null || sister2Table.recordset[j].DayRelHumMin == undefined || sister2Table.recordset[j].DayRelHumMin > 100 || sister2Table.recordset[j].DayRelHumMin < 7 ){
							DayRelHumMin = parseFloat(mCD.Rhmin);
						}

						// else, sister2Records is NOT NULL, set the variable to sister2records
						else {
							DayRelHumMin = parseFloat(sister2Table.recordset[j].DayRelHumMin);
						}

					}

					// else, sister1records is NOT NULL, set the variable to sister1records
					else {
						DayRelHumMin = parseFloat(sister1Table.recordset[j].DayRelHumMin);
					}
				}

				else {
					DayRelHumMin = parseFloat(mainTable.recordset[j].DayRelHumMin);

				}




				if (mainTable.recordset[j].DayWindSpdAvg == null || mainTable.recordset[j].DayWindSpdAvg == undefined || mainTable.recordset[j].DayWindSpdAvg > 10 || mainTable.recordset[j].DayWindSpdAvg < 0.2 ){

					// if sister1records is null or undefined, check sister2records
					if (sister1Table.recordset[j].DayWindSpdAvg == null || sister1Table.recordset[j].DayWindSpdAvg == undefined || sister1Table.recordset[j].DayWindSpdAvg > 10 || sister1Table.recordset[j].DayWindSpdAvg < 0.2 ){

						// if siter2records is null or undefined, just use the main record (nothing else to do)
						if(sister2Table.recordset[j].DayWindSpdAvg == null || sister2Table.recordset[j].DayWindSpdAvg == undefined || sister2Table.recordset[j].DayWindSpdAvg > 10 || sister2Table.recordset[j].DayWindSpdAvg < 0.2 ){
							DayWindSpdAvg = parseFloat(mCD.Wind);
						}

						// else, sister2Records is NOT NULL, set the variable to sister2records
						else {
							DayWindSpdAvg = parseFloat(sister2Table.recordset[j].DayWindSpdAvg);
						}

					}

					// else, sister1records is NOT NULL, set the variable to sister1records
					else {
						DayWindSpdAvg = parseFloat(sister1Table.recordset[j].DayWindSpdAvg);
					}
				}

				else {
					DayWindSpdAvg = parseFloat(mainTable.recordset[j].DayWindSpdAvg);

				}




				if (mainTable.recordset[j].DayDewPnt == null || mainTable.recordset[j].DayDewPnt == undefined ){

					// if sister1records is null or undefined, check sister2records
					if (sister1Table.recordset[j].DayDewPnt == null || sister1Table.recordset[j].DayDewPnt == undefined ){

						// if siter2records is null or undefined, just use the main record (nothing else to do)
						if(sister2Table.recordset[j].DayDewPnt == null || sister2Table.recordset[j].DayDewPnt == undefined ){
							DayDewPnt = parseFloat(0);
						}

						// else, sister2Records is NOT NULL, set the variable to sister2records
						else {
							DayDewPnt = parseFloat(sister2Table.recordset[j].DayDewPnt);
						}

					}

					// else, sister1records is NOT NULL, set the variable to sister1records
					else {
						DayDewPnt = parseFloat(sister1Table.recordset[j].DayDewPnt);
					}
				}

				else {
					DayDewPnt = parseFloat(mainTable.recordset[j].DayDewPnt);

				}




				if (mainTable.recordset[j].DayEto == null || mainTable.recordset[j].DayEto == undefined || mainTable.recordset[j].DayEto > 13 || mainTable.recordset[j].DayEto < 0 ){

					// if sister1records is null or undefined, check sister2records
					if (sister1Table.recordset[j].DayEto == null || sister1Table.recordset[j].DayEto == undefined || sister1Table.recordset[j].DayEto > 13 || sister1Table.recordset[j].DayEto < 0 ){

						// if siter2records is null or undefined, just use the main record (nothing else to do)
						if(sister2Table.recordset[j].DayEto == null || sister2Table.recordset[j].DayEto == undefined || sister2Table.recordset[j].DayEto > 13 || sister2Table.recordset[j].DayEto < 0 ){
							DayEto = parseFloat(mCD.Eto);
						}

						// else, sister2Records is NOT NULL, set the variable to sister2records
						else {
							DayEto = parseFloat(sister2Table.recordset[j].DayEto);
						}

					}

					// else, sister1records is NOT NULL, set the variable to sister1records
					else {
						DayEto = parseFloat(sister1Table.recordset[j].DayEto);
					}
				}

				else {
					DayEto = parseFloat(mainTable.recordset[j].DayEto);

				}




				if (mainTable.recordset[j].DayAsceEto == null || mainTable.recordset[j].DayAsceEto == undefined || mainTable.recordset[j].DayAsceEto > 13 || mainTable.recordset[j].DayAsceEto < 0 ){

					// if sister1records is null or undefined, check sister2records
					if (sister1Table.recordset[j].DayAsceEto == null || sister1Table.recordset[j].DayAsceEto == undefined || sister1Table.recordset[j].DayAsceEto > 13 || sister1Table.recordset[j].DayAsceEto < 0 ){

						// if siter2records is null or undefined, just use the main record (nothing else to do)
						if(sister2Table.recordset[j].DayAsceEto == null || sister2Table.recordset[j].DayAsceEto == undefined || sister2Table.recordset[j].DayAsceEto > 13 || sister2Table.recordset[j].DayAsceEto < 0 ){
							DayAsceEto = parseFloat(mCD.AsceETo);
						}

						// else, sister2Records is NOT NULL, set the variable to sister2records
						else {
							DayAsceEto = parseFloat(sister2Table.recordset[j].DayAsceEto);
						}

					}

					// else, sister1records is NOT NULL, set the variable to sister1records
					else {
						DayAsceEto = parseFloat(sister1Table.recordset[j].DayAsceEto);
					}
				}

				else {
					DayAsceEto = parseFloat(mainTable.recordset[j].DayAsceEto);

				}




				if (mainTable.recordset[j].DayPrecip == null || mainTable.recordset[j].DayPrecip == undefined || mainTable.recordset[j].DayPrecip > 75 || mainTable.recordset[j].DayPrecip < 0 ){

					// if sister1records is null or undefined, check sister2records
					if (sister1Table.recordset[j].DayPrecip == null || sister1Table.recordset[j].DayPrecip == undefined || sister1Table.recordset[j].DayPrecip > 75 || sister1Table.recordset[j].DayPrecip < 0 ){

						// if siter2records is null or undefined, just use the main record (nothing else to do)
						if(sister2Table.recordset[j].DayPrecip == null || sister2Table.recordset[j].DayPrecip == undefined || sister2Table.recordset[j].DayPrecip > 75 || sister2Table.recordset[j].DayPrecip < 0 ){
							DayPrecip = parseFloat(mCD.Precip);
						}

						// else, sister2Records is NOT NULL, set the variable to sister2records
						else {
							DayPrecip = parseFloat(sister2Table.recordset[j].DayPrecip);
						}

					}

					// else, sister1records is NOT NULL, set the variable to sister1records
					else {
						DayPrecip = parseFloat(sister1Table.recordset[j].DayPrecip);
					}
				}

				else {
					DayPrecip = parseFloat(mainTable.recordset[j].DayPrecip);

				}


				try{

					d = rawDate.toISOString();
					strDate = d[0] + d[1] + d[2] + d[3] + d[4]+ d[5] + d[6] + d[7] + d[8] + d[9];

					console.log(" This is the Date " + strDate );
					console.log(" This is DayAirTmpMax " + DayAirTmpMax );
					console.log(" This is DayAirTmpMin " + DayAirTmpMin );
					console.log(" This is DayRelHumMax " + DayRelHumMax );
					console.log(" This is DayRelHumMin " + DayRelHumMin );
					console.log(" This is DayWindSpdAvg " + DayWindSpdAvg );
					console.log(" This is DayDewPnt " + DayDewPnt );
					console.log(" This is DayEto " + DayEto );
					console.log(" This is DayAsceEto " + DayAsceEto );
					console.log(" This is DayPrecip " + DayPrecip );


					let insertRequest2 = "INSERT INTO " + dailyMainTable[i] + 
						"(Date," +
						" DayAirTmpMax," +
						" DayAirTmpMin," + 
						" DayRelHumMax," +
						" DayRelHumMin," + 
						" DayWindSpdAvg," +
						" DayDewPnt," +
						" DayEto," +
						" DayAsceEto," + 
						" DayPrecip)" +

						" VALUES " + 
						"(@Date," +
						" @DayAirTmpMax," +
						" @DayAirTmpMin," + 
						" @DayRelHumMax," +
						" @DayRelHumMin," + 
						" @DayWindSpdAvg," +
						" @DayDewPnt," +
						" @DayEto," +
						" @DayAsceEto," + 
						" @DayPrecip)";

					// send dailyMainTable insertRequest2 to SQL
					let req2 = await pool.request()						
						// tell the request what data types are
						.input("Date", sql.Date, strDate)
						.input("DayAirTmpMax", sql.Float, DayAirTmpMax)
						.input("DayAirTmpMin", sql.Float, DayAirTmpMin)
						.input("DayRelHumMax", sql.Float, DayRelHumMax)
						.input("DayRelHumMin", sql.Float, DayRelHumMin)
						.input("DayWindSpdAvg", sql.Float, DayWindSpdAvg)
						.input("DayDewPnt", sql.Float, DayDewPnt)
						.input("DayEto", sql.Float, DayEto)					
						.input("DayAsceEto", sql.Float, DayAsceEto)		
						.input("DayPrecip", sql.Float, DayPrecip)

						.query(insertRequest2);


					console.log("Inserted records" + j + " into " + dailyMainTable[i] + " and it is on " + strDate );

						}

						catch (err) {
							console.log('uniqueID');
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

	

exports.insertAlldailyMain = insertAlldailyMain

