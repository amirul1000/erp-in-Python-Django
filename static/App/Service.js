app.service("CRUDService", function ($http) {
    this.getAllEmployeeInfo = function () {
        return $http.get('/Home/ShowEmpList');
    };

    this.AddEmployee = function (EmployeeViewModel) {
        var ServerData = $http({
            method: "Post",
            url: "/Home/AddEmpDetails",
            data: JSON.stringify({ EmployeeViewModelClient: EmployeeViewModel }),
            dataType: 'json',
            //contentType: 'application/json',
        });
        return ServerData;
    }

    this.EditEmployee = function (EmployeeID) {
        var ServerData = $http({
            method: "Post",
            url: "/Home/GetEmployeeById",
            data: JSON.stringify({ EmpID: EmployeeID }),
            dataType: 'json',
            //contentType: 'application/json',
        });
        return ServerData;
    }

    this.UpdateEmployee = function (EmployeeViewModel) {
        var ServerData = $http({
            method: "Post",
            url: "/Home/UpdateEmployee",
            data: JSON.stringify({ EmployeeViewModelClient: EmployeeViewModel }),
            dataType: 'json',
            //contentType: 'application/json',
        });
        return ServerData;
    }

    this.DeleteEmployee = function (EmployeeID) {
        var ServerData = $http({
            method: "Post",
            url: "/Home/DeleteByID",
            data: JSON.stringify({ EmpID: EmployeeID }),
            dataType: 'json',
            //contentType: 'application/json',
        });
        return ServerData;
    }
});