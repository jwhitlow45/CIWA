const ser = require('./server');
module.exports = async function (context, myTimer) {
    var timeStamp = new Date().toISOString();

    ser.expServer();
    
    if (myTimer.IsPastDue)
    {
        context.log('JavaScript is running late!');
    }
    context.log('JavaScript timer trigger function ran!', timeStamp);   
};