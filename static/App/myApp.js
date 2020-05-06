var app = angular.module('App', ['AngularDemo.EmpAddController',
                       'AngularDemo.AddressController',
                       'AngularDemo.DeleteController'
])

app.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider) {

    $routeProvider.when('/', {
        templateUrl: '/Home/AddEmployee',
        controller: 'EmpAddCtrl',
    });
    $routeProvider.when('/Edit', {
        templateUrl: '/Home/EditEmployee',
        controller: 'EditCtrl'
    });
    $routeProvider.when('/Delete', {
        templateUrl: '/Home/DeleteEmployee',
        controller: 'DeleteCtrl'
    });
    $routeProvider.otherwise({
        redirectTo: '/'
    });
    // Specify HTML5 mode (using the History APIs) or HashBang syntax.
    $locationProvider.html5Mode(false).hashPrefix('!');

}]);

////Add Employee Controller
//angular.module('AngularDemo.EmpAddController', ['ngRoute'])
//.controller('EmpAddCtrl', function ($scope, $http) {

//    $scope.EmpAddressList = {};
//    $http.get('/Home/ShowEmpList').success(function (data) {
//        $scope.EmpAddressList = data;
//    });


//    $scope.EmpDetailsModel =
//     {
//         EmpID: '',
//         EmpName: '',
//         EmpPhone: ''
//     };

//    $scope.EmpAddressModel =
//    {
//        Address1: '',
//        Address2: '',
//        Address3: ''
//    };

//    $scope.EmployeeViewModel = {
//        empDetailModel: $scope.EmpDetailsModel,
//        empAddressModel: $scope.EmpAddressModel
//    };



//    $scope.AddEmployee = function () {
//        //debugger;
//        $.ajax({
//            url: '/Home/AddEmpDetails',
//            type: 'POST',
//            dataType: 'json',
//            contentType: 'application/json',
//            traditional: true,
//            cache: false,
//            data: JSON.stringify({ EmployeeViewModelClient: $scope.EmployeeViewModel }),
//            success: function (data) {
//                $scope.EmpAddressList.push(data[0]);
//                $scope.$apply();
//                //$scope.$apply();
//                alert("Record is been added");
//            }
//        });
//    };
//});

////Address Controller
//angular.module('AngularDemo.AddressController', ['ngRoute'])
//.controller('EditCtrl', function ($scope, $http) {

//    $scope.EmpAddressList = {};
//    $http.get('/Home/ShowEmpList').success(function (data) {
//        $scope.EmpAddressList = data;

//    });
//    $scope.EmpDetailsModel =
//     {
//         EmpID: '',
//         EmpName: '',
//         EmpPhone: ''
//     };

//    $scope.EmpAddressModel =
//    {
//        Address1: '',
//        Address2: '',
//        Address3: ''
//    };

//    $scope.EmployeeViewModel = {
//        empDetailModel: $scope.EmpDetailsModel,
//        empAddressModel: $scope.EmpAddressModel
//    };


//    $scope.EditEmployee = function (EmployeeID) {
//        $.ajax({
//            url: '/Home/GetEmployeeById',
//            type: 'POST',
//            dataType: 'json',
//            contentType: 'application/json',
//            traditional: true,
//            data: JSON.stringify({ EmpID: EmployeeID }),
//            cache: false,
//            success: function (data) {
//                $scope.EmpDetailsModel.EmpID = data[0].empDetailModel.EmpID;
//                $scope.EmpDetailsModel.EmpName = data[0].empDetailModel.EmpName;
//                $scope.EmpDetailsModel.EmpPhone = data[0].empDetailModel.EmpPhone;
//                $scope.EmpAddressModel.Address1 = data[0].empAddressModel.Address1
//                $scope.EmpAddressModel.Address2 = data[0].empAddressModel.Address2;
//                $scope.EmpAddressModel.Address3 = data[0].empAddressModel.Address3;
//                $scope.$apply();

//            }
//        });

//    };

//    $scope.UpdateEmployee = function () {

//        $.ajax({
//            url: '/Home/UpdateEmployee',
//            type: 'POST',
//            dataType: 'json',
//            contentType: 'application/json',
//            traditional: true,
//            data: JSON.stringify({ EmployeeViewModelClient: $scope.EmployeeViewModel }),
//            cache: false,
//            success: function (data) {
//                $scope.EmpAddressList = data;
//                $scope.$apply();
//            }
//        });
//    };
//});

//angular.module('AngularDemo.DeleteController', ['ngRoute'])
//.controller('DeleteCtrl', function ($scope, $http) {
//    //$scope.Message = "Delete in Part 2 is coming soon";

//    $scope.EmpAddressList = {};
//    $http.get('/Home/ShowEmpList').success(function (data) {
//        $scope.EmpAddressList = data;
//    });

//    $scope.DeleteByID = function (EmployeeID) {

//        $.ajax({
//            url: '/Home/DeleteByID',
//            type: 'POST',
//            dataType: 'json',
//            contentType: 'application/json',
//            traditional: true,
//            cache: false,
//            data: JSON.stringify({ EmpID: EmployeeID }),
//            success: function (data) {
//                $scope.EmpAddressList = data;
//                $scope.$apply();
//            }
//        });

//    };
//});

