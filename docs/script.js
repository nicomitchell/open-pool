var config = {
  apiKey: "AIzaSyBdC5IFAhQx7m8LDPg8NZln7rPU4QwyQRQ",
  authDomain: "open-pool.firebaseapp.com",
  databaseURL: "https://open-pool.firebaseio.com",
  projectId: "open-pool",
  storageBucket: "open-pool.appspot.com",
  messagingSenderId: "569437181618"
};
firebase.initializeApp(config);
var app = angular.module("openPool", ["firebase"]);


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
    return function(username) {
      // create a reference to the database node where we will store our data
      var ref = firebase.database().ref("accounts").push();
      var profileRef = ref.child(username);

      // return it as a synchronized object
      return $firebaseObject(profileRef);
    }
  }
]);

app.controller('myCtrl', function($scope, Pool) {
    $scope.user = "no user";
    //login
    $scope.login = function() {
      firebase.auth().signInWithRedirect(provider);
    };
    //logout
    $scope.logout = function() {
      firebase.auth().signOut().then(function() {
        $scope.user = "log out";
        $scope.$apply()
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
        $scope.user = result.user.email;
        $scope.userid = result.user.email.substring(0, result.user.email.indexOf("@"));
        $scope.$apply()
      }
      // The signed-in user info.
      var user = result.user;
    }).catch(function(error) {
      console.log(error);
    });

    //save user's new pool
    $scope.saveNewPool = function() {
          $scope.pool = Pool($scope.userid);
          $scope.pool.$save().then(function() {
            alert('Pool saved!');
          }).catch(function(error) {
            alert('Error!');
          });
        };

    //read existing pools into pools variable
    $scope.pools = 

});
