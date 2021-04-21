cloudComputingApp.controller('mainCtrl', [
    '$scope',
    'djangoRMI',
    '$timeout',
    function($scope, djangoRMI, $timeout){
        $("#id_image").change(function(){
            var uploadInput = document.getElementById("id_image");
            $scope.uploadedItems = false;
            $timeout(function(){
                selectImage();
            },1);
        });

        function selectImage(){
            var file = document.getElementById("id_image").files[0];
            $scope.selectedFile = {
                filePath: (window.URL || window.webkitURL).createObjectURL(file),
                fileName: file.name,
                fileSize: file.size/1024000,
                fileType: file.type,
                fileLastModified: file.lastModifiedDate,
            } ;
        }

        $scope.onClickListBtn = function(){
            djangoRMI.list_all_images({}).then(function(response){
                $scope.selectedFile = false;
                $scope.uploadedItems = response.data.all_items;
            }, function(err){
                console.log(err);
            });
        }

    }
]);

cloudComputingApp.controller('metaCtrl', [
    '$scope',
    function($scope){

        var data = JSON.parse($('#id_data').val() || {});
        $scope.fetchedData = data;
    }
]);