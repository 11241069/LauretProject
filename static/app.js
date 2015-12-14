var myApp = angular.module('myApp', ['ngRoute']);

myApp.config(['$compileProvider', function ($compileProvider) {
    $compileProvider.debugInfoEnabled(false);
}]);
myApp.config(function ($routeProvider) {
    
    $routeProvider
    
    .when('/', {
        templateUrl: 'static/busqueda.html',
        controller: 'mainController'
    })
    
});
