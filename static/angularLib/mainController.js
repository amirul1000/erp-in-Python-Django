'use strict';
//bootstrap ng-app="myApp"
angular.element(document).ready(function () {
    angular.bootstrap(document, ['myApp']);
});
//module for myApp decide route/controller/service/directive
var deskApp = angular.module('myApp', ['ngRoute', 'myControllers', 'myServices', 'ngCookies']);

//deskApp.constant('webAppConstant', 'http://api.demoavra.eu/');
deskApp.constant('webAppConstant', 'http://127.0.0.1:8000/');

deskApp.config(['$routeProvider',
        function ($routeProvider) {
            $routeProvider.when('/accounting/index/', {
                templateUrl: '/accounting/index.html',
                controller: 'homeController',
            }).when('/spacetree', {
                templateUrl: 'view/spacetree/spacetree.html',
                controller: 'spacetreeController'

            }).when('/information', {
                templateUrl: 'view/information/information.html',
                controller: 'informationController'

            }).when('/bar', {
                templateUrl: 'view/bar/bar.html',
                controller: 'barController'

            }).otherwise({
                redirectTo: '/home'
            });
            //$locationProvider.html5Mode(true); //For Remove #
        }])
    .run(function ($rootScope, $location, $cookies) {
        $rootScope.$on('$routeChangeStart', function (event, next) {
            $("#loader").fadeIn();
            var userData = $cookies.getObject('userData');

            $rootScope.authenticated = false;
            if (userData) {
                $rootScope.authenticated = true;
            }
            else {
                var nextUrl = next.$$route.originalPath;

                if (nextUrl == '/home' || nextUrl == '/home') {
                }
                else {
                    $location.path("/home");
                }
            }
        });
    });

var deskControllers = angular.module('myControllers', []);

var deskServices = angular.module('myServices', ['ngResource']);
