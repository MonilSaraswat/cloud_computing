var cloudComputingApp = angular.module('cloudComputingApp', [
    'ngResource',
    'djng.forms',
    'djng.rmi',
]);

cloudComputingApp.config([
    'djangoRMIProvider',
    function (djangoRMIProvider) {
    djangoRMIProvider.configure(djangoRmiTags);
}]);