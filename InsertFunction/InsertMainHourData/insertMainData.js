const sql = require('mssql');
const config = require('./config');




async function insertMainData() {


// startDate will be used to select which starting date to call the Json file from our SQL table
var date1 = new Date();
date1.setDate(date1.getDate() -1);
var a = date1.toISOString();
var start = a[0] + a[1] + a[2] + a[3] + a[4]+ a[5] + a[6] + a[7] + a[8] + a[9];
console.log(start);

// endDate will be use to select where to stop on the called upn json file
// the reason why there are two seperate variables is because if there needs to be manual adjustments,
// we can go back and call different range of dates

var date2 = new Date();
date2.setDate(date2.getDate() -1);
var b = date2.toISOString();
var end = b[0] + b[1] + b[2] + b[3] + b[4]+ b[5] + b[6] + b[7] + b[8] + b[9];
console.log(end);



// mainDataTable will be used to select the table in which the data goes into
	const mainHourTable = ['hourlyMain2',
		'hourlyMain7',
		'hourlyMain39',
		'hourlyMain80',
		'hourlyMain105',
		'hourlyMain124',
		'hourlyMain142',
		'hourlyMain190',
		'hourlyMain205',
		'hourlyMain5',
		'hourlyMain54', 
		'hourlyMain125', 
		'hourlyMain146',
		'hourlyMain15',
		'hourlyMain188',
		'hourlyMain56',
		'hourlyMain92',
		'hourlyMain148',
		'hourlyMain70',
		'hourlyMain71',
		'hourlyMain194',
		'hourlyMain206',
		'hourlyMain86', 
		'hourlyMain169',
		'hourlyMain182'];



// we will be calling a json file from our tables 

	const rawDataTable = ['hourlyRaw2',
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



// first sisterStation encase rawDataTable data is missing
	const sister1Data = ['hourlyRaw15',
		'hourlyRaw124',
		'hourlyRaw80',
		'hourlyRaw39',
		'hourlyRaw7',
		'hourlyRaw7',
		'hourlyRaw39',
		'hourlyRaw2',
		'hourlyRaw2',
		'hourlyRaw146',
		'hourlyRaw146', 
		'hourlyRaw5', 
		'hourlyRaw5',
		'hourlyRaw2',
		'hourlyRaw80',
		'hourlyRaw124',
		'hourlyRaw56',
		'hourlyRaw188',
		'hourlyRaw71',
		'hourlyRaw70',
		'hourlyRaw206',
		'hourlyRaw194',
		'hourlyRaw142', 
		'hourlyRaw182',
		'hourlyRaw5'];

// second sisterStation
// all arrays are ligned up correctly to associated tables

	const sister2Data = ['hourlyRaw190',
		'hourlyRaw56',
		'hourlyRaw142',
		'hourlyRaw188',
		'hourlyRaw190',
		'hourlyRaw56',
		'hourlyRaw86',
		'hourlyRaw15',
		'hourlyRaw15',
		'hourlyRaw54',
		'hourlyRaw5', 
		'hourlyRaw146', 
		'hourlyRaw54',
		'hourlyRaw54',
		'hourlyRaw148',
		'hourlyRaw7',
		'hourlyRaw148',
		'hourlyRaw206',
		'hourlyRaw194',
		'hourlyRaw194',
		'hourlyRaw71',
		'hourlyRaw71',
		'hourlyRaw169', 
		'hourlyRaw86',
		'hourlyRaw169'];


	const conTable = ['hourlyHist2',
		'hourlyHist7',
		'hourlyHist39',
		'hourlyHist80',
		'hourlyHist105',
		'hourlyHist124',
		'hourlyHist142',
		'hourlyHist190',
		'hourlyHist205',
		'hourlyHist5',
		'hourlyHist54',
		'hourlyHist125', 
		'hourlyHist146',
		'hourlyHist15',
		'hourlyHist188',
		'hourlyHist56',
		'hourlyHist92',
		'hourlyHist148',
		'hourlyHist70',
		'hourlyHist71',
		'hourlyHist194',
		'hourlyHist206',
		'hourlyHist86', 
		'hourlyHist169',
		'hourlyHist182'];



	let pool = await sql.connect(config.sqlDatabase);

	try{

		console.log("im in the Function");

		for (let i = 0; i < mainHourTable.length; i++) {


				let endDate = end + " 23:00:00"
				let startDate = start + " 00:00:00"

				console.log(endDate)
				console.log(startDate)


				// These requests will be used to call the Json files from our Database
				let mainRequest = "SELECT * FROM " + rawDataTable[i] + " Where Date >= @input_parameter And Date <= '"+ endDate +"' ORDER BY Date ASC";
				let sister1Request = "SELECT * FROM " + sister1Data[i] + " Where Date >= @input_parameter2 And Date <= '"+ endDate +"' ORDER BY Date ASC";
				let sister2Request = "SELECT * FROM " + sister2Data[i] + " Where Date >= @input_parameter3 And Date <= '"+ endDate +"' ORDER BY Date ASC";
				let contingency = "SELECT * FROM " + conTable[i] +   " Where Month >=  @input_parameter4 ORDER BY Date ASC";

				let rawTable = await pool.request()
					.input("input_parameter", sql.VarChar(), startDate)
					.query(mainRequest);


				let sister1Table = await pool.request()
					.input("input_parameter2", sql.VarChar(), startDate)
					.query(sister1Request);

				let sister2Table = await pool.request()
					.input("input_parameter3", sql.VarChar(), startDate)
					.query(sister2Request);

				let contT = await pool.request()
					.input("input_parameter4", sql.Float, 1 )
					.query(contingency);

				
			
				// these log used for testing purposes 
/*				
				console.log(rawTable);
				console.log(sister1Table);
				console.log(sister2Table);
				
				console.log(rawTable.recordset.length);
				console.log(sister1Table.recordset.length)
				console.log(sister2Table.recordset.length)
				console.log(contT.recordset.length)
				console.log(contT)
*/


			for (let j = 0; j < rawTable.recordset.length; j++ ) {


				let myHourDate = rawTable.recordset[j].Date;
				let HlyAirTmp = null;
				let HlyDewPnt = null;
				let HlyPrecip = null;
				let HlyRelHum = null;
				let HlySoilTmp = null;
				let HlyWindDir = null;
				let HlyWindSpd = null;
				let HlySolRad = null;
				let HlyEto = null;
				let HlyAsceEto = null;
				let mCD = null;


				h = myHourDate.toISOString();
				contDate = '2000-' + h[5] + h[6] + h[7] + h[8] + h[9] + ' ' + h[11] + h[12] + ':00:00.000 ';
				//console.log(contDate);
				//console.log(contT.recordset[j].Date)

				// we needed to create this for loop, The Date has a different format this was the way to work around it
				for (let k = 0; k < contT.recordset.length; k++){

					//console.log(contT.recordset[k]);

					// we will also create another variable that will store the data from result1 (conTable)
					if (contT.recordset[k].Date == contDate){
						mCD = contT.recordset[k];
						//console.log("im in");
						//console.log(mCD);
						break;
					}
				}




				// Checks for th HlyAirTmp 
				if (rawTable.recordset[j].HlyAirTmp == null || rawTable.recordset[j].HlyAirTmp == undefined || rawTable.recordset[j].HlyAirTmp > 48 || rawTable.recordset[j].HlyAirTmp < -12 ){

					// if sister1records is null or undefined, check sister2records
					if (sister1Table.recordset[j].HlyAirTmp == null || sister1Table.recordset[j].HlyAirTmp == undefined || sister1Table.recordset[j].HlyAirTmp > 48 || sister1Table.recordset[j].HlyAirTmp < -12 ){

						// if siter2records is null or undefined, just use the main record (nothing else to do)
						if(sister2Table.recordset[j].HlyAirTmp == null || sister2Table.recordset[j].HlyAirTmp == undefined || sister2Table.recordset[j].HlyAirTmp > 48 || sister2Table.recordset[j].HlyAirTmp < -12 ){
							
							// if evetything else fails use the value from the ContTable (variable become mCD."RowName" in this case mCD.Tmax)
							HlyAirTmp = parseFloat(mCD.HlyAirTmp);
						}

						// else, sister2Records is NOT NULL, set the variable to sister2records
						else {
							HlyAirTmp = parseFloat(sister2Table.recordset[j].HlyAirTmp);
						}

					}

					// else, sister1records is NOT NULL, set the variable to sister1records
					else {
						HlyAirTmp = parseFloat(sister1Table.recordset[j].HlyAirTmp);
					}
				}

				else {
					HlyAirTmp = parseFloat(rawTable.recordset[j].HlyAirTmp);

				}


				// Checks for the HlyDewPnt
				if (rawTable.recordset[j].HlyDewPnt == null || rawTable.recordset[j].HlyDewPnt == undefined ){

					// if sister1records is null or undefined, check sister2records
					if (sister1Table.recordset[j].HlyDewPnt == null || sister1Table.recordset[j].HlyDewPnt == undefined ){

						// if siter2records is null or undefined, just use the main record (nothing else to do)
						if(sister2Table.recordset[j].HlyDewPnt == null || sister2Table.recordset[j].HlyDewPnt == undefined ){
							
							// if evetything else fails use the value from the ContTable (variable become mCD."RowName" in this case mCD.Tmax)
							HlyDewPnt = parseFloat(mCD.HlyDewPnt);
						}

						// else, sister2Records is NOT NULL, set the variable to sister2records
						else {
							HlyDewPnt = parseFloat(sister2Table.recordset[j].HlyDewPnt);
						}

					}

					// else, sister1records is NOT NULL, set the variable to sister1records
					else {
						HlyDewPnt = parseFloat(sister1Table.recordset[j].HlyDewPnt);
					}
				}

				else {
					HlyDewPnt = parseFloat(rawTable.recordset[j].HlyDewPnt);

				}


				// Checks for the HlyPrecip
				if (rawTable.recordset[j].HlyPrecip == null || rawTable.recordset[j].HlyPrecip == undefined || rawTable.recordset[j].HlyPrecip > 75 || rawTable.recordset[j].HlyPrecip < 0 ){

					// if sister1records is null or undefined, check sister2records
					if (sister1Table.recordset[j].HlyPrecip == null || sister1Table.recordset[j].HlyPrecip == undefined || sister1Table.recordset[j].HlyPrecip > 75 || sister1Table.recordset[j].HlyPrecip < 0 ){

						// if siter2records is null or undefined, just use the main record (nothing else to do)
						if(sister2Table.recordset[j].HlyPrecip == null || sister2Table.recordset[j].HlyPrecip == undefined || sister2Table.recordset[j].HlyPrecip > 75 || sister2Table.recordset[j].HlyPrecip < 0 ){
							
							// if evetything else fails use the value from the ContTable (variable become mCD."RowName" in this case mCD.Tmax)
							HlyPrecip = parseFloat(mCD.HlyPrecip);
						}

						// else, sister2Records is NOT NULL, set the variable to sister2records
						else {
							HlyPrecip = parseFloat(sister2Table.recordset[j].HlyPrecip);
						}

					}

					// else, sister1records is NOT NULL, set the variable to sister1records
					else {
						HlyPrecip = parseFloat(sister1Table.recordset[j].HlyPrecip);
					}
				}

				else {
					HlyPrecip = parseFloat(rawTable.recordset[j].HlyPrecip);
				}


				// Checks for the HlyRelHum
				if (rawTable.recordset[j].HlyRelHum == null || rawTable.recordset[j].HlyRelHum == undefined || rawTable.recordset[j].HlyRelHum > 100 || rawTable.recordset[j].HlyRelHum < 7 ){

					// if sister1records is null or undefined, check sister2records
					if (sister1Table.recordset[j].HlyRelHum == null || sister1Table.recordset[j].HlyRelHum == undefined || sister1Table.recordset[j].HlyRelHum > 100 || sister1Table.recordset[j].HlyRelHum < 7 ){

						// if siter2records is null or undefined, just use the main record (nothing else to do)
						if(sister2Table.recordset[j].HlyRelHum == null || sister2Table.recordset[j].HlyRelHum == undefined || sister2Table.recordset[j].HlyRelHum > 100 || sister2Table.recordset[j].HlyRelHum < 7 ){
							
							// if evetything else fails use the value from the ContTable (variable become mCD."RowName" in this case mCD.Tmax)
							HlyRelHum = parseFloat(mCD.HlyRelHum);
						}

						// else, sister2Records is NOT NULL, set the variable to sister2records
						else {
							HlyRelHum = parseFloat(sister2Table.recordset[j].HlyRelHum);
						}

					}

					// else, sister1records is NOT NULL, set the variable to sister1records
					else {
						HlyRelHum = parseFloat(sister1Table.recordset[j].HlyRelHum);
					}
				}

				else {
					HlyRelHum = parseFloat(rawTable.recordset[j].HlyRelHum);
				}



				//Checks for the HlySoilTmp
				if (rawTable.recordset[j].HlySoilTmp == null || rawTable.recordset[j].HlySoilTmp == undefined || rawTable.recordset[j].HlySoilTmp > 40 || rawTable.recordset[j].HlySoilTmp < -12 ){

					// if sister1records is null or undefined, check sister2records
					if (sister1Table.recordset[j].HlySoilTmp == null || sister1Table.recordset[j].HlySoilTmp == undefined || sister1Table.recordset[j].HlySoilTmp > 40 || sister1Table.recordset[j].HlySoilTmp < -12 ){

						// if siter2records is null or undefined, just use the main record (nothing else to do)
						if(sister2Table.recordset[j].HlySoilTmp == null || sister2Table.recordset[j].HlySoilTmp == undefined || sister2Table.recordset[j].HlySoilTmp > 40 || sister2Table.recordset[j].HlySoilTmp < -12 ){
							
							// if evetything else fails use the value from the ContTable (variable become mCD."RowName" in this case mCD.Tmax)
							HlySoilTmp = parseFloat(mCD.HlySoilTmp);
						}

						// else, sister2Records is NOT NULL, set the variable to sister2records
						else {
							HlySoilTmp = parseFloat(sister2Table.recordset[j].HlySoilTmp);
						}

					}

					// else, sister1records is NOT NULL, set the variable to sister1records
					else {
						HlySoilTmp = parseFloat(sister1Table.recordset[j].HlySoilTmp);
					}
				}

				else {
					HlySoilTmp = parseFloat(rawTable.recordset[j].HlySoilTmp);
				}


				//Checks for the HlyWindDir
				if (rawTable.recordset[j].HlyWindDir == null || rawTable.recordset[j].HlyWindDir == undefined || rawTable.recordset[j].HlyWindDir > 360 || rawTable.recordset[j].HlyWindDir < 0 ){

					// if sister1records is null or undefined, check sister2records
					if (sister1Table.recordset[j].HlyWindDir == null || sister1Table.recordset[j].HlyWindDir == undefined || sister1Table.recordset[j].HlyWindDir > 360 || sister1Table.recordset[j].HlyWindDir < 0 ){

						// if siter2records is null or undefined, just use the main record (nothing else to do)
						if(sister2Table.recordset[j].HlyWindDir == null || sister2Table.recordset[j].HlyWindDir == undefined || sister2Table.recordset[j].HlyWindDir > 360 || sister2Table.recordset[j].HlyWindDir < 0 ){
							
							// if evetything else fails use the value from the ContTable (variable become mCD."RowName" in this case mCD.Tmax)
							HlyWindDir = parseFloat(mCD.HlyWindDir);
						}

						// else, sister2Records is NOT NULL, set the variable to sister2records
						else {
							HlyWindDir = parseFloat(sister2Table.recordset[j].HlyWindDir);
						}

					}

					// else, sister1records is NOT NULL, set the variable to sister1records
					else {
						HlyWindDir = parseFloat(sister1Table.recordset[j].HlyWindDir);
					}
				}

				else {
					HlyWindDir = parseFloat(rawTable.recordset[j].HlyWindDir);
				}


				//Checks for the HlyWindSpd
				if (rawTable.recordset[j].HlyWindSpd == null || rawTable.recordset[j].HlyWindSpd == undefined || rawTable.recordset[j].HlyWindSpd > 10 || rawTable.recordset[j].HlyWindSpd < 0.2 ){

					// if sister1records is null or undefined, check sister2records
					if (sister1Table.recordset[j].HlyWindSpd == null || sister1Table.recordset[j].HlyWindSpd == undefined || sister1Table.recordset[j].HlyWindSpd > 10 || sister1Table.recordset[j].HlyWindSpd < 0.2 ){

						// if siter2records is null or undefined, just use the main record (nothing else to do)
						if(sister2Table.recordset[j].HlyWindSpd == null || sister2Table.recordset[j].HlyWindSpd == undefined || sister2Table.recordset[j].HlyWindSpd > 10 || sister2Table.recordset[j].HlyWindSpd < 0.2 ){
							
							// if evetything else fails use the value from the ContTable (variable become mCD."RowName" in this case mCD.Tmax)
							HlyWindSpd = parseFloat(mCD.HlyWindSpd);
						}

						// else, sister2Records is NOT NULL, set the variable to sister2records
						else {
							HlyWindSpd = parseFloat(sister2Table.recordset[j].HlyWindSpd);
						}

					}

					// else, sister1records is NOT NULL, set the variable to sister1records
					else {
						HlyWindSpd = parseFloat(sister1Table.recordset[j].HlyWindSpd);
					}
				}

				else {
					HlyWindSpd = parseFloat(rawTable.recordset[j].HlyWindSpd);
				}


				//Checks for the HlySolarRadiation
				if (rawTable.recordset[j].HlySolRad == null || rawTable.recordset[j].HlySolRad == undefined || rawTable.recordset[j].HlySolRad > 1100 || rawTable.recordset[j].HlySolRad < 0 ){

					// if sister1records is null or undefined, check sister2records
					if (sister1Table.recordset[j].HlySolRad == null || sister1Table.recordset[j].HlySolRad == undefined || sister1Table.recordset[j].HlySolRad > 1100 || sister1Table.recordset[j].HlySolRad < 0 ){

						// if siter2records is null or undefined, just use the main record (nothing else to do)
						if(sister2Table.recordset[j].HlySolRad == null || sister2Table.recordset[j].HlySolRad == undefined || sister2Table.recordset[j].HlySolRad > 1100 || sister2Table.recordset[j].HlySolRad < 0 ){
							
							// if evetything else fails use the value from the ContTable (variable become mCD."RowName" in this case mCD.Tmax)
							HlySolRad = parseFloat(mCD.HlySolRad);
						
						}

						// else, sister2Records is NOT NULL, set the variable to sister2records
						else {
							HlySolRad = parseFloat(sister2Table.recordset[j].HlySolRad);
						}

					}

					// else, sister1records is NOT NULL, set the variable to sister1records
					else {
						HlySolRad = parseFloat(sister1Table.recordset[j].HlySolRad);
					}
				}

				else {
					HlySolRad = parseFloat(rawTable.recordset[j].HlySolRad);
				}


				//Checks for the HlyEto
				if (rawTable.recordset[j].HlyEto == null || rawTable.recordset[j].HlyEto == undefined || rawTable.recordset[j].HlyEto > 13 || rawTable.recordset[j].HlyEto < 0 ){

					// if sister1records is null or undefined, check sister2records
					if (sister1Table.recordset[j].HlyEto == null || sister1Table.recordset[j].HlyEto == undefined || sister1Table.recordset[j].HlyEto > 13 || sister1Table.recordset[j].HlyEto < 0 ){

						// if siter2records is null or undefined, just use the main record (nothing else to do)
						if(sister2Table.recordset[j].HlyEto == null || sister2Table.recordset[j].HlyEto == undefined || sister2Table.recordset[j].HlyEto > 13 || sister2Table.recordset[j].HlyEto < 0 ){
							
							// if evetything else fails use the value from the ContTable (variable become mCD."RowName" in this case mCD.Tmax)
							HlyEto = parseFloat(mCD.HlyEto);
						}

						// else, sister2Records is NOT NULL, set the variable to sister2records
						else {
							HlyEto = parseFloat(sister2Table.recordset[j].HlyEto);
						}

					}

					// else, sister1records is NOT NULL, set the variable to sister1records
					else {
						HlyEto = parseFloat(sister1Table.recordset[j].HlyEto);
					}
				}

				else {
					HlyEto = parseFloat(rawTable.recordset[j].HlyEto);
				}


				//Checks for the HlyAsceEto
				if (rawTable.recordset[j].HlyAsceEto == null || rawTable.recordset[j].HlyAsceEto == undefined || rawTable.recordset[j].HlyAsceEto > 13 || rawTable.recordset[j].HlyAsceEto < 0 ){

					// if sister1records is null or undefined, check sister2records
					if (sister1Table.recordset[j].HlyAsceEto == null || sister1Table.recordset[j].HlyAsceEto == undefined || sister1Table.recordset[j].HlyAsceEto > 13 || sister1Table.recordset[j].HlyAsceEto < 0 ){

						// if siter2records is null or undefined, just use the main record (nothing else to do)
						if(sister2Table.recordset[j].HlyAsceEto == null || sister2Table.recordset[j].HlyAsceEto == undefined || sister2Table.recordset[j].HlyAsceEto > 13 || sister2Table.recordset[j].HlyAsceEto < 0 ){
							
							// if evetything else fails use the value from the ContTable (variable become mCD."RowName" in this case mCD.Tmax)
							HlyAsceEto = parseFloat(mCD.HlyAsceEto);
						}

						// else, sister2Records is NOT NULL, set the variable to sister2records
						else {
							HlyAsceEto = parseFloat(sister2Table.recordset[j].HlyAsceEto);
						}

					}

					// else, sister1records is NOT NULL, set the variable to sister1records
					else {
						HlyAsceEto = parseFloat(sister1Table.recordset[j].HlyAsceEto);
					}
				}

				else {
					HlyAsceEto = parseFloat(rawTable.recordset[j].HlyAsceEto);
				}



				try{


					c = myHourDate.toISOString();
					let date = c[0] + c[1] + c[2] + c[3] + c[4] + c[5] + c[6] + c[7] + c[8] + c[9] + " " + c[11] + c[12] + ":00:00";

/*
					console.log("This is the Date " + date);
					console.log("This is the AirTmp " + HlyAirTmp);
					console.log("This is the DewPoint " + HlyDewPnt);
					console.log("This is the Precip " + HlyPrecip);
					console.log("This is the RelHum " + HlyRelHum);
					console.log("This is the SoilTmp " + HlySoilTmp);
					console.log("This is the WindDir " + HlyWindDir);
					console.log("This is the WindSpeed " + HlyWindSpd);
					console.log("This is the SolRad " + HlySolRad);
					console.log("This is the ETO " + HlyEto);
					console.log("This is the AsceETO " + HlyAsceEto);
					console.log(" ");
*/


					let insertRequest = "INSERT INTO " + mainHourTable[i] +
						"(Date," +
						" HlyAirTmp," +
						" HlyDewPnt," +
						" HlyPrecip," +
						" HlyRelHum," +
						" HlySoilTmp," +
						" HlyWindDir," +
						" HlyWindSpd," +
						" HlySolRad," +
						" HlyEto," +
						" HlyAsceEto)" +

						" VALUES " +
						"(@Date," +
						" @HlyAirTmp," +
						" @HlyDewPnt," +
						" @HlyPrecip," +
						" @HlyRelHum," +
						" @HlySoilTmp," +
						" @HlyWindDir," +
						" @HlyWindSpd," +
						" @HlySolRad," +
						" @HlyEto," +
						" @HlyAsceEto)";

					let req = await pool.request()


						.input("Date", sql.VarChar(), date)
						.input("HlyAirTmp", sql.Float, HlyAirTmp)
						.input("HlyDewPnt", sql.Float, HlyDewPnt)
						.input("HlyPrecip", sql.Float, HlyPrecip)
						.input("HlyRelHum", sql.Float, HlyRelHum)
						.input("HlySoilTmp", sql.Float, HlySoilTmp)
						.input("HlyWindDir", sql.Float, HlyWindDir)
						.input("HlyWindSpd", sql.Float, HlyWindSpd)
						.input("HlySolRad", sql.Float, HlySolRad)
						.input("HlyEto", sql.Float, HlyEto)
						.input("HlyAsceEto", sql.Float, HlyAsceEto)

						.query(insertRequest);

					console.log("Inserted records" + j + " into " + mainHourTable[i] + " and it is on " + date );

						}

						catch (err) {
							console.log("uniqueID");
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

	

exports.insertMainData = insertMainData

