angular.module('AngularDemo.EmpAddController', ['ngRoute'])
app.controller('EmpAddCtrl', function ($scope, CRUDService) {
    //debugger;
    var GetAllData = CRUDService.getAllEmployeeInfo();
    GetAllData.then(function (data) {
        $scope.EmpAddressList = data.data;
        //console.log($scope.EmpAddressList);
    })

    $scope.EmpAddressList = {};
    $scope.EmpDetailsModel =
     {
         EmpID: '',
         EmpName: '',
         EmpPhone: ''
     };

    $scope.EmpAddressModel =
    {
        Address1: '',
        Address2: '',
        Address3: ''
    };

    $scope.EmployeeViewModel = {
        empDetailModel: $scope.EmpDetailsModel,
        empAddressModel: $scope.EmpAddressModel
    };

    $scope.AddEmployee = function () {
        var NewEmployee = CRUDService.AddEmployee($scope.EmployeeViewModel);
        NewEmployee.then(function (emp) {
            $scope.EmpAddressList.push(emp.data[0]);
        })
    }
});