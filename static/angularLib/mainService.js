'use strict';


deskServices.factory('recalculate',['$resource','webAppConstant',
    function($resource,webAppConstant){
        return $resource(webAppConstant + 'Recalculate.php', {}, {
            query: { method: "POST"}
        });
    }]);

