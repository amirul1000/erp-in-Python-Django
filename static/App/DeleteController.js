angular.module('AngularDemo.DeleteController', ['ngRoute'])
app.controller('DeleteCtrl', function ($scope, CRUDService) {
    $scope.EmpAddressList = {};

    var GetAllData = CRUDService.getAllEmployeeInfo();
    GetAllData.then(function (data) {
        $scope.EmpAddressList = data.data;
    })

    $scope.DeleteByID = function (EmployeeID) {
        debugger;
        var DeletedEmployee = CRUDService.DeleteEmployee(EmployeeID);
        DeletedEmployee.then(function (Emp) {
            $scope.EmpAddressList = Emp.data;
        })
    }
});