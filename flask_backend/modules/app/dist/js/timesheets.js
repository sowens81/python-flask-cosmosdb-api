var app = angular.module('myApp', []);
app.controller('FormCtrl', function ($scope, $http) {
    
    $scope.data = {
        firstname: "default",
        lastname: "default",
        email: "default",
        password: "default"
    };
    $scope.submitForm = function() {
        console.log("posting data....");
        $http.post('http://posttestserver.com/post.php?dir=jsfiddle', JSON.stringify(data)).success(function(){/*success callback*/});
    };
});