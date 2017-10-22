(function () {
	  // Initialize Firebase
      var config = {
        apiKey: "AIzaSyBdC5IFAhQx7m8LDPg8NZln7rPU4QwyQRQ",
        authDomain: "open-pool.firebaseapp.com",
        databaseURL: "https://open-pool.firebaseio.com",
        projectId: "open-pool",
        storageBucket: "open-pool.appspot.com",
        messagingSenderId: "569437181618"
      };
 
	firebase.initializeApp(config);

	angular
		.module('openPool', ['firebase'])
		.controller('MyController', function($fireBaseObject) {
			const rootRef = firebase.dataBase().ref().child('angular');	
			const ref = rootRef.child('object');
			this.object = $fireBaseObject(ref);
		});

}());
