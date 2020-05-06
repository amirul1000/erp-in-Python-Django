angular.module('AngularDemo.AddressController', ['ngRoute'])
app.controller('EditCtrl', function ($scope, CRUDService) {

    var GetAllData = CRUDService.getAllEmployeeInfo();
    GetAllData.then(function (data) {
        $scope.EmpAddressList = data.data;
    })

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

    $scope.EditEmployee = function (EmployeeID) {
        var EditedEmployee = CRUDService.EditEmployee(EmployeeID);
        EditedEmployee.then(function (Emp) {
            $scope.EmpDetailsModel.EmpID = Emp.data[0].empDetailModel.EmpID;
            $scope.EmpDetailsModel.EmpName = Emp.data[0].empDetailModel.EmpName;
            $scope.EmpDetailsModel.EmpPhone = Emp.data[0].empDetailModel.EmpPhone;
            $scope.EmpAddressModel.Address1 = Emp.data[0].empAddressModel.Address1
            $scope.EmpAddressModel.Address2 = Emp.data[0].empAddressModel.Address2;
            $scope.EmpAddressModel.Address3 = Emp.data[0].empAddressModel.Address3;
            $scope.$apply();
        })
    };

    $scope.UpdateEmployee = function () {
        var UpdatedEmployee = CRUDService.UpdateEmployee($scope.EmployeeViewModel);
        UpdatedEmployee.then(function (Emp) {
            $scope.EmpAddressList = Emp.data;
            $scope.$apply();
        })
    };
});