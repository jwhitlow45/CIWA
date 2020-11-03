
const sql = require('mssql');
const config = require('./config');



async function insertHourlyMissingDates() {

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

	let pool = await sql.connect(config.sqlDatabase);

	

	try{


		for(let j = 0; j < hourlyRawTable.length; j++){


			// convert myDate into an ISO string and create rawDate variable
			// Decide how far back you want to inserdate by changing the "-1"
			var myDate = new Date();
			myDate.setDate(myDate.getDate() -1);
			var d = myDate.toISOString();
			var rawDate = d[0] + d[1] + d[2] + d[3] + d[4]+ d[5] + d[6] + d[7] + d[8] + d[9];
			console.log("rawDate " + rawDate);


			// convert otherDate into an ISO string and create limitDate variable
			var otherDate = new Date();
			otherDate.setDate(otherDate.getDate());
			var s = otherDate.toISOString();
			var limitDate = s[0] + s[1] + s[2] + s[3] + s[4]+ s[5] + s[6] + s[7] + s[8] + s[9];
			console.log("limitDate " + limitDate);


			
			// j is used for our date counter 
			var k = 0;

			// while loop runs as long as the rawDate is not equal to limitDate
			// in this case we use the variable limitDate and subtract 1 to it since Cimis is a day behind
			// if we want to go back further we can adjust rawDate 

			while (rawDate != limitDate){

				let hour00 = rawDate + " 00:00:00";
				let hour01 = rawDate + " 01:00:00";
				let hour02 = rawDate + " 02:00:00";
				let hour03 = rawDate + " 03:00:00";
				let hour04 = rawDate + " 04:00:00";
				let hour05 = rawDate + " 05:00:00";
				let hour06 = rawDate + " 06:00:00";
				let hour07 = rawDate + " 07:00:00";
				let hour08 = rawDate + " 08:00:00";
				let hour09 = rawDate + " 09:00:00";
				let hour10 = rawDate + " 10:00:00";
				let hour11 = rawDate + " 11:00:00";
				let hour12 = rawDate + " 12:00:00";
				let hour13 = rawDate + " 13:00:00";
				let hour14 = rawDate + " 14:00:00";
				let hour15 = rawDate + " 15:00:00";
				let hour16 = rawDate + " 16:00:00";
				let hour17 = rawDate + " 17:00:00";
				let hour18 = rawDate + " 18:00:00";
				let hour19 = rawDate + " 19:00:00";
				let hour20 = rawDate + " 20:00:00";
				let hour21 = rawDate + " 21:00:00";
				let hour22 = rawDate + " 22:00:00";
				let hour23 = rawDate + " 23:00:00";

				try{

					let insertHourlyDates = 
						"INSERT INTO " + hourlyRawTable[j] + "(Date)" + " VALUES " + "(@Date00)" +
						"INSERT INTO " + hourlyRawTable[j] + "(Date)" + " VALUES " + "(@Date01)" +
						"INSERT INTO " + hourlyRawTable[j] + "(Date)" + " VALUES " + "(@Date02)" +
						"INSERT INTO " + hourlyRawTable[j] + "(Date)" + " VALUES " + "(@Date03)" +
						"INSERT INTO " + hourlyRawTable[j] + "(Date)" + " VALUES " + "(@Date04)" +
						"INSERT INTO " + hourlyRawTable[j] + "(Date)" + " VALUES " + "(@Date05)" +
						"INSERT INTO " + hourlyRawTable[j] + "(Date)" + " VALUES " + "(@Date06)" +
						"INSERT INTO " + hourlyRawTable[j] + "(Date)" + " VALUES " + "(@Date07)" +
						"INSERT INTO " + hourlyRawTable[j] + "(Date)" + " VALUES " + "(@Date08)" +
						"INSERT INTO " + hourlyRawTable[j] + "(Date)" + " VALUES " + "(@Date09)" +
						"INSERT INTO " + hourlyRawTable[j] + "(Date)" + " VALUES " + "(@Date10)" +
						"INSERT INTO " + hourlyRawTable[j] + "(Date)" + " VALUES " + "(@Date11)" +
						"INSERT INTO " + hourlyRawTable[j] + "(Date)" + " VALUES " + "(@Date12)" +
						"INSERT INTO " + hourlyRawTable[j] + "(Date)" + " VALUES " + "(@Date13)" +
						"INSERT INTO " + hourlyRawTable[j] + "(Date)" + " VALUES " + "(@Date14)" +
						"INSERT INTO " + hourlyRawTable[j] + "(Date)" + " VALUES " + "(@Date15)" +
						"INSERT INTO " + hourlyRawTable[j] + "(Date)" + " VALUES " + "(@Date16)" +
						"INSERT INTO " + hourlyRawTable[j] + "(Date)" + " VALUES " + "(@Date17)" +
						"INSERT INTO " + hourlyRawTable[j] + "(Date)" + " VALUES " + "(@Date18)" +
						"INSERT INTO " + hourlyRawTable[j] + "(Date)" + " VALUES " + "(@Date19)" +
						"INSERT INTO " + hourlyRawTable[j] + "(Date)" + " VALUES " + "(@Date20)" +
						"INSERT INTO " + hourlyRawTable[j] + "(Date)" + " VALUES " + "(@Date21)" +
						"INSERT INTO " + hourlyRawTable[j] + "(Date)" + " VALUES " + "(@Date22)" +
						"INSERT INTO " + hourlyRawTable[j] + "(Date)" + " VALUES " + "(@Date23)" ;


					

					// send insert data request to SQL
					let req00 = await pool.request()
						.input("Date00", sql.VarChar(), hour00)
						.input("Date01", sql.VarChar(), hour01)
						.input("Date02", sql.VarChar(), hour02)
						.input("Date03", sql.VarChar(), hour03)
						.input("Date04", sql.VarChar(), hour04)
						.input("Date05", sql.VarChar(), hour05)
						.input("Date06", sql.VarChar(), hour06)
						.input("Date07", sql.VarChar(), hour07)
						.input("Date08", sql.VarChar(), hour08)
						.input("Date09", sql.VarChar(), hour09)
						.input("Date10", sql.VarChar(), hour10)
						.input("Date11", sql.VarChar(), hour11)
						.input("Date12", sql.VarChar(), hour12)
						.input("Date13", sql.VarChar(), hour13)
						.input("Date14", sql.VarChar(), hour14)
						.input("Date15", sql.VarChar(), hour15)
						.input("Date16", sql.VarChar(), hour16)
						.input("Date17", sql.VarChar(), hour17)
						.input("Date18", sql.VarChar(), hour18)
						.input("Date19", sql.VarChar(), hour19)
						.input("Date20", sql.VarChar(), hour20)
						.input("Date21", sql.VarChar(), hour21)
						.input("Date22", sql.VarChar(), hour22)
						.input("Date23", sql.VarChar(), hour23)
						.query(insertHourlyDates);
						console.log( "inserted Date " + rawDate + " into " + hourlyRawTable[j]);
						


				}

				catch(err){


					console.log("unique ID on " + hourlyRawTable[j] + " on Date " + rawDate );

					// add 1 to myDate to keep track
					myDate.setDate(myDate.getDate() + 1); 

					// update d for while loop comparison 
					d = myDate.toISOString();
					rawDate = d[0] + d[1] + d[2] + d[3] + d[4]+ d[5] + d[6] + d[7] + d[8] + d[9];

					// increase j
					k++; 

				// if we get Unique Id error from SQL skip to next table
				continue;

					}
				}
			}
		}

				catch(err){

	}
			
}





exports.insertHourlyMissingDates = insertHourlyMissingDates



