class Pool {
    constructor(users,beginConditions,endConditions,totalValue,stockOptions) {
        this.users = users;
        this.beginConditions = beginConditions;
        this.endConditions = endConditions;
        this.totalValue = totalValue;
        this.stockOptions = stockOptions;
    }
    addUser(user) {
        this.users.push(user);
        user.activePools.push(this);
    }
}

class User {
    constructor(screenName,auth,activePools,bankId) {
        this.screenName = screenName;
        this.auth = auth;
        this.activePools = activePools;
        this.bankId = bankId;
    }
}

var user = new User("Nico","ex.",[],"59eb7ee4b390353c953a1559");
var pool = new Pool([],[],[],0.0,["AAPL","TSLA","FB"]);
pool.addUser(user);
console.log(pool.users[0].screenName);