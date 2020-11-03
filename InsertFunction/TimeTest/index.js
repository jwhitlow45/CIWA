


module.exports = async function (context, myTimer) {
    var timeStamp = new Date().toISOString();

    var date1 = new Date();
    date1.setDate(date1.getDate()-1);
    var a = date1.toISOString();
    context.log("This is my Date Test " + a);
    
    
    if (myTimer.IsPastDue)
    {
        context.log('JavaScript is running late!');
    }
    context.log('JavaScript timer trigger function ran!', timeStamp);   
};