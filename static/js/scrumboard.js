(function(){
    'use strict';
    angular.module('scrumboard.demo',[])
    .controller('ScrumboardController', ['$scope','$http', ScrumboardController]);

    function ScrumboardController($scope,$http){
        $scope.data =[];
        $http.get('/scrumboard/lists/').then(
            function(response){
                $scope.data=response.data;
            }
        );

        $scope.add = function(list,title){
            var card ={
                list:list.id,
                title:title
            };
            $http.post('/scrumboard/cards/',card)
                .then(function(response){
                    list.cards.push(response.data);
                    $('.add-card-btn').val('');
                    return "";
                },
                function(){
                    alert('Failed to create a card');
                }
                );
        };

        $scope.addlist = function(data,name){
            var list={
                name:name,
                project:1
            };
            $http.post('/scrumboard/lists/',list)
                .then(function(response){
                    data.push(response.data);
                    $('.add-list-btn').val('');
                    return "";
                },
                function(){
                    alert('Failed to create a List');
                }
                );
        };

        $scope.deletelist =  function(list,data){
            //alert(list.id);
            var url = '/scrumboard/lists/'+list.id+'/';
            $http.delete(url).then(
                function(){
                    data.splice(data.indexOf(list),1);
                    $('.modal-backdrop').hide(); 
                }
            );
        };
    }
}());