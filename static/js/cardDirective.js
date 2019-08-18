(function(){
    'use strict';
    angular.module('scrumboard.demo')
        .directive('scrumboardCard',CardDirective);

    function CardDirective(){
        return {
            templateUrl:'/static/html/card.html',
            restrict: 'E',
            controller: ['$scope','$http', function($scope,$http){
                var url = '/scrumboard/cards/'+$scope.card.id+'/';
                $scope.update = function(){
                    $http.put(url,$scope.card).then(function(){
                        return false;
                    });
                };
                
                $scope.delete =  function(){
                    //alert($scope.list.id);
                    $http.delete(url).then(
                    function(){
                        var cards = $scope.list.cards;
                        cards.splice(cards.indexOf($scope.card),1);
                        return false;
                    }
                    );
                };

                $scope.movecard = function(movelist,card){
                    card.list=movelist;
                    $http.put(url,card).then(function(){
                        var cards = $scope.list.cards;
                        cards.splice(cards.indexOf($scope.card),1);
                        for(var key in $scope.data){
                            var list = $scope.data[key];
                            if(list.id==movelist){
                                list.cards.push(card);
                            }
                        }
                        $('.modal-backdrop').hide(); 
                        //alert("Move Success");
                    });
                };


            }]
        };
    }
})();