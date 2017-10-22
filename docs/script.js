var config = {
  apiKey: "AIzaSyBdC5IFAhQx7m8LDPg8NZln7rPU4QwyQRQ",
  authDomain: "open-pool.firebaseapp.com",
  databaseURL: "https://open-pool.firebaseio.com",
  projectId: "open-pool",
  storageBucket: "open-pool.appspot.com",
  messagingSenderId: "569437181618"
};
firebase.initializeApp(config);
var app = angular.module("openPool", ["firebase", "ui.bootstrap"]);


// let's create a re-usable factory that generates the $firebaseAuth instance
app.factory("Auth", ["$firebaseAuth",
  function($firebaseAuth) {
    return $firebaseAuth();
  }
]);

var provider = new firebase.auth.GoogleAuthProvider();


// a factory to create a re-usable profile object
// we pass in a username and get back their synchronized data
app.factory("Pool", ["$firebaseObject",
  function($firebaseObject) {
    return function() {
      // create a reference to the database node where we will store our data
      var ref = firebase.database().ref("pools").push();
      //var profileRef = ref.child(username);

      // return it as a synchronized object
      return $firebaseObject(ref);
    }
  }
]);

// factory for reading high level lists, like "pools"
app.factory("ObjectsList", ["$firebaseArray",
  function($firebaseArray) {
    return function(database_name) {
      // create a reference to the database node where we will store our data
      var ref = firebase.database().ref(database_name);

      // return it as a synchronized object
      return $firebaseArray(ref);
    }
  }
]);
// object factory for syncted user data 
app.factory("User", ["$firebaseObject",
  function($firebaseObject) {
    return function(username) {
      // create a reference to the database node where we will store our data
      var ref = firebase.database().ref("users");
      var profileRef = ref.child(username);

      
      // return it as a synchronized object
      return $firebaseObject(profileRef);
    }
  }
]);


app.controller('myCtrl', function($scope, Pool, User, ObjectsList) {
    $scope.userid = "no user";
    //login
    $scope.login = function() {
      firebase.auth().signInWithRedirect(provider);
      $scope.userid = "loading account, please wait.";
    };
    //logout
    $scope.logout = function() {
      firebase.auth().signOut().then(function() {
        $scope.userid = "log out";
        $scope.$apply();
        location.reload();
      }, function(error) {
        console.log(error);
      });
    };

    //login callback
    firebase.auth().getRedirectResult().then(function(result) {
      console.log("got result")
      if (result.credential) {
        // This gives you a Google Access Token. You can use it to access the Google API.
        var token = result.credential.accessToken;
        var email = result.user.email;
        console.log("got token", email, token)
        //extract email prefix to use as unique ID TODO: don't do this
        $scope.userid = email.substring(0, email.indexOf("@"));
        //create synced user for submitting user info
        $scope.user = User($scope.userid)
        $scope.user.$loaded().then(function(stuff) {
          console.log("user loaded" + $scope.user.token);
          if ($scope.user.token === undefined){
          console.log($scope.user.token);
            $scope.user.userid= $scope.userid;

            //fill up with data in admin-side format
            $scope.user.token = token;
            $scope.user.usd_balance = 50;
            $scope.user.screen_name = result.user.displayName;
            $scope.user.picture = result.user.photoURL;
            $scope.user.email_address = result.user.email;
            $scope.user.$save().then(function(){
              console.log("Your user stuff:");
              }).catch(function(error){alert('Error!');})
          } else {
            console.log("Account already exists");
          }
          //console.log($scope.user);
          $scope.showUserInfo();
          //$scope.$apply();
        });
      }
    }).catch(function(error) {
      console.log(error);
    });

    $scope.newpool = Pool();
    //save user's new pool
    $scope.saveNewPool = function() {
      if ($scope.user === undefined){
        alert("please sign in first");
      } else {
		$scope.hidePoolForm()
        $scope.newpool.number_investors = 1;
        $scope.newpool.creator = $scope.user.userid;
        $scope.newpool.investors = {}
        $scope.newpool.investors[$scope.user.userid] = {
                     assets : $scope.newpool.assets_suggestions,
                     value : $scope.newpool.first_investment
                     };
        $scope.user.usd_balance -= $scope.newpool.first_investment;
        $scope.newpool.$save().then(function() {
          console.log("pool saved!");
        }).catch(function(error) {
          alert(error);
        });
        $scope.newpool = Pool();
      }
    };
    
    //read existing pools into pools variable
    $scope.pools = ObjectsList("pools");

    //join existing pool
    $scope.enterPool = function(x) {
        if ($scope.user === undefined){
          alert("please sign in first");
          return;
        } 
      var current_investment = 0;
      console.log(x);  
      if (!(x.investors[$scope.user.userid] === undefined)){
        current_investment = x.investors[$scope.user.userid].value 
        if (current_investment > x.usd_spent_input){
          alert("Lesser values are not allowed");
          return;
        }
      }

      console.log(x.usd_spent_input);
      if (x.usd_spent_input < 0){
        alert("Negative values are not allowed");
        return;
      }
      x.investors[$scope.user.userid] = {
                       assets : x.assets_input_string,
                       value : x.usd_spent_input
                       };
      x.number_investors = Object.keys(x.investors).length 
      $scope.pools.$save(x);
      $scope.user.usd_balance += -x.usd_spent_input + current_investment;
      $scope.user.$save();
    }

    //make pool creation form visible
    $scope.showPoolForm = function() {
      if ($scope.user === undefined){
        alert("please sign in first")
      } else {
        document.getElementById("poolForm").classList.remove('hidden');
      }
    }

    $scope.showUserInfo = function() {
     document.getElementById("userInfo").classList.remove('hidden');
     document.getElementById("intro").classList.add('hidden');
    }

    $scope.hidePoolForm = function() {
     document.getElementById("poolForm").classList.add('hidden');
    }

});


