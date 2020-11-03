const sql = require('mssql');
const config = require('./config');



async function insertMissingDates() {

	//dailyRaw tables 
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
		'dailyRaw182',
        'test1rawJava'];

	let pool = await sql.connect(config.sqlDatabase);

	try{

		//go through each dailyRaw table
		for(let i = 0; i < dailyRawTable.length; i++){

			// convert myDate into an ISO string 
			var myDate = new Date();
			myDate.setDate(myDate.getDate() -1);
			var d = myDate.toISOString();
			var rawDate = d[0] + d[1] + d[2] + d[3] + d[4]+ d[5] + d[6] + d[7] + d[8] + d[9];
			console.log("rawDate " + rawDate);


			var otherDate = new Date();
			otherDate.setDate(otherDate.getDate() );
			var s = otherDate.toISOString();
			var limitDate = s[0] + s[1] + s[2] + s[3] + s[4]+ s[5] + s[6] + s[7] + s[8] + s[9];
			console.log("limitDate " + limitDate);


			
			// j is used for our date counter 
			var j = 0;

			// make the "2019-01-20" another date variable so it can change on its own as well. 
			while (rawDate != limitDate){

				try {

				let insertdailyRaw = "INSERT INTO " + dailyRawTable[i] + "(Date)" + " VALUES " + "(@Date)";
				// send insert data request to SQL
				let req = await pool.request()
					.input("Date", sql.Date, rawDate)
					.query(insertdailyRaw);
					console.log( "inserted rawDate " + rawDate + " into " + dailyRawTable[i]);
				}

				catch(err){

					console.log(" uniqueID ");

					// add 1 to myDate to keep track
					myDate.setDate(myDate.getDate() + 1); 

				// update d for while loop comparison 
					d = myDate.toISOString();
					rawDate = d[0] + d[1] + d[2] + d[3] + d[4]+ d[5] + d[6] + d[7] + d[8] + d[9];

				// increase j
					j++; 


				// if we get Unique Id error from SQL skip to next table
				continue;
					}
				}
			}
		}

				catch(err){

	}
			
}





exports.insertMissingDates = insertMissingDates


