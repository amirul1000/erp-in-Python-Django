deskApp.directive('focus', function () {
    return function (scope, element) {
        element[0].focus();
    }
});

deskApp.directive('deskHeader', function () {
    return {
        restrict: 'E',
        templateUrl: 'view/layout/header.html',
        controller: ['$scope', '$window',
            function ($scope, $window) {

                //$(".shortcutButton").click(function(){$(".shortcut").hasClass("hidden")? $(".shortcut").removeClass("hidden"): $(".shortcut").addClass("hidden")});
                $("#shortcutButton").click(function(){$('.shortcut').css('display') == 'none'? $('.shortcut').css('display','block'): $('.shortcut').css('display','none')});
                $("#menuButton").click(function(){$('.menubar').css('display') == 'none'? $('.menubar').css('display','block'): $('.menubar').css('display','none')});



            }]
    }
});

deskApp.directive('deskFooter', function () {
    return {
        restrict: 'E',
        templateUrl: 'view/layout/footer.html',
        controller: ['$scope', '$http',
            function ($scope, $http) {
            }]
    }
});

deskApp.directive('deskSidebar', function () {
    return {
        restrict: 'E',
        templateUrl: 'view/layout/sidebar.html',
        controller: ['$scope', '$http',
            function ($scope, $http) {
            }]
    }
});

deskApp.directive('deskMenubar', function () {
    return {
        restrict: 'E',
        templateUrl: 'view/layout/menuBar.html',
        controller: ['$scope', '$http',
            function ($scope, $http) {
            }]
    }
});

deskApp.directive('deskPopup', function () {
    return {
        restrict: 'E',
        transclude: true,
        replace:true,
        scope:true,
        templateUrl: 'view/layout/popupModel.html',
        controller: ['$scope', '$http',
            function ($scope, $http) {
            }],

        link: function postLink(scope, element, attrs) {
            scope.title = attrs.title;

            scope.$watch(attrs.visible, function(value){
                if(value == true)
                    $(element).modal('show');
                else
                    $(element).modal('hide');
            });

            $(element).on('shown.bs.modal', function(){
                scope.$apply(function(){
                    scope.$parent[attrs.visible] = true;
                });
            });

            $(element).on('hidden.bs.modal', function(){
                scope.$apply(function(){
                    scope.$parent[attrs.visible] = false;
                });
            });
        }
    };
});

deskApp.directive("whenScrolled", function(){
    return{

        restrict: 'A',
        link: function(scope, elem, attrs){

            // we get a list of elements of size 1 and need the first element
            raw = elem[0];

            // we load more elements when scrolled past a limit
            elem.scroll(function() {
                if(elem.scrollTop() + elem.height() > elem.height() - 100) {
                    scope.$apply(attrs.whenScrolled);
                    alert("near bottom!");
                }
            });
            elem.bind('scroll', function()
            {
                if($(this).scrollTop() + $(this).innerHeight()>=$(this)[0].scrollHeight)
                {
                    scope.$apply(attrs.whenScrolled);
                    alert('end reached');
                }
            })
        }
    }
});

deskApp.directive('fileModel', ['$parse', function ($parse) {
    return {
        restrict: 'A',
        link: function(scope, element, attrs) {
            var model = $parse(attrs.fileModel);
            var modelSetter = model.assign;

            element.bind('change', function(){
                scope.$apply(function(){
                    modelSetter(scope, element[0].files[0]);
                });
            });
        }
    };
}]);

